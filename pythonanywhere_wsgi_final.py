# PythonAnywhere WSGI Configuration - FINAL WORKING VERSION
# Copy this ENTIRE content to: /var/www/rahulpythondb_pythonanywhere_com_wsgi.py
# 
# IMPORTANT: After pasting, make sure to:
# 1. Replace 'rahulpythondb' with YOUR actual username in the paths
# 2. Save the file
# 3. Click "Reload" button in Web tab

import sys
import os

# Add your project directory to the path
project_path = '/home/rahulpythondb/python-db'  # CHANGE THIS to your username
if project_path not in sys.path:
    sys.path.insert(0, project_path)

# Change to your project directory
os.chdir(project_path)

# Activate virtualenv if it exists
venv_path = '/home/rahulpythondb/python-db/venv'  # CHANGE THIS to your username
activate_this = os.path.join(venv_path, 'bin', 'activate_this.py')
if os.path.exists(activate_this):
    exec(open(activate_this).read(), {'__file__': activate_this})

# Now import your Flask app
# This MUST be after setting the path and activating venv
from app import app

# PythonAnywhere expects 'application' variable
application = app

# Debug: Uncomment these lines to see what's being loaded (check error log)
# import logging
# logging.basicConfig(level=logging.DEBUG)
# logging.debug(f"Loaded app: {application}")
# logging.debug(f"App routes: {[str(rule) for rule in application.url_map.iter_rules()]}")

