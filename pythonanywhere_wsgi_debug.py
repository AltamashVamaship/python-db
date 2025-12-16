# PythonAnywhere WSGI Configuration - WITH ERROR HANDLING
# This version will show errors in the error log if something goes wrong
# Copy this ENTIRE content to: /var/www/rahulpythondb_pythonanywhere_com_wsgi.py

import sys
import os

# Add your project directory to the path
project_path = '/home/rahulpythondb/python-db'  # Make sure this matches YOUR username
if project_path not in sys.path:
    sys.path.insert(0, project_path)

# Change to your project directory
os.chdir(project_path)

# Activate virtualenv if it exists
venv_path = '/home/rahulpythondb/python-db/venv'  # Make sure this matches YOUR username
activate_this = os.path.join(venv_path, 'bin', 'activate_this.py')
if os.path.exists(activate_this):
    try:
        exec(open(activate_this).read(), {'__file__': activate_this})
    except Exception as e:
        # Log error but continue
        import logging
        logging.error(f"Failed to activate virtualenv: {e}")

# Now import your Flask app with error handling
try:
    from app import app
    application = app
except ImportError as e:
    # If import fails, create a simple error app
    from flask import Flask
    error_app = Flask(__name__)
    
    @error_app.route('/')
    def error():
        return f"""
        <h1>WSGI Configuration Error</h1>
        <p>Failed to import your Flask app.</p>
        <p>Error: {str(e)}</p>
        <p>Please check:</p>
        <ul>
            <li>All files are uploaded to {project_path}</li>
            <li>Virtualenv path is correct: {venv_path}</li>
            <li>Dependencies are installed: pip install -r requirements.txt</li>
            <li>Check error log for more details</li>
        </ul>
        <p>Run this in Bash console to test: python3 test_import.py</p>
        """, 500
    
    application = error_app
except Exception as e:
    # Any other error
    from flask import Flask
    error_app = Flask(__name__)
    
    @error_app.route('/')
    def error():
        import traceback
        return f"""
        <h1>WSGI Configuration Error</h1>
        <p>Unexpected error loading your Flask app.</p>
        <pre>{str(e)}</pre>
        <pre>{traceback.format_exc()}</pre>
        """, 500
    
    application = error_app

