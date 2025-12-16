#!/usr/bin/env python3
"""
Test script to verify imports work correctly
Run this in PythonAnywhere Bash console: python3 test_import.py
"""
import sys
import os

# Add project path
path = '/home/rahulpythondb/python-db'
if path not in sys.path:
    sys.path.insert(0, path)

os.chdir(path)

print("Testing imports...")
print(f"Current directory: {os.getcwd()}")
print(f"Python path: {sys.path[:3]}")

try:
    print("\n1. Testing config import...")
    from config import DB_CONFIG
    print(f"   ✅ Config loaded: {DB_CONFIG['host']}")
except Exception as e:
    print(f"   ❌ Config error: {e}")

try:
    print("\n2. Testing db_helper import...")
    from db_helper import DatabaseHelper
    print("   ✅ db_helper imported")
except Exception as e:
    print(f"   ❌ db_helper error: {e}")

try:
    print("\n3. Testing models import...")
    from models import Base, get_table
    print("   ✅ models imported")
except Exception as e:
    print(f"   ❌ models error: {e}")

try:
    print("\n4. Testing orm_executor import...")
    from orm_executor import execute_orm_query
    print("   ✅ orm_executor imported")
except Exception as e:
    print(f"   ❌ orm_executor error: {e}")

try:
    print("\n5. Testing sql_executor import...")
    from sql_executor import execute_sql_with_python
    print("   ✅ sql_executor imported")
except Exception as e:
    print(f"   ❌ sql_executor error: {e}")

try:
    print("\n6. Testing Flask app import...")
    from app import app
    print(f"   ✅ Flask app imported: {app}")
    print(f"   ✅ App name: {app.name}")
    print(f"   ✅ Routes: {[str(rule) for rule in app.url_map.iter_rules()][:5]}")
except Exception as e:
    print(f"   ❌ Flask app error: {e}")
    import traceback
    traceback.print_exc()

print("\n" + "="*50)
print("Import test complete!")

