# PythonAnywhere WSGI Configuration - FORCE LOAD YOUR APP
# This version will FORCE load your app and show errors if it fails
# Copy this ENTIRE content to: /var/www/rahulpythondb_pythonanywhere_com_wsgi.py

import sys
import os

# CRITICAL: Add your project directory FIRST
project_path = '/home/rahulpythondb/python-db'
sys.path.insert(0, project_path)  # Insert at beginning, not append

# Change to your project directory
os.chdir(project_path)

# Activate virtualenv BEFORE importing
venv_path = '/home/rahulpythondb/python-db/venv'
activate_this = os.path.join(venv_path, 'bin', 'activate_this.py')
if os.path.exists(activate_this):
    exec(open(activate_this).read(), {'__file__': activate_this})

# Now import - this MUST be your app, not a default one
try:
    # Delete any existing app module from cache to force reload
    if 'app' in sys.modules:
        del sys.modules['app']
    
    # Import your app
    from app import app as my_app
    
    # Verify it's YOUR app by checking routes
    routes = [str(rule) for rule in my_app.url_map.iter_rules()]
    if len(routes) <= 2:  # Only static and one route = wrong app
        raise ImportError(f"Wrong app loaded! Only found {len(routes)} routes: {routes}")
    
    # This is YOUR app
    application = my_app
    
    # Log success
    import logging
    logging.basicConfig(level=logging.INFO)
    logging.info("="*60)
    logging.info("SUCCESS: Your app loaded correctly!")
    logging.info(f"Routes found: {len(routes)}")
    logging.info(f"Sample routes: {routes[:5]}")
    logging.info("="*60)
    
except Exception as e:
    # If import fails, create error app that shows the problem
    from flask import Flask
    error_app = Flask(__name__)
    
    import traceback
    error_msg = str(e)
    error_trace = traceback.format_exc()
    
    @error_app.route('/')
    def error():
        return f"""
        <h1 style="color: red;">WSGI Import Error</h1>
        <h2>Your app failed to load</h2>
        <p><strong>Error:</strong> {error_msg}</p>
        <h3>Full Traceback:</h3>
        <pre style="background: #f0f0f0; padding: 10px; overflow: auto;">{error_trace}</pre>
        <h3>Debugging Steps:</h3>
        <ol>
            <li>Check that all files are in: {project_path}</li>
            <li>Verify virtualenv exists: {venv_path}</li>
            <li>Run in Bash: <code>cd ~/python-db && source venv/bin/activate && python3 -c "from app import app; print('OK')"</code></li>
            <li>Check error log for more details</li>
        </ol>
        """, 500
    
    application = error_app
    
    # Also log the error
    import logging
    logging.basicConfig(level=logging.ERROR)
    logging.error("="*60)
    logging.error("FAILED to load your app!")
    logging.error(f"Error: {error_msg}")
    logging.error(f"Traceback: {error_trace}")
    logging.error("="*60)

