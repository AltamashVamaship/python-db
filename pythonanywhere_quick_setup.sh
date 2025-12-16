#!/bin/bash
# Quick setup script for PythonAnywhere
# Run this in a PythonAnywhere Bash console

echo "🚀 PythonAnywhere Setup Script"
echo "================================"
echo ""

# Get current directory
CURRENT_DIR=$(pwd)
echo "Current directory: $CURRENT_DIR"
echo ""

# Check if we're in the right directory
if [ ! -f "app.py" ]; then
    echo "❌ Error: app.py not found in current directory"
    echo "Please cd to your project directory first"
    exit 1
fi

echo "✅ Found app.py"
echo ""

# Create virtual environment
echo "📦 Creating virtual environment..."
python3.10 -m venv venv

# Activate and install dependencies
echo "📥 Installing dependencies..."
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

echo ""
echo "✅ Setup complete!"
echo ""
echo "Next steps:"
echo "1. Create .env file with your database credentials"
echo "2. Go to Web tab in PythonAnywhere dashboard"
echo "3. Configure WSGI file (see PYTHONANYWHERE_SETUP.md)"
echo "4. Add environment variables in Web tab"
echo "5. Click Reload button"
echo ""

