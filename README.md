# Python ORM Query Web Interface

A beautiful web-based interface for running Python ORM (SQLAlchemy) and SQL queries against your MySQL database. Execute queries, view results in JSON format, and manipulate data with Python code - all from your browser.

## 🚀 Features

- ✨ **Modern Web Interface** - Clean, responsive UI with full-width layout
- 🐍 **Python ORM Queries** - Write SQLAlchemy ORM-style queries using generated models
- 📊 **SQL Queries** - Execute raw SQL queries and manipulate results with Python
- 📋 **Auto-generated Models** - 199+ SQLAlchemy models for all database tables
- 🔒 **Authentication** - Email/password protected access
- 📖 **Documentation Page** - Comprehensive ORM query examples (basic to advanced)
- 🎨 **Multiple Views** - Switch between text and table views for results
- ⌨️ **Keyboard Shortcuts** - Ctrl+Enter to execute queries
- 🔐 **Safe Execution** - Sandboxed environment for secure code execution

## 📋 Prerequisites

Before you begin, ensure you have:

- **Python 3.8+** installed
- **MySQL database** access (host, port, username, password, database name)
- **pip** (Python package manager)
- **Git** (to clone the repository)

For Ubuntu/Debian systems, you may need:
```bash
sudo apt install python3-venv python3-pip
```

## 🔧 Step-by-Step Setup Guide

### Step 1: Clone the Repository

```bash
git clone <repository-url>
cd python-db
```

### Step 2: Configure Database Credentials

Edit `config.py` and update the database connection details:

### Setup

**Alternatively**, create a `.env` file in the project root:

```bash
DB_HOST=your-database-host
DB_PORT=3306
DB_USER=your-username
DB_PASSWORD=your-password
DB_NAME=your-database-name
```

### Step 3: Configure Authentication (Optional)

The default login credentials are set in `app.py`. To change them, edit:

```python
VALID_EMAIL = 'your-email@example.com'
VALID_PASSWORD = 'YourPassword123!'
```

**Important:** Also change the `app.secret_key` in `app.py` for production use:

```python
app.secret_key = 'your-random-secret-key-here'
```

### Step 4: Run Setup Script

Make the setup script executable and run it:

```bash
chmod +x setup.sh
./setup.sh
```

This will:
- Create a Python virtual environment (`venv/`)
- Install all required dependencies from `requirements.txt`

