"""
Database configuration
You can also use environment variables by creating a .env file
"""
import os
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
load_dotenv()

DB_CONFIG = {
    'host': os.getenv('DB_HOST', '34.93.204.50'),
    'port': int(os.getenv('DB_PORT', 3306)),
    'user': os.getenv('DB_USER', 'rahul'),
    'password': os.getenv('DB_PASSWORD', 'Das4wrin@'),
    'database': os.getenv('DB_NAME', 'ecom3')
}

