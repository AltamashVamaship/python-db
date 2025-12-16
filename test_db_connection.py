#!/usr/bin/env python3
"""
Test database connection on PythonAnywhere
Run: python3 test_db_connection.py
"""
import os
import sys
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

print("="*60)
print("Database Connection Test")
print("="*60)
print()

# Show environment variables
print("Environment Variables:")
print(f"  DB_HOST: {os.getenv('DB_HOST', 'NOT SET')}")
print(f"  DB_PORT: {os.getenv('DB_PORT', 'NOT SET')}")
print(f"  DB_USER: {os.getenv('DB_USER', 'NOT SET')}")
print(f"  DB_NAME: {os.getenv('DB_NAME', 'NOT SET')}")
password = os.getenv('DB_PASSWORD', '')
print(f"  DB_PASSWORD: {'*' * len(password) if password else 'NOT SET'}")
print()

# Test connection
print("Testing connection...")
try:
    from db_helper import DatabaseHelper
    
    db = DatabaseHelper()
    if db.connect():
        print("✅ Database connection successful!")
        print(f"  Connected to: {db.connection.database}")
        db.disconnect()
    else:
        print("❌ Database connection failed")
        print("  Check error messages above")
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()

print()
print("="*60)

