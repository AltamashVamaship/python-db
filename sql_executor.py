"""
SQL query executor that executes SQL and makes results available for Python manipulation
"""
from db_helper import DatabaseHelper
from datetime import datetime, date
from decimal import Decimal
import json


def json_serializer(obj):
    """Custom JSON serializer for datetime and Decimal objects"""
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    elif isinstance(obj, Decimal):
        return float(obj)
    raise TypeError(f"Type {type(obj)} not serializable")


def execute_sql_with_python(sql_query, python_code=None):
    """
    Execute SQL query and optionally run Python code to manipulate results
    
    Args:
        sql_query: SQL query string
        python_code: Optional Python code to manipulate the SQL results
        
    Returns:
        tuple: (success: bool, result: dict or error: str)
    """
    # Security: Block dangerous SQL operations
    sql_lower = sql_query.lower().strip()
    forbidden_sql = ['drop', 'delete', 'truncate', 'alter', 'create', 'insert', 'update']
    
    # Allow SELECT only (read-only)
    if not sql_lower.startswith('select'):
        return False, "Only SELECT queries are allowed for security reasons"
    
    for keyword in forbidden_sql:
        if f' {keyword} ' in sql_lower or sql_lower.startswith(keyword):
            return False, f"Security: '{keyword.upper()}' operations are not allowed. Only SELECT queries are permitted."
    
    # Execute SQL query
    db = DatabaseHelper()
    try:
        if not db.connect():
            return False, "Failed to connect to database"
        
        # Execute SQL
        sql_results = db.execute_query(sql_query)
        
        if sql_results is None:
            return False, "SQL query execution failed"
        
        # Convert to JSON-serializable format
        serialized_results = []
        for row in sql_results:
            serialized_row = {}
            for key, value in row.items():
                serialized_row[key] = json_serializer(value) if not isinstance(value, (int, float, str, bool, type(None))) else value
            serialized_results.append(serialized_row)
        
        # If no Python code, just return SQL results
        if not python_code or not python_code.strip():
            return True, {
                'query_result': serialized_results,
                'python_output': None,
                'python_data': serialized_results,
                'row_count': len(serialized_results)
            }
        
        # Execute Python code with SQL results available as 'result' variable
        import io
        from contextlib import redirect_stdout, redirect_stderr
        
        # Security: Block dangerous Python operations
        python_lower = python_code.lower()
        forbidden_keywords = [
            'import', 'exec', 'eval', 'compile', '__import__', 'open', 'file',
            'input', 'raw_input', 'reload', '__builtins__', 'globals', 'locals',
            'vars', 'dir', 'getattr', 'setattr', 'delattr', 'hasattr',
            'exit', 'quit', 'sys', 'os', 'subprocess', 'shutil', 'pickle',
            'marshal', 'ctypes', '__file__', '__name__', 'breakpoint'
        ]
        
        for keyword in forbidden_keywords:
            if keyword in python_lower:
                return False, f"Security: '{keyword}' is not allowed in Python code"
        
        # Prepare execution environment
        exec_globals = {
            'result': serialized_results,  # SQL results available as 'result'
            'len': len,
            'list': list,
            'dict': dict,
            'str': str,
            'int': int,
            'float': float,
            'sum': sum,
            'max': max,
            'min': min,
            'sorted': sorted,
            'enumerate': enumerate,
            'zip': zip,
            'print': print,
        }
        
        # List to capture printed data
        printed_data_list = []
        
        # Custom print function that converts objects to dicts
        def smart_print(*args, **kwargs):
            """Print function that automatically converts objects to dictionaries"""
            import json as json_module
            
            def convert_to_dict(obj):
                """Convert object to dictionary"""
                if isinstance(obj, (list, tuple)):
                    return [convert_to_dict(item) for item in obj]
                elif isinstance(obj, dict):
                    return {k: convert_to_dict(v) for k, v in obj.items()}
                elif isinstance(obj, (int, float, str, bool, type(None))):
                    return obj
                elif isinstance(obj, (datetime, date)):
                    return obj.isoformat()
                elif isinstance(obj, Decimal):
                    return float(obj)
                else:
                    return str(obj)
            
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
                    for item in converted:
                        if isinstance(item, dict):
                            printed_data_list.append(item)
                
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
            
            print(*converted_args, **kwargs)
        
        exec_globals['print'] = smart_print
        
        # Capture stdout/stderr
        stdout_capture = io.StringIO()
        stderr_capture = io.StringIO()
        
        # Execute Python code
        with redirect_stdout(stdout_capture), redirect_stderr(stderr_capture):
            try:
                exec(compile(python_code, '<string>', 'exec'), exec_globals)
            except Exception as e:
                return False, f"Python execution error: {str(e)}"
        
        stdout_output = stdout_capture.getvalue()
        stderr_output = stderr_capture.getvalue()
        
        if stderr_output:
            return False, f"Error: {stderr_output}"
        
        # Return combined results
        return True, {
            'query_result': serialized_results,  # Original SQL results
            'python_output': stdout_output.strip() if stdout_output else None,
            'python_data': printed_data_list,  # Data from print statements
            'row_count': len(serialized_results)
        }
        
    except Exception as e:
        return False, f"Error: {str(e)}"
    finally:
        db.disconnect()

