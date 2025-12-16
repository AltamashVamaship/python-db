# PythonAnywhere WSGI Configuration - WORKING VERSION
# This is the final version that should work
# Copy this to: /var/www/rahulpythondb_pythonanywhere_com_wsgi.py

import sys
import os

# Add your project directory to the path
project_path = '/home/rahulpythondb/python-db'
if project_path not in sys.path:
    sys.path.insert(0, project_path)

# Change to your project directory
os.chdir(project_path)

# Activate virtualenv
venv_path = '/home/rahulpythondb/python-db/venv'
activate_this = os.path.join(venv_path, 'bin', 'activate_this.py')
if os.path.exists(activate_this):
    exec(open(activate_this).read(), {'__file__': activate_this})

# Import your Flask app
from app import app

# PythonAnywhere expects 'application' variable
application = app

# Enable logging to see what's happening (check error log)
import logging
logging.basicConfig(level=logging.INFO)
logging.info(f"WSGI loaded app: {application}")
logging.info(f"App routes: {[str(rule) for rule in application.url_map.iter_rules()]}")

