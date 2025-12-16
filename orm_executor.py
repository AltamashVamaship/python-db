"""
Safe Python ORM code executor
Executes Python ORM queries in a sandboxed environment
"""
import sys
import io
from contextlib import redirect_stdout, redirect_stderr
from models import SessionLocal, Base
from sqlalchemy import func, and_, or_, desc, asc
from sqlalchemy.orm import Query
import json
from datetime import datetime, date
from decimal import Decimal


# Allowed imports and functions for the sandbox
ALLOWED_BUILTINS = {
    'len', 'str', 'int', 'float', 'list', 'dict', 'tuple', 'set',
    'min', 'max', 'sum', 'abs', 'round', 'range', 'enumerate',
    'zip', 'sorted', 'reversed', 'any', 'all', 'isinstance',
    'type', 'hasattr', 'getattr', 'setattr', 'dir', 'vars'
}

ALLOWED_SAFEBUILTINS = {
    '__builtins__': {k: v for k, v in __builtins__.items() if k in ALLOWED_BUILTINS}
}


def json_serializer(obj):
    """Custom JSON serializer for datetime and Decimal objects"""
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    elif isinstance(obj, Decimal):
        return float(obj)
    elif isinstance(obj, (int, float, str, bool)) or obj is None:
        # Basic JSON-serializable types
        return obj
    elif isinstance(obj, (list, tuple)):
        return [json_serializer(item) for item in obj]
    elif isinstance(obj, dict):
        return {k: json_serializer(v) for k, v in obj.items()}
    elif hasattr(obj, '__dict__'):
        return {k: json_serializer(v) for k, v in obj.__dict__.items() if not k.startswith('_')}
    else:
        # Fallback: convert to string
        return str(obj)


