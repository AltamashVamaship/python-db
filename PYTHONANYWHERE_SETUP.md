# PythonAnywhere Deployment Guide

## Step-by-Step Instructions

### 1. Upload Your Files

#### Option A: Using Git (Recommended)
```bash
# In PythonAnywhere Bash console
cd ~
git clone https://github.com/your-username/your-repo.git python-db
cd python-db
```

#### Option B: Using Files Tab
1. Go to **Files** tab in PythonAnywhere
2. Navigate to `/home/rahulpythondb/` (your username)
3. Create folder `python-db`
4. Upload all your project files:
   - `app.py`
   - `config.py`
   - `models.py`
   - `orm_executor.py`
   - `sql_executor.py`
   - `db_helper.py`
   - `requirements.txt`
   - `templates/` folder (with all HTML files)
   - `.env` file (create it with your database credentials)

### 2. Set Up Virtual Environment

In a **Bash console**:
```bash
cd ~/python-db
python3.10 -m venv venv  # PythonAnywhere uses Python 3.10
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

### 3. Create .env File

In the **Files** tab, create `/home/rahulpythondb/python-db/.env`:
```
DB_HOST=34.93.204.50
DB_PORT=3306
DB_USER=rahul
DB_PASSWORD=Das4wrin@
DB_NAME=ecom3
SECRET_KEY=your-generated-secret-key-here
```

Generate secret key:
```bash
python3 -c "import secrets; print(secrets.token_hex(32))"
```

### 4. Configure Web App

1. Go to **Web** tab in PythonAnywhere dashboard
2. Click **"Add a new web app"** (if you don't have one)
3. Choose **Flask**
4. Select **Python 3.10**
5. Enter path: `/home/rahulpythondb/python-db/app.py`
6. Click **Next** → **Next**

### 5. Configure WSGI File

1. In the **Web** tab, click on the WSGI configuration file link
2. It will open: `/var/www/rahulpythondb_pythonanywhere_com_wsgi.py`
3. Replace the entire content with:

```python
import sys
import os

# Add your project directory to the path
path = '/home/rahulpythondb/python-db'  # Change to your username
if path not in sys.path:
    sys.path.insert(0, path)

# Change to your project directory
os.chdir(path)

# Import the Flask app
from app import app as application

if __name__ == "__main__":
    application.run()
```

**Important:** Replace `rahulpythondb` with your actual PythonAnywhere username!

### 6. Configure Static Files (Optional but Recommended)

In the **Web** tab, under **Static files**:
- **URL**: `/static/`
- **Directory**: `/home/rahulpythondb/python-db/static/`

(If you don't have a static folder, you can skip this)

### 7. Set Environment Variables

In the **Web** tab, scroll down to **Environment variables**:
- Add: `DB_HOST` = `34.93.204.50`
- Add: `DB_PORT` = `3306`
- Add: `DB_USER` = `rahul`
- Add: `DB_PASSWORD` = `Das4wrin@`
- Add: `DB_NAME` = `ecom3`
- Add: `SECRET_KEY` = `your-generated-secret-key`

### 8. Reload Web App

1. Click the green **"Reload"** button in the Web tab
2. Your app should now be live at: `https://rahulpythondb.pythonanywhere.com`

## Troubleshooting

### Check Logs
- **Error log**: Click "Error log" link in Web tab
- **Server log**: Click "Server log" link in Web tab

### Common Issues

1. **Import errors**: Make sure all files are in `/home/yourusername/python-db/`
2. **Database connection**: Check if your database allows connections from PythonAnywhere IPs
3. **Module not found**: Run `pip install -r requirements.txt` in your virtual environment
4. **Path issues**: Make sure the path in WSGI file matches your actual directory

### Test Locally First
```bash
# In Bash console
cd ~/python-db
source venv/bin/activate
python app.py
```

## Security Notes

- Never commit `.env` file to Git
- Use strong `SECRET_KEY` in production
- PythonAnywhere free accounts have limited CPU time (100 seconds/day)
- Consider upgrading for production use

## Updating Your App

1. Make changes to your files
2. Click **"Reload"** button in Web tab
3. Changes take effect immediately

## Custom Domain (Paid Accounts)

1. Go to **Web** tab
2. Click **"Add a new domain"**
3. Enter your domain
4. Update DNS records as instructed

