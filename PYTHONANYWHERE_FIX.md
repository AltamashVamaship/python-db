# PythonAnywhere Fix Guide - Site Not Working

## Quick Fix Checklist

### ✅ Step 1: Check Error Logs
1. Go to **Web** tab
2. Click **"Error log"** link
3. Look for any import errors or missing modules
4. Copy any errors you see

### ✅ Step 2: Set Virtualenv Path
**CRITICAL:** This is often the main issue!

1. In **Web** tab, scroll to **"Virtualenv"** section
2. Enter: `/home/rahulpythondb/python-db/venv`
3. Click **"Reload"** button

### ✅ Step 3: Update WSGI File
1. In **Web** tab, click **"WSGI configuration file"** link
2. Replace ALL content with this:

```python
import sys
import os

# Add your project directory to the path
path = '/home/rahulpythondb/python-db'
if path not in sys.path:
    sys.path.insert(0, path)

# Change to your project directory
os.chdir(path)

# Activate virtualenv (if using one)
activate_this = '/home/rahulpythondb/python-db/venv/bin/activate_this.py'
if os.path.exists(activate_this):
    with open(activate_this) as f:
        exec(f.read(), {'__file__': activate_this})

# Import the Flask app
from app import app as application

if __name__ == "__main__":
    application.run()
```

3. **Save** the file
4. Click **"Reload"** button

### ✅ Step 4: Verify Files Are Uploaded
In **Files** tab, check that these files exist in `/home/rahulpythondb/python-db/`:
- ✅ `app.py`
- ✅ `config.py`
- ✅ `models.py`
- ✅ `orm_executor.py`
- ✅ `sql_executor.py`
- ✅ `db_helper.py`
- ✅ `requirements.txt`
- ✅ `templates/` folder (with `index.html`, `login.html`, `docs.html`)
- ✅ `.env` file (create if missing)

### ✅ Step 5: Install Dependencies
In a **Bash console**:
```bash
cd ~/python-db
source venv/bin/activate
pip install -r requirements.txt
```

### ✅ Step 6: Check Environment Variables
In **Web** tab, under **"Environment variables"**, add:
- `DB_HOST` = `34.93.204.50`
- `DB_PORT` = `3306`
- `DB_USER` = `rahul`
- `DB_PASSWORD` = `Das4wrin@`
- `DB_NAME` = `ecom3`
- `SECRET_KEY` = `7f642e79e86cc408e07a801e0dfd8b8f7dd22d65a88f4b280b1cef4da87e73c7`

### ✅ Step 7: Test in Console
In a **Bash console**, test if imports work:
```bash
cd ~/python-db
source venv/bin/activate
python3
>>> from app import app
>>> print("✅ Import successful!")
```

If you get errors, fix them before reloading.

## Common Errors & Solutions

### Error: "No module named 'flask'"
**Solution:** 
```bash
cd ~/python-db
source venv/bin/activate
pip install flask sqlalchemy mysql-connector-python python-dotenv
```

### Error: "No module named 'orm_executor'"
**Solution:** Check that `orm_executor.py` exists in `/home/rahulpythondb/python-db/`

### Error: "Template not found"
**Solution:** Check that `templates/` folder exists and contains `index.html`, `login.html`, `docs.html`

### Error: "Database connection failed"
**Solution:** 
1. Check `.env` file exists with correct credentials
2. Verify database allows connections from PythonAnywhere IPs
3. Test connection in Bash console:
```bash
python3 -c "from db_helper import DatabaseHelper; db = DatabaseHelper(); print('Connected!' if db.connect() else 'Failed')"
```

### Still seeing "Hello from Flask!"?
This means PythonAnywhere is using the default Flask template. Make sure:
1. ✅ Virtualenv path is set correctly
2. ✅ WSGI file imports `from app import app as application`
3. ✅ All files are in the correct directory
4. ✅ No import errors in error log

## Still Not Working?

1. **Check Error Log** - Most important step!
2. **Check Server Log** - For startup issues
3. **Test in Console** - Try importing your app manually
4. **Verify Paths** - Make sure all paths use your actual username