def execute_orm_query(code):
    """
    Safely execute Python ORM code and return results
    
    Args:
        code: Python code string with ORM query
        
    Returns:
        tuple: (success: bool, result: list/dict or error: str)
    """
    # Security: Block dangerous operations
    forbidden_keywords = [
        'import', 'exec', 'eval', 'compile', '__import__', 'open', 'file',
        'input', 'raw_input', 'reload', '__builtins__', 'globals', 'locals',
        'vars', 'dir', 'getattr', 'setattr', 'delattr', 'hasattr',
        'exit', 'quit', 'sys', 'os', 'subprocess', 'shutil', 'pickle',
        'marshal', 'ctypes', '__file__', '__name__', 'breakpoint'
    ]
    
    code_lower = code.lower()
    for keyword in forbidden_keywords:
        if keyword in code_lower:
            return False, f"Security: '{keyword}' is not allowed"
    
    # Helpful fix: Check for common mistake - get_table without quotes
    import re
    # Pattern: get_table(variable_name) where variable_name is not a string
    pattern = r'get_table\(([a-zA-Z_][a-zA-Z0-9_]*)\)'
    matches = re.findall(pattern, code)
    if matches:
        for match in matches:
            # Check if it's not already quoted
            if f'get_table("{match}")' not in code and f"get_table('{match}')" not in code:
                return False, f'Error: Table name must be a string. Use get_table("{match}") instead of get_table({match})'
    
    # Auto-capture: Find query expressions and automatically assign them to 'result'
    # This allows users to write: session.query(Entities).limit(10).all()
    # Without needing: result = session.query(Entities).limit(10).all()
    lines = code.strip().split('\n')
    query_methods = ['.all()', '.first()', '.one()', '.scalar()', '.count()']
    query_found = False
    
    # Find the first query expression that's not already assigned
    for i, line in enumerate(lines):
        line_stripped = line.strip()
        # Skip comments and empty lines
        if not line_stripped or line_stripped.startswith('#'):
            continue
        
        # Check if this line is a query expression (not an assignment, not a print)
        has_query_method = any(method in line_stripped for method in query_methods)
        has_query = 'session.query' in line_stripped or '.query(' in line_stripped or 'get_table(' in line_stripped
        is_assignment = '=' in line_stripped.split('#')[0]
        is_print = line_stripped.startswith('print')
        
        if has_query_method and has_query and not is_assignment and not is_print:
            # This is a query expression - wrap it to assign to result
            # Preserve indentation
            indent = len(line) - len(line.lstrip())
            lines[i] = ' ' * indent + f'result = {line_stripped}'
            query_found = True
            break  # Only wrap the first query expression
    
    if query_found:
        code = '\n'.join(lines)
    
    # Create a new session
    session = SessionLocal()
    
    try:
        # Prepare the execution environment
        exec_globals = {
            '__builtins__': ALLOWED_SAFEBUILTINS['__builtins__'],
            'session': session,
            'func': func,
            'and_': and_,
            'or_': or_,
            'desc': desc,
            'asc': asc,
            'Query': Query,
            'json': json,
            'datetime': datetime,
            'date': date,
        }
        
        # Import all models dynamically
        from models import Base, get_table, get_all_tables
        import models
        
        # Add all model classes to exec_globals
        for name in dir(models):
            obj = getattr(models, name)
            if isinstance(obj, type) and issubclass(obj, Base) and obj != Base:
                exec_globals[name] = obj
        
        # Add dynamic table access
        exec_globals['get_table'] = get_table
        exec_globals['get_all_tables'] = get_all_tables
        
        # Add Table class for dynamic queries
        from sqlalchemy import Table as SQLTable
        exec_globals['Table'] = SQLTable
        
        # List to capture printed data for table view
        printed_data_list = []
        
        # Custom print function that converts ORM objects to dicts
        def smart_print(*args, **kwargs):
            """Print function that automatically converts ORM objects to dictionaries"""
            import sys
            import json as json_module
            
            def convert_to_dict(obj):
                """Convert ORM object to dictionary with proper serialization"""
                if hasattr(obj, '__dict__') and not isinstance(obj, (int, float, str, bool, type(None), list, dict, tuple)):
                    try:
                        if hasattr(obj, '_mapping'):
                            # SQLAlchemy Row object
                            return dict(obj._mapping)
                        elif hasattr(obj, '_fields'):
                            # Older Row object
                            item_dict = {}
                            for field in obj._fields:
                                value = getattr(obj, field)
                                item_dict[field] = json_serializer(value)
                            return item_dict
                        elif hasattr(obj, '__table__') or hasattr(obj, '__tablename__'):
                            # SQLAlchemy model instance
                            item_dict = {}
                            for key, value in obj.__dict__.items():
                                if not key.startswith('_'):
                                    item_dict[key] = json_serializer(value)
                            return item_dict
                        else:
                            # Generic object with __dict__
                            item_dict = {}
                            for key, value in obj.__dict__.items():
                                if not key.startswith('_'):
                                    item_dict[key] = json_serializer(value)
                            return item_dict
                    except Exception:
                        return obj
                elif isinstance(obj, (list, tuple)):
                    # Convert list/tuple of ORM objects
                    converted = []
                    for item in obj:
                        converted.append(convert_to_dict(item))
                    return converted if isinstance(obj, list) else tuple(converted)
                else:
                    return json_serializer(obj) if not isinstance(obj, (int, float, str, bool, type(None))) else obj
            
            def sort_dict_keys(obj):
                """Recursively sort dictionary keys alphabetically"""
                if isinstance(obj, dict):
                    return {k: sort_dict_keys(v) for k, v in sorted(obj.items())}
                elif isinstance(obj, list):
                    return [sort_dict_keys(item) for item in obj]
                else:
                    return obj
            
            converted_args = []
            for arg in args:
                converted = convert_to_dict(arg)
                
                # Store dict/list data for table view
                if isinstance(converted, dict):
                    printed_data_list.append(converted)
                elif isinstance(converted, list):
                    # If it's a list of dicts, add all items
                    for item in converted:
                        if isinstance(item, dict):
                            printed_data_list.append(item)
                    # Also add the list itself if it's not empty
                    if converted and not all(isinstance(x, dict) for x in converted):
                        printed_data_list.extend(converted)
                
                # Sort dictionary keys alphabetically
                if isinstance(converted, (dict, list)):
                    converted = sort_dict_keys(converted)
                    try:
                        formatted = json_module.dumps(converted, indent=2, default=json_serializer, ensure_ascii=False)
                        converted_args.append(formatted)
                    except Exception:
                        converted_args.append(str(converted))
                else:
                    converted_args.append(converted)
            
            # Use the original print with converted args
            print(*converted_args, **kwargs)
        
        exec_globals['print'] = smart_print
        exec_globals['len'] = len
        exec_globals['list'] = list
        exec_globals['dict'] = dict
        exec_globals['str'] = str
        exec_globals['int'] = int
        exec_globals['float'] = float
        exec_globals['sum'] = sum
        exec_globals['max'] = max
        exec_globals['min'] = min
        exec_globals['sorted'] = sorted
        exec_globals['enumerate'] = enumerate
        exec_globals['zip'] = zip
        
        # Capture stdout/stderr
        stdout_capture = io.StringIO()
        stderr_capture = io.StringIO()
        
        # Execute the code
        with redirect_stdout(stdout_capture), redirect_stderr(stderr_capture):
            # Initialize result variable
            exec_globals['result'] = None
            
            # Execute the user's code
            exec(compile(code, '<string>', 'exec'), exec_globals)
            
            # Capture stdout output
            stdout_output = stdout_capture.getvalue()
            
            # Try to get result from various possible variable names
            result = exec_globals.get('result')
            
            # If result is None, try to find common variable names
            if result is None:
                for var_name in ['results', 'data', 'query_result', 'output']:
                    if var_name in exec_globals:
                        result = exec_globals[var_name]
                        # Also store it in result for consistency
                        exec_globals['result'] = result
                        break
            
            # If still no result, try to capture the last expression
            # This handles cases like: session.query(Entities).limit(10).all()
            if result is None:
                # Try to evaluate the last line as an expression
                lines = [line.strip() for line in code.strip().split('\n') if line.strip() and not line.strip().startswith('#')]
                if lines:
                    last_line = lines[-1]
                    # Check if it looks like a query (contains .query( or .all() or .first() etc.)
                    # But not if it's an assignment or print statement
                    if (not last_line.startswith('print') and 
                        not '=' in last_line.split('#')[0] and  # Not an assignment
                        any(method in last_line for method in ['.all()', '.first()', '.one()', '.scalar()', '.count()', '.limit(', '.filter(', '.order_by('])):
                        try:
                            # Try to evaluate the last line
                            last_result = eval(compile(last_line, '<string>', 'eval'), exec_globals)
                            if last_result is not None:
                                result = last_result
                                exec_globals['result'] = result
                        except Exception:
                            # If evaluation fails, that's okay - user might have already assigned it
                            pass
        
        # Check for errors
        stderr_output = stderr_capture.getvalue()
        if stderr_output:
            return False, f"Error: {stderr_output}"
        
        # Prepare response with both query results and Python output
        response_data = {
            'query_result': None,
            'python_output': stdout_output.strip() if stdout_output else None,
            'python_data': printed_data_list,  # Captured data from print statements for table view
            'has_result': result is not None
        }
        
        # Convert result to JSON-serializable format if it exists
        # Note: result is now automatically captured from queries
        # If result is None but there's output, that's okay (user might just be printing)
        # Only error if there's no result AND no output
        if result is None and not stdout_output:
            return False, "No result returned. Write a query like 'session.query(Entities).limit(10).all()' or assign it to a variable."
        
        # Handle different result types and serialize
        def serialize_result(res):
            """Helper function to serialize a result"""
            if isinstance(res, (list, tuple)):
                # Convert ORM objects to dicts
                serialized = []
                for item in res:
                    if isinstance(item, (int, float, str, bool, type(None))):
                        # Primitive type
                        serialized.append(json_serializer(item))
                    elif hasattr(item, '_mapping') or hasattr(item, '_fields'):
                        # SQLAlchemy Row object (2.0 style with _mapping or older with _fields)
                        item_dict = {}
                        try:
                            # Try SQLAlchemy 2.0 style (Row._mapping)
                            if hasattr(item, '_mapping'):
                                item_dict = dict(item._mapping)
                            # Try older style (Row._fields)
                            elif hasattr(item, '_fields'):
                                for field in item._fields:
                                    value = getattr(item, field)
                                    item_dict[field] = json_serializer(value)
                            # Try direct dict conversion
                            else:
                                item_dict = dict(item)
                        except Exception:
                            # Fallback: try _asdict() method
                            try:
                                item_dict = item._asdict()
                            except Exception:
                                # Last resort: convert to dict using keys()
                                item_dict = {str(k): json_serializer(v) for k, v in zip(item.keys(), item)}
                        
                        # Serialize all values in the dict
                        serialized.append({k: json_serializer(v) for k, v in item_dict.items()})
                    elif hasattr(item, '__dict__'):
                        # SQLAlchemy model instance
                        item_dict = {}
                        for key, value in item.__dict__.items():
                            if not key.startswith('_'):
                                item_dict[key] = json_serializer(value)
                        serialized.append(item_dict)
                    elif hasattr(item, 'keys') and callable(item.keys):
                        # Row-like object with keys() method
                        try:
                            item_dict = {k: json_serializer(v) for k, v in zip(item.keys(), item)}
                            serialized.append(item_dict)
                        except Exception:
                            serialized.append(json_serializer(item))
                    else:
                        # Unknown type, try to serialize
                        serialized.append(json_serializer(item))
                return serialized
            elif isinstance(res, (int, float, str, bool, type(None))):
                # Primitive type - wrap in dict for consistency
                return [{'value': json_serializer(res)}]
            elif hasattr(res, '_mapping') or hasattr(res, '_fields'):
                # Single SQLAlchemy Row object
                item_dict = {}
                try:
                    if hasattr(res, '_mapping'):
                        item_dict = dict(res._mapping)
                    elif hasattr(res, '_fields'):
                        for field in res._fields:
                            value = getattr(res, field)
                            item_dict[field] = json_serializer(value)
                    else:
                        item_dict = dict(res)
                except Exception:
                    try:
                        item_dict = res._asdict()
                    except Exception:
                        item_dict = {str(k): json_serializer(v) for k, v in zip(res.keys(), res)}
                
                item_dict = {k: json_serializer(v) for k, v in item_dict.items()}
                return [item_dict]
            elif hasattr(res, '__dict__'):
                # Single model instance
                item_dict = {}
                for key, value in res.__dict__.items():
                    if not key.startswith('_'):
                        item_dict[key] = json_serializer(value)
                return [item_dict]
            elif hasattr(res, 'keys') and callable(res.keys):
                # Row-like object
                try:
                    item_dict = {k: json_serializer(v) for k, v in zip(res.keys(), res)}
                    return [item_dict]
                except Exception:
                    return [{'value': json_serializer(res)}]
            else:
                # Unknown type
                return [{'value': json_serializer(res)}]
        
        # Serialize the query result
        if result is not None:
            response_data['query_result'] = serialize_result(result)
        
        return True, response_data
            
    except Exception as e:
        return False, f"Error: {str(e)}"
    finally:
        session.close()

