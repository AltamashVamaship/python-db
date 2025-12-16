# PythonAnywhere WSGI Configuration Template
# 
# INSTRUCTIONS:
# 1. Go to Web tab in PythonAnywhere dashboard
# 2. Click on the WSGI configuration file link
# 3. Replace ALL content with this file (update the path with YOUR username)
# 4. Save and reload your web app

import sys
import os

# IMPORTANT: Change 'rahulpythondb' to YOUR PythonAnywhere username
# Your project should be at: /home/YOURUSERNAME/python-db
path = '/home/rahulpythondb/python-db'
if path not in sys.path:
    sys.path.insert(0, path)

# Change to your project directory
os.chdir(path)

# Import the Flask app
from app import app as application

# This is what PythonAnywhere will use to serve your app
if __name__ == "__main__":
    application.run()

