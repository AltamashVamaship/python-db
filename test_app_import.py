#!/usr/bin/env python3
"""
Quick test to verify app imports correctly
Run: python3 test_app_import.py
"""
import sys
import os

# Add project path
path = '/home/rahulpythondb/python-db'
if path not in sys.path:
    sys.path.insert(0, path)

os.chdir(path)

try:
    from app import app
    print('✅ App imported successfully!')
    print(f'App name: {app.name}')
    print(f'\nRoutes found:')
    for rule in list(app.url_map.iter_rules())[:10]:
        print(f'  - {rule}')
    print('\n✅ Everything looks good!')
except Exception as e:
    print(f'❌ Error importing app: {e}')
    import traceback
    traceback.print_exc()

