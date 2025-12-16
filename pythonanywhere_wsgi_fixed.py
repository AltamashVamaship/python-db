# PythonAnywhere WSGI Configuration - FIXED VERSION
# Copy this ENTIRE content to: /var/www/rahulpythondb_pythonanywhere_com_wsgi.py

import sys
import os

# Add your project directory to the path
path = '/home/rahulpythondb/python-db'  # Change 'rahulpythondb' to YOUR username
if path not in sys.path:
    sys.path.insert(0, path)

# Change to your project directory
os.chdir(path)

# Activate virtualenv (IMPORTANT!)
activate_this = '/home/rahulpythondb/python-db/venv/bin/activate_this.py'
if os.path.exists(activate_this):
    with open(activate_this) as f:
        exec(f.read(), {'__file__': activate_this})

# Import the Flask app
from app import app as application

# This is what PythonAnywhere will use to serve your app
if __name__ == "__main__":
    application.run()

