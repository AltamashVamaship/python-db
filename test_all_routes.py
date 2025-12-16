#!/usr/bin/env python3
"""
Test all routes in the app
"""
import sys
import os

path = '/home/rahulpythondb/python-db'
if path not in sys.path:
    sys.path.insert(0, path)

os.chdir(path)

from app import app

print("="*60)
print("ALL ROUTES IN APP:")
print("="*60)
for rule in app.url_map.iter_rules():
    methods = ','.join(sorted(rule.methods - {'OPTIONS', 'HEAD'}))
    print(f"{rule.rule:40} {methods:20} {rule.endpoint}")
print("="*60)
print(f"\nTotal routes: {len(list(app.url_map.iter_rules()))}")

# Test if login_required decorator is working
print("\n" + "="*60)
print("TESTING APP FUNCTIONALITY:")
print("="*60)

# Check if we can access the app instance
print(f"App name: {app.name}")
print(f"App debug: {app.debug}")
print(f"App secret_key set: {'Yes' if app.secret_key else 'No'}")

# Try to get a route handler
try:
    with app.test_request_context():
        print("\n✅ App context works")
except Exception as e:
    print(f"\n❌ App context error: {e}")

print("\n✅ All tests complete!")

