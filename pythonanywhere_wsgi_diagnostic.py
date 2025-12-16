# PythonAnywhere WSGI Configuration - DIAGNOSTIC VERSION
# This will show us exactly what's being imported
# Copy this ENTIRE content to: /var/www/rahulpythondb_pythonanywhere_com_wsgi.py

import sys
import os

# Add your project directory FIRST
project_path = '/home/rahulpythondb/python-db'
sys.path.insert(0, project_path)

# Change to your project directory
os.chdir(project_path)

# Activate virtualenv
venv_path = '/home/rahulpythondb/python-db/venv'
activate_this = os.path.join(venv_path, 'bin', 'activate_this.py')
if os.path.exists(activate_this):
    exec(open(activate_this).read(), {'__file__': activate_this})

# Clear any cached modules
modules_to_clear = [m for m in sys.modules.keys() if m.startswith('app')]
for m in modules_to_clear:
    del sys.modules[m]

# Now import and show diagnostic info
from flask import Flask

# Check what files exist
app_py_path = os.path.join(project_path, 'app.py')
app_exists = os.path.exists(app_py_path)

# Create diagnostic app
diagnostic_app = Flask(__name__)

@diagnostic_app.route('/')
def diagnostic():
    import importlib.util
    
    info = []
    info.append(f"<h1>WSGI Diagnostic Information</h1>")
    info.append(f"<h2>File System Check:</h2>")
    info.append(f"<p>Project path: {project_path}</p>")
    info.append(f"<p>app.py exists: {app_exists}</p>")
    if app_exists:
        info.append(f"<p>app.py size: {os.path.getsize(app_py_path)} bytes</p>")
        info.append(f"<p>app.py modified: {os.path.getmtime(app_py_path)}</p>")
    
    info.append(f"<h2>Python Path:</h2>")
    info.append(f"<p>sys.path[0]: {sys.path[0]}</p>")
    info.append(f"<p>Current directory: {os.getcwd()}</p>")
    
    info.append(f"<h2>Module Check:</h2>")
    info.append(f"<p>'app' in sys.modules: {'app' in sys.modules}</p>")
    
    # Try to import the actual app
    info.append(f"<h2>Import Test:</h2>")
    try:
        # Force reload
        if 'app' in sys.modules:
            del sys.modules['app']
        
        # Import using importlib to see what happens
        spec = importlib.util.spec_from_file_location("app", app_py_path)
        if spec and spec.loader:
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            
            if hasattr(module, 'app'):
                imported_app = module.app
                routes = [str(rule) for rule in imported_app.url_map.iter_rules()]
                info.append(f"<p style='color: green;'>✅ Successfully imported your app!</p>")
                info.append(f"<p>Routes found: {len(routes)}</p>")
                info.append(f"<p>Routes: {routes}</p>")
                info.append(f"<p>App name: {imported_app.name}</p>")
                info.append(f"<p>Secret key set: {'Yes' if imported_app.secret_key else 'No'}</p>")
                
                # Use the real app
                global application
                application = imported_app
                info.append(f"<p style='color: green; font-weight: bold;'>✅ Using your app now! Reload the page.</p>")
            else:
                info.append(f"<p style='color: red;'>❌ app.py exists but has no 'app' variable</p>")
        else:
            info.append(f"<p style='color: red;'>❌ Could not create spec from app.py</p>")
    except Exception as e:
        import traceback
        info.append(f"<p style='color: red;'>❌ Import error: {str(e)}</p>")
        info.append(f"<pre>{traceback.format_exc()}</pre>")
    
    # Check for other app files
    info.append(f"<h2>Other Files:</h2>")
    if os.path.exists(project_path):
        files = os.listdir(project_path)
        py_files = [f for f in files if f.endswith('.py')]
        info.append(f"<p>Python files in project: {', '.join(py_files[:10])}</p>")
    
    return '<br>'.join(info)

# Default to diagnostic app for now
application = diagnostic_app

