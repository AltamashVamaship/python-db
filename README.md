# Python ORM Query Web Interface

Easy-to-use web interface for running Python ORM-style queries against your MySQL database.

## Quick Start

### 🌐 Web Interface

Start the web interface and run queries in your browser:

```bash
# Start the web server
./start_web.sh

# Or manually:
source venv/bin/activate
python app.py
```

Then open your browser and go to: **http://127.0.0.1:5000**

**Features:**
- ✨ Beautiful, modern web interface
- 🐍 Write Python ORM-style queries (SQLAlchemy)
- 📊 View results in pretty JSON format
- 📋 Browse available models
- 🔒 Safe execution environment (read-only)
- ⌨️ Keyboard shortcut: Ctrl+Enter to execute queries

### Setup

1. **Setup virtual environment and install dependencies:**
   ```bash
   # Make setup script executable (first time only)
   chmod +x setup.sh
   
   # Run setup
   ./setup.sh
   ```
   
   Or manually:
   ```bash
   # Install python3-venv if needed (Ubuntu/Debian)
   sudo apt install python3-venv
   
   # Create virtual environment
   python3 -m venv venv
   
   # Activate virtual environment
   source venv/bin/activate
   
   # Install dependencies
   pip install -r requirements.txt
   ```

2. **Activate virtual environment (whenever you open a new terminal):**
   ```bash
   source venv/bin/activate
   ```

3. **Start the web interface:**
   ```bash
   ./start_web.sh
   ```

## Using the Web Interface

1. **Write your Python ORM query** in the text area on the left
   - Example: `session.query(Entity).limit(10).all()`
   - Example: `session.query(Entity.id, Entity.entity_name).filter(Entity.id > 100).all()`
2. **Click "Run Query"** or press **Ctrl+Enter**
3. **View results** in formatted JSON on the right
4. **Browse models** by clicking "Load Tables" to see available ORM models
5. **Use quick examples** by clicking on the example queries below the text area

### Example ORM Queries:

```python
# Get all entities (limit 10)
session.query(Entity).limit(10).all()

# Get specific columns
session.query(Entity.id, Entity.entity_name, Entity.credit_balance).limit(20).all()

# Filter results
session.query(Entity).filter(Entity.id > 100).limit(10).all()

# Count records
session.query(func.count(Entity.id)).scalar()

# Order by
session.query(Entity).order_by(desc(Entity.created_at)).limit(10).all()

# Query NDR table
session.query(Ndr).limit(5).all()
```

## Configuration

The database credentials are set in `config.py`. You can also:

1. **Use environment variables:** Create a `.env` file (see `.env.example`)
2. **Modify config.py directly:** Credentials are already set with your values

## Features

- ✅ **Web Interface** - Beautiful browser-based query interface
- ✅ **Python ORM Queries** - Write SQLAlchemy ORM-style queries
- ✅ Pretty JSON formatted results
- ✅ Browse available models
- ✅ Quick example queries
- ✅ Keyboard shortcuts (Ctrl+Enter to execute)
- ✅ Safe execution environment (sandboxed)
- ✅ Real-time status and error messages
- ✅ Support for filtering, ordering, aggregations, and more

## Database Credentials

- Host: 34.93.204.50
- Port: 3306
- Database: ecom3
- User: rahul

