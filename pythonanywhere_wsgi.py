# This file is for PythonAnywhere deployment
# Upload this file to: /var/www/yourusername_pythonanywhere_com_wsgi.py
# Or configure it in the Web tab of PythonAnywhere dashboard

import sys
import os

# Add your project directory to the path
path = '/home/rahulpythondb/python-db'  # Change 'rahulpythondb' to your PythonAnywhere username
if path not in sys.path:
    sys.path.insert(0, path)

# Change to your project directory
os.chdir(path)

# Import the Flask app
from app import app as application

# Optional: Set any environment variables here if needed
# os.environ['DB_HOST'] = 'your-host'
# os.environ['DB_USER'] = 'your-user'
# etc.

if __name__ == "__main__":
    application.run()

