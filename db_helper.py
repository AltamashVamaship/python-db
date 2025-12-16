"""
Database helper module for easy MySQL queries
"""
import mysql.connector
from mysql.connector import Error
from config import DB_CONFIG


class DatabaseHelper:
    """Simple database helper class for executing queries"""
    
    def __init__(self):
        self.connection = None
        self.cursor = None
    
    def connect(self):
        """Establish database connection"""
        try:
            self.connection = mysql.connector.connect(**DB_CONFIG)
            if self.connection.is_connected():
                self.cursor = self.connection.cursor(dictionary=True)  # Returns results as dict
                print("Successfully connected to database")
                return True
        except Error as e:
            print(f"Error connecting to MySQL: {e}")
            return False
    
    def disconnect(self):
        """Close database connection"""
        if self.cursor:
            self.cursor.close()
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Database connection closed")
    
    def execute_query(self, query, params=None):
        """
        Execute a SELECT query and return results
        
        Args:
            query: SQL query string
            params: Optional tuple or dict of parameters for parameterized queries
        
        Returns:
            List of dictionaries (rows) or None if error
        """
        if not self.connection or not self.connection.is_connected():
            if not self.connect():
                return None
        
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            
            results = self.cursor.fetchall()
            return results
        except Error as e:
            print(f"Error executing query: {e}")
            return None
    
    def execute_update(self, query, params=None):
        """
        Execute INSERT, UPDATE, or DELETE query
        
        Args:
            query: SQL query string
            params: Optional tuple or dict of parameters for parameterized queries
        
        Returns:
            Number of affected rows or None if error
        """
        if not self.connection or not self.connection.is_connected():
            if not self.connect():
                return None
        
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            
            self.connection.commit()
            return self.cursor.rowcount
        except Error as e:
            print(f"Error executing update: {e}")
            self.connection.rollback()
            return None
    
    def get_table_info(self, table_name):
        """Get column information for a table"""
        query = f"DESCRIBE {table_name}"
        return self.execute_query(query)
    
    def get_tables(self):
        """Get list of all tables in the database"""
        query = "SHOW TABLES"
        result = self.execute_query(query)
        if result:
            # Extract table names from the result
            table_key = list(result[0].keys())[0] if result else None
            return [row[table_key] for row in result] if table_key else []
        return []


# Convenience function for quick queries
def run_query(query, params=None):
    """
    Quick function to run a query without managing connection
    
    Usage:
        results = run_query("SELECT * FROM entities LIMIT 10")
    """
    db = DatabaseHelper()
    try:
        if db.connect():
            return db.execute_query(query, params)
    finally:
        db.disconnect()


def run_update(query, params=None):
    """
    Quick function to run an update query without managing connection
    
    Usage:
        rows_affected = run_update("UPDATE entities SET name = %s WHERE id = %s", ("New Name", 1))
    """
    db = DatabaseHelper()
    try:
        if db.connect():
            return db.execute_update(query, params)
    finally:
        db.disconnect()


def run_query_json(query, params=None):
    """
    Run a query and return results as JSON string (pretty formatted)
    
    Usage:
        json_output = run_query_json("SELECT * FROM entities LIMIT 10")
        print(json_output)
    """
    import json
    from datetime import datetime, date
    from decimal import Decimal
    
    def json_serializer(obj):
        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        elif isinstance(obj, Decimal):
            return float(obj)
        raise TypeError(f"Type {type(obj)} not serializable")
    
    results = run_query(query, params)
    if results is not None:
        return json.dumps(results, indent=2, default=json_serializer, ensure_ascii=False)
    return "[]"

