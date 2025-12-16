# Database Connection Fix for PythonAnywhere

## The Problem
Error: `Can't connect to MySQL server on '34.93.204.50:3306' (111)`

This means PythonAnywhere cannot reach your MySQL database server. This is usually because:
1. The MySQL server doesn't allow connections from PythonAnywhere's IP addresses
2. Environment variables are not set correctly
3. The `.env` file is missing or incorrect

## Solution Steps

### Step 1: Check .env File on PythonAnywhere

1. Go to **Files** tab
2. Navigate to `/home/rahulpythondb/python-db/`
3. Check if `.env` file exists
4. If it exists, click to edit it
5. Make sure it contains:
   ```
   DB_HOST=34.93.204.50
   DB_PORT=3306
   DB_USER=rahul
   DB_PASSWORD=Das4wrin@
   DB_NAME=ecom3
   ```

### Step 2: Set Environment Variables in Web Tab

**IMPORTANT:** PythonAnywhere sometimes doesn't read `.env` files reliably. Set environment variables directly:

1. Go to **Web** tab
2. Scroll down to **"Environment variables"** section
3. Add these variables (one by one):
   - `DB_HOST` = `34.93.204.50`
   - `DB_PORT` = `3306`
   - `DB_USER` = `rahul`
   - `DB_PASSWORD` = `Das4wrin@`
   - `DB_NAME` = `ecom3`
4. Click **"Reload"** button

### Step 3: Test Database Connection

In a **Bash console**, test the connection:
```bash
cd ~/python-db
source venv/bin/activate
python3 -c "
from db_helper import DatabaseHelper
db = DatabaseHelper()
if db.connect():
    print('✅ Database connection successful!')
    db.disconnect()
else:
    print('❌ Database connection failed')
"
```

### Step 4: Check MySQL Server Firewall

The error `(111)` usually means the connection was refused. This could mean:

1. **MySQL server firewall**: Your MySQL server at `34.93.204.50` might be blocking connections from PythonAnywhere's IP addresses.

2. **Solution**: You need to allow connections from PythonAnywhere. However, PythonAnywhere uses dynamic IP addresses, so this is tricky.

3. **Alternative**: If your MySQL server is on Google Cloud (based on the IP), you might need to:
   - Add PythonAnywhere's IP ranges to the allowed list
   - Or use a VPN/tunnel
   - Or allow connections from `0.0.0.0/0` (less secure, but works)

### Step 5: Check if Database Allows External Connections

Your MySQL server might only allow local connections. You need to:
1. Check MySQL server configuration (`bind-address` in `my.cnf`)
2. Make sure it's set to `0.0.0.0` or the server's public IP
3. Restart MySQL service

## Quick Test Script

Create a test file to check connection:

```python
# test_db_connection.py
from db_helper import DatabaseHelper
import os
from dotenv import load_dotenv

load_dotenv()

print("Environment variables:")
print(f"DB_HOST: {os.getenv('DB_HOST')}")
print(f"DB_PORT: {os.getenv('DB_PORT')}")
print(f"DB_USER: {os.getenv('DB_USER')}")
print(f"DB_NAME: {os.getenv('DB_NAME')}")
print(f"DB_PASSWORD: {'*' * len(os.getenv('DB_PASSWORD', ''))}")

db = DatabaseHelper()
if db.connect():
    print("\n✅ Connection successful!")
    db.disconnect()
else:
    print("\n❌ Connection failed")
```

Run it:
```bash
cd ~/python-db
source venv/bin/activate
python3 test_db_connection.py
```

## Most Likely Issue

The MySQL server at `34.93.204.50` is probably:
1. **Blocking external connections** - Only allows localhost
2. **Firewall blocking PythonAnywhere IPs** - Need to whitelist PythonAnywhere

## If You Can't Change MySQL Server Settings

If you cannot modify the MySQL server to allow external connections, you have these options:

1. **Use a different hosting provider** that allows database connections (Railway, Render, Heroku)
2. **Set up a database proxy/tunnel**
3. **Use a cloud database service** that allows external connections (AWS RDS, Google Cloud SQL with public IP)

## Next Steps

1. ✅ Set environment variables in Web tab
2. ✅ Test connection in Bash console
3. ✅ Check MySQL server firewall/security settings
4. ✅ Verify database credentials are correct