**Manual Setup** (if the script doesn't work):

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt
```

### Step 5: Generate ORM Models (First Time Only)

If you need to regenerate models for your database tables:

```bash
source venv/bin/activate
python generate_models.py
```

This will create/update `models.py` with SQLAlchemy models for all tables that have primary keys.

### Step 6: Start the Web Server

Make the start script executable and run it:

```bash
chmod +x start_web.sh
./start_web.sh
```

**Manual Start**:

```bash
source venv/bin/activate
python app.py
```

### Step 7: Access the Web Interface

Open your browser and navigate to:

**http://127.0.0.1:5000**

You'll be prompted to login with:
- **Email:** `rahul.sharma@vamaship.com` (or your configured email)
- **Password:** `Vama@1234#` (or your configured password)

## 📖 Usage Guide

### Python ORM Queries

1. Click the **"🐍 Python ORM"** button to switch to ORM mode
2. Write your query in the text area:
   ```python
   session.query(Entities).limit(10).all()
   ```
3. Click **"Run Query"** or press **Ctrl+Enter**
4. View results in JSON format (alphabetically sorted keys)
5. Toggle between **Text View** and **Table View** for results

**Example ORM Queries:**

```python
# Get all records (limit 10)
session.query(Entities).limit(10).all()

# Filter results
session.query(Entities).filter(Entities.id > 100).limit(10).all()

# Select specific columns
session.query(Entities.id, Entities.entity_name).limit(20).all()

# Order by
from sqlalchemy import desc
session.query(Entities).order_by(desc(Entities.created_at)).limit(10).all()

# Count records
from sqlalchemy import func
session.query(func.count(Entities.id)).scalar()

# Query results are automatically stored in 'result' variable
session.query(Entities).limit(5).all()
print(result)  # Access the query results
```

### SQL Queries

1. Click the **"📊 SQL"** button to switch to SQL mode
2. Write your SQL query:
   ```sql
   SELECT * FROM entities LIMIT 10;
   ```
3. Optionally add Python code to manipulate results:
   ```sql
   SELECT * FROM entities LIMIT 10;
   
   # Python code to manipulate results
   print(len(result))
   print(result[0])
   ```
4. Click **"Run Query"** or press **Ctrl+Enter**
5. SQL results are stored in the `result` variable for Python manipulation

**Note:** Only `SELECT` queries are allowed for security.

### Browse Available Tables

Click **"Load Tables"** to see:
- **ORM Models** - Available SQLAlchemy model classes
- **SQL Tables** - All database tables (including those without primary keys)

### Documentation Page

Click **"📖 Documentation"** in the header to access:
- Basic ORM query examples
- Intermediate queries (joins, aggregations)
- Advanced queries (subqueries, complex filters)
- Side-by-side ORM and SQL comparisons

## 🗂️ Project Structure

```
python-db/
├── app.py                 # Main Flask application
├── config.py              # Database configuration
├── models.py              # Auto-generated SQLAlchemy models
├── orm_executor.py        # ORM query execution engine
├── sql_executor.py        # SQL query execution engine
├── db_helper.py           # Database connection helper
├── generate_models.py     # Script to generate ORM models
├── requirements.txt       # Python dependencies
├── setup.sh              # Setup script
├── start_web.sh          # Start server script
├── templates/
│   ├── index.html        # Main query interface
│   ├── docs.html         # Documentation page
│   └── login.html        # Login page
└── README.md             # This file
```

## 🔒 Security Features

- **Authentication Required** - All pages are protected with email/password login
- **Read-Only Queries** - SQL queries are restricted to `SELECT` statements only
- **Sandboxed Execution** - Python code runs in a restricted environment
- **Session Management** - Secure session handling with Flask sessions

## 🐛 Troubleshooting

### Issue: "Virtual environment not found"

**Solution:**
```bash
./setup.sh
```

### Issue: "Module not found" errors

**Solution:**
```bash
source venv/bin/activate
pip install -r requirements.txt
```

### Issue: "Cannot connect to database"

**Solution:**
1. Check your database credentials in `config.py` or `.env`
2. Ensure your database server is running and accessible
3. Verify network connectivity and firewall settings

### Issue: "IndentationError" or syntax errors

**Solution:**
- Ensure you're using Python 3.8+
- Check that all dependencies are installed correctly
- Try regenerating models: `python generate_models.py`

### Issue: "Login page not working"

**Solution:**
- Check that `app.secret_key` is set in `app.py`
- Clear browser cookies and try again
- Verify authentication credentials in `app.py`

### Issue: Models not found for some tables

**Solution:**
- Tables without primary keys cannot have ORM models
- Use SQL queries or `get_table()` for those tables
- Check `generate_models.py` output for warnings

## 📝 Dependencies

- **Flask 3.0.0** - Web framework
- **SQLAlchemy 2.0.23** - ORM library
- **mysql-connector-python 8.2.0** - MySQL database connector
- **python-dotenv 1.0.0** - Environment variable management

## 🎯 Quick Reference

| Action | Command |
|--------|---------|
| Setup project | `./setup.sh` |
| Start server | `./start_web.sh` |
| Activate venv | `source venv/bin/activate` |
| Generate models | `python generate_models.py` |
| Install deps | `pip install -r requirements.txt` |

## 📞 Support

For issues or questions:
1. Check the troubleshooting section above
2. Review the documentation page in the web interface
3. Check error messages in the terminal where the server is running

## 📄 License

This project is for internal use. Modify as needed for your requirements.

---

**Happy Querying! 🚀**
