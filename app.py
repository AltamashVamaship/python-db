#!/usr/bin/env python3
"""
Web interface for running Python ORM queries on the database
"""
from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from orm_executor import execute_orm_query
from sql_executor import execute_sql_with_python
from db_helper import DatabaseHelper
import json
from datetime import datetime, date
from decimal import Decimal
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your-secret-key-change-this-in-production'  # Change this to a random secret key

# Authentication credentials
VALID_EMAIL = 'rahul.sharma@vamaship.com'
VALID_PASSWORD = 'Vama@1234#'


def json_serializer(obj):
    """Custom JSON serializer for datetime and Decimal objects"""
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    elif isinstance(obj, Decimal):
        return float(obj)
    raise TypeError(f"Type {type(obj)} not serializable")


def login_required(f):
    """Decorator to require login for routes"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('authenticated'):
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login page"""
    if request.method == 'POST':
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '').strip()
        
        if email == VALID_EMAIL and password == VALID_PASSWORD:
            session['authenticated'] = True
            session['email'] = email
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error='Invalid email or password')
    
    # If already authenticated, redirect to main page
    if session.get('authenticated'):
        return redirect(url_for('index'))
    
    return render_template('login.html')


@app.route('/logout')
def logout():
    """Logout and clear session"""
    session.clear()
    return redirect(url_for('login'))


@app.route('/')
@login_required
def index():
    """Main page with query interface"""
    return render_template('index.html')


@app.route('/api/query', methods=['POST'])
@login_required
def execute_query():
    """Execute Python ORM query or SQL query and return results"""
    try:
        data = request.get_json()
        code = data.get('query', '').strip()
        query_mode = data.get('mode', 'orm').lower()  # 'orm' or 'sql'
        
        if not code:
            return jsonify({
                'success': False,
                'error': 'Query cannot be empty'
            }), 400
        
        if query_mode == 'sql':
            # Execute SQL query
            # Split SQL and Python code if both are present
            # Look for SQL query (starts with SELECT) and optional Python code after
            lines = code.split('\n')
            sql_lines = []
            python_lines = []
            in_python_section = False
            
            for line in lines:
                line_stripped = line.strip()
                if line_stripped.upper().startswith('SELECT'):
                    in_python_section = False
                    sql_lines.append(line)
                elif line_stripped and not in_python_section:
                    # Check if it's still SQL (common SQL keywords)
                    sql_keywords = ['FROM', 'WHERE', 'JOIN', 'GROUP BY', 'ORDER BY', 'HAVING', 'LIMIT', 'UNION', 'AND', 'OR']
                    if any(keyword in line_stripped.upper() for keyword in sql_keywords) or line_stripped.endswith(';'):
                        sql_lines.append(line)
                    else:
                        # Switch to Python section
                        in_python_section = True
                        python_lines.append(line)
                elif in_python_section:
                    python_lines.append(line)
            
            sql_query = '\n'.join(sql_lines).strip()
            python_code = '\n'.join(python_lines).strip() if python_lines else None
            
            if not sql_query:
                return jsonify({
                    'success': False,
                    'error': 'SQL query cannot be empty'
                }), 400
            
            # Execute SQL with optional Python code
            success, result = execute_sql_with_python(sql_query, python_code)
            
            if not success:
                return jsonify({
                    'success': False,
                    'error': result  # result contains error message
                }), 400
            
            # result is now a dict with query_result, python_output, and python_data
            query_result = result.get('query_result', [])
            python_output = result.get('python_output')
            python_data = result.get('python_data', [])
            
            return jsonify({
                'success': True,
                'data': query_result if query_result else [],
                'python_output': python_output,
                'python_data': python_data,
                'row_count': result.get('row_count', 0)
            })
        else:
            # Execute ORM query (default)
            success, result = execute_orm_query(code)
            
            if not success:
                return jsonify({
                    'success': False,
                    'error': result  # result contains error message
                }), 400
            
            # result is now a dict with query_result, python_output, and has_result
            query_result = result.get('query_result', [])
            python_output = result.get('python_output')
            python_data = result.get('python_data', [])  # Parsed data from print statements
            
            return jsonify({
                'success': True,
                'data': query_result if query_result else [],
                'python_output': python_output,
                'python_data': python_data,  # Add parsed data for table view
                'row_count': len(query_result) if isinstance(query_result, list) else (1 if query_result else 0)
            })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/tables', methods=['GET'])
@login_required
def get_tables():
    """Get list of all tables and available models"""
    try:
        # Get all tables from database
        from models import get_all_tables, Base
        import models
        
        # Get database tables
        db_tables = get_all_tables()
        
        # Get available ORM models (sorted alphabetically)
        available_models = []
        for name in dir(models):
            obj = getattr(models, name)
            if isinstance(obj, type) and issubclass(obj, Base) and obj != Base:
                available_models.append(name)
        
        # Sort models alphabetically
        available_models.sort()
        
        # Get model table names to identify which tables have models
        model_table_names = set()
        for model_name in available_models:
            try:
                model_class = getattr(models, model_name)
                if hasattr(model_class, '__tablename__'):
                    model_table_names.add(model_class.__tablename__)
            except Exception:
                pass
        
        # Separate tables into those with models and those without
        tables_with_models = [t for t in db_tables if t in model_table_names]
        tables_without_models = [t for t in db_tables if t not in model_table_names]
        
        # Also add table names for dynamic querying
        # Format: table_name -> can be queried as get_table('table_name')
        return jsonify({
            'success': True,
            'tables': sorted(db_tables),  # All tables sorted
            'models': available_models,  # All models sorted
            'tables_with_models': sorted(tables_with_models),
            'tables_without_models': sorted(tables_without_models)
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/docs', methods=['GET'])
@login_required
def docs():
    """Serve the documentation page"""
    return render_template('docs.html')


@app.route('/api/table-info/<table_name>', methods=['GET'])
@login_required
def get_table_info(table_name):
    """Get structure information for a specific table"""
    try:
        db = DatabaseHelper()
        if db.connect():
            columns = db.get_table_info(table_name)
            db.disconnect()
            
            # Convert to JSON-serializable format
            json_columns = json.dumps(columns, indent=2, default=json_serializer, ensure_ascii=False)
            
            return jsonify({
                'success': True,
                'columns': json.loads(json_columns)
            })
        else:
            return jsonify({
                'success': False,
                'error': 'Failed to connect to database'
            }), 500
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


if __name__ == '__main__':
    print("\n" + "="*50)
    print("Python ORM Query Web Interface")
    print("="*50)
    print("Starting server...")
    print("Open your browser and go to: http://127.0.0.1:5000")
    print("Press Ctrl+C to stop the server")
    print("="*50 + "\n")
    app.run(debug=True, host='0.0.0.0', port=5000)

