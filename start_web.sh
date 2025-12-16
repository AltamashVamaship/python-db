#!/bin/bash

# Start the web interface for database queries

cd "$(dirname "$0")"

if [ ! -d "venv" ]; then
    echo "Virtual environment not found. Running setup..."
    bash setup.sh
fi

source venv/bin/activate

echo ""
echo "Starting web interface..."
echo "Open your browser and go to: http://127.0.0.1:5000"
echo "Press Ctrl+C to stop the server"
echo ""

python app.py

