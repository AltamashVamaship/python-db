#!/bin/bash

# Setup script for Python Database Query Tool

echo "Setting up Python Database Query Tool..."
echo ""

# Check if venv already exists and is valid
if [ -d "venv" ] && [ -f "venv/bin/activate" ]; then
    echo "Virtual environment already exists."
elif [ -d "venv" ]; then
    echo "Found incomplete virtual environment. Removing and recreating..."
    rm -rf venv
    echo "Creating virtual environment..."
    python3 -m venv venv
    
    if [ $? -ne 0 ]; then
        echo ""
        echo "ERROR: Failed to create virtual environment."
        echo "Please install python3-venv first:"
        echo "  sudo apt install python3-venv"
        exit 1
    fi
    echo "Virtual environment created successfully!"
else
    echo "Creating virtual environment..."
    python3 -m venv venv
    
    if [ $? -ne 0 ]; then
        echo ""
        echo "ERROR: Failed to create virtual environment."
        echo "Please install python3-venv first:"
        echo "  sudo apt install python3-venv"
        exit 1
    fi
    echo "Virtual environment created successfully!"
fi

echo ""
echo "Activating virtual environment and installing dependencies..."
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Setup complete!"
    echo ""
    echo "To use the database helper:"
    echo "  1. Activate the virtual environment: source venv/bin/activate"
    echo "  2. Run your Python scripts: python example.py"
    echo ""
    echo "Or use the run.sh script to automatically activate and run scripts."
else
    echo ""
    echo "❌ Installation failed. Please check the error messages above."
    exit 1
fi

