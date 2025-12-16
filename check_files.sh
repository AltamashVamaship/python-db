#!/bin/bash
# Check what files actually exist on PythonAnywhere
# Run this in Bash console: bash check_files.sh

echo "=========================================="
echo "File System Check"
echo "=========================================="
echo ""

cd ~/python-db

echo "Current directory: $(pwd)"
echo ""

echo "Python files:"
ls -la *.py 2>/dev/null | head -20
echo ""

echo "app.py details:"
if [ -f "app.py" ]; then
    echo "  ✅ app.py exists"
    echo "  Size: $(wc -l < app.py) lines"
    echo "  First 5 lines:"
    head -5 app.py
    echo ""
    echo "  Looking for 'app = Flask' pattern:"
    grep -n "app = Flask" app.py || echo "  ⚠️  'app = Flask' not found!"
else
    echo "  ❌ app.py NOT FOUND!"
fi
echo ""

echo "Templates folder:"
if [ -d "templates" ]; then
    echo "  ✅ templates/ exists"
    ls -la templates/
else
    echo "  ❌ templates/ NOT FOUND!"
fi
echo ""

echo "Checking for other app files that might conflict:"
find . -name "*.py" -type f | grep -E "(app|main|wsgi)" | head -10
echo ""

echo "Checking sys.path when importing:"
python3 -c "import sys; print('  sys.path[0]:', sys.path[0])" 2>/dev/null
echo ""

echo "=========================================="
echo "Test import:"
echo "=========================================="
python3 -c "
import sys
import os
sys.path.insert(0, os.getcwd())
try:
    from app import app
    print('✅ Import successful')
    print(f'  App name: {app.name}')
    routes = [str(r) for r in app.url_map.iter_rules()]
    print(f'  Routes: {len(routes)}')
    print(f'  Sample routes: {routes[:5]}')
except Exception as e:
    print(f'❌ Import failed: {e}')
    import traceback
    traceback.print_exc()
"

