#!/bin/bash
# Quick setup verification script for PythonAnywhere
# Run this in a PythonAnywhere Bash console

echo "🔍 PythonAnywhere Setup Verification"
echo "====================================="
echo ""

# Check current directory
echo "1. Current directory:"
pwd
echo ""

# Check if we're in the right place
if [ ! -f "app.py" ]; then
    echo "❌ ERROR: app.py not found in current directory"
    echo "Please run: cd ~/python-db"
    exit 1
fi

echo "✅ Found app.py"
echo ""

# Check if virtualenv exists
echo "2. Checking virtualenv:"
if [ -d "venv" ]; then
    echo "✅ Virtualenv exists"
    if [ -f "venv/bin/activate" ]; then
        echo "✅ Virtualenv activate script exists"
    else
        echo "❌ Virtualenv activate script missing"
    fi
else
    echo "❌ Virtualenv not found!"
    echo "   Run: python3.10 -m venv venv"
fi
echo ""

# Check required files
echo "3. Checking required files:"
files=("app.py" "config.py" "models.py" "orm_executor.py" "sql_executor.py" "db_helper.py" "requirements.txt")
for file in "${files[@]}"; do
    if [ -f "$file" ]; then
        echo "✅ $file"
    else
        echo "❌ $file MISSING"
    fi
done
echo ""

# Check templates folder
echo "4. Checking templates folder:"
if [ -d "templates" ]; then
    echo "✅ templates/ folder exists"
    templates=("index.html" "login.html" "docs.html")
    for template in "${templates[@]}"; do
        if [ -f "templates/$template" ]; then
            echo "✅ templates/$template"
        else
            echo "❌ templates/$template MISSING"
        fi
    done
else
    echo "❌ templates/ folder MISSING"
fi
echo ""

# Check .env file
echo "5. Checking .env file:"
if [ -f ".env" ]; then
    echo "✅ .env file exists"
else
    echo "⚠️  .env file not found (you can use environment variables in Web tab instead)"
fi
echo ""

# Test Python import
echo "6. Testing Python imports:"
if [ -d "venv" ]; then
    source venv/bin/activate
    echo "Testing import..."
    python3 -c "from app import app; print('✅ App imported successfully!')" 2>&1
    if [ $? -eq 0 ]; then
        echo "✅ All imports working!"
    else
        echo "❌ Import failed - check error above"
    fi
    deactivate
else
    echo "⚠️  Skipping import test (no virtualenv)"
fi
echo ""

echo "====================================="
echo "Verification complete!"
echo ""
echo "Next steps:"
echo "1. Fix any ❌ errors above"
echo "2. Make sure virtualenv path is set in Web tab: ~/python-db/venv"
echo "3. Update WSGI file with correct username"
echo "4. Click Reload in Web tab"

