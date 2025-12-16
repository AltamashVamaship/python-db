"""
Script to generate SQLAlchemy models for all tables in the database
"""
from sqlalchemy import create_engine, inspect, MetaData
from sqlalchemy.orm import declarative_base
from urllib.parse import quote_plus
from config import DB_CONFIG

# URL encode password to handle special characters like @
encoded_password = quote_plus(DB_CONFIG['password'])

# Create database connection string
DATABASE_URL = f"mysql+mysqlconnector://{DB_CONFIG['user']}:{encoded_password}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"

# Create engine
engine = create_engine(DATABASE_URL, echo=False, pool_pre_ping=True)

# Create inspector
inspector = inspect(engine)

# Type mapping from MySQL to SQLAlchemy
TYPE_MAPPING = {
    'int': 'Integer',
    'bigint': 'BigInteger',
    'smallint': 'SmallInteger',
    'tinyint': 'SmallInteger',
    'varchar': 'String',
    'char': 'String',
    'text': 'Text',
    'longtext': 'Text',
    'mediumtext': 'Text',
    'datetime': 'DateTime',
    'date': 'Date',
    'time': 'Time',
    'timestamp': 'DateTime',
    'decimal': 'Numeric',
    'numeric': 'Numeric',
    'float': 'Float',
    'double': 'Float',
    'boolean': 'Boolean',
    'bool': 'Boolean',
    'blob': 'LargeBinary',
    'longblob': 'LargeBinary',
    'json': 'JSON',
}

def get_sqlalchemy_type(col_type):
    """Convert MySQL column type to SQLAlchemy type"""
    col_type_lower = col_type.lower()
    
    # Handle VARCHAR with length
    if col_type_lower.startswith('varchar'):
        length = col_type.split('(')[1].split(')')[0] if '(' in col_type else '255'
        return f"String({length})"
    
    # Handle CHAR with length
    if col_type_lower.startswith('char'):
        length = col_type.split('(')[1].split(')')[0] if '(' in col_type else '1'
        return f"String({length})"
    
    # Handle DECIMAL/NUMERIC with precision
    if col_type_lower.startswith('decimal') or col_type_lower.startswith('numeric'):
        if '(' in col_type:
            parts = col_type.split('(')[1].split(')')[0].split(',')
            precision = parts[0]
            scale = parts[1] if len(parts) > 1 else '0'
            return f"Numeric({precision}, {scale})"
        return "Numeric"
    
    # Handle INT with display width (ignore display width)
    if col_type_lower.startswith('int'):
        return 'Integer'
    
    # Handle other types
    for mysql_type, sqlalchemy_type in TYPE_MAPPING.items():
        if col_type_lower.startswith(mysql_type):
            return sqlalchemy_type
    
    # Default to String if unknown
    return 'String(255)'

def generate_model_class(table_name, columns, has_primary_key=True):
    """Generate a SQLAlchemy model class for a table"""
    # Convert table name to class name (PascalCase, handle plural)
    class_name = ''.join(word.capitalize() for word in table_name.split('_'))
    
    # Generate class code
    lines = [f"class {class_name}(Base):"]
    lines.append(f"    __tablename__ = '{table_name}'")
    if not has_primary_key:
        # For tables without primary keys, we need to use __table_args__
        lines.append(f"    __table_args__ = {{'extend_existing': True}}")
    lines.append("")
    
    # Add columns
    for col in columns:
        col_name = col['name']
        col_type = col['type']
        nullable = col['nullable']
        default = col.get('default')
        primary_key = col.get('primary_key', False)
        autoincrement = col.get('autoincrement', False)
        
        # Get SQLAlchemy type
        sa_type = get_sqlalchemy_type(col_type)
        
        # Build column definition
        col_def = f"    {col_name} = Column({sa_type}"
        
        # Add constraints
        if primary_key:
            col_def += ", primary_key=True"
        if not nullable:
            col_def += ", nullable=False"
        elif nullable:
            col_def += ", nullable=True"
        if autoincrement and primary_key:
            col_def += ", autoincrement=True"
        if default is not None and default != 'NULL':
            # Handle default values
            default_str = str(default)
            # Skip server_default for date/time literals (they're usually set by application)
            # Only add server_default for CURRENT_TIMESTAMP and numeric/string defaults
            if 'CURRENT_TIMESTAMP' in default_str.upper():
                # For CURRENT_TIMESTAMP, use text() function
                if 'ON UPDATE' in default_str:
                    col_def += f", server_default=text(\"'{default_str}'\")"
                else:
                    col_def += f", server_default=text('{default_str}')"
            elif default_str.replace('.', '').replace('-', '').isdigit() or default_str in ['0', '1', 'true', 'false', 'TRUE', 'FALSE']:
                # Numeric or boolean defaults
                col_def += f", server_default='{default_str}'"
            # Skip date/time string literals like '2000-01-01 00:00:00' - they cause syntax errors
        
        col_def += ")"
        lines.append(col_def)
    
    return '\n'.join(lines)

def main():
    """Generate models for all tables"""
    print("Connecting to database...")
    
    # Get all tables
    table_names = inspector.get_table_names()
    print(f"Found {len(table_names)} tables")
    
    # Generate model code
    model_classes = []
    imports = [
        "from sqlalchemy import create_engine, Column, Integer, String, DateTime, Numeric, Text, Boolean, MetaData, Table, inspect, BigInteger, SmallInteger, Date, Time, Float, LargeBinary, JSON, text",
        "from sqlalchemy.orm import declarative_base, sessionmaker",
        "from urllib.parse import quote_plus",
        "from config import DB_CONFIG",
        "from datetime import datetime",
        "",
        "# URL encode password to handle special characters like @",
        "encoded_password = quote_plus(DB_CONFIG['password'])",
        "",
        "# Create database connection string",
        "DATABASE_URL = f\"mysql+mysqlconnector://{DB_CONFIG['user']}:{encoded_password}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}\"",
        "",
        "# Create engine",
        "engine = create_engine(DATABASE_URL, echo=False, pool_pre_ping=True)",
        "",
        "# Create session factory",
        "SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)",
        "",
        "# Base class for models",
        "Base = declarative_base()",
        "",
        "",
    ]
    
    print("\nGenerating models...")
    for table_name in sorted(table_names):
        print(f"  Processing {table_name}...")
        columns = inspector.get_columns(table_name)
        
        # Get primary keys
        pk_constraint = inspector.get_pk_constraint(table_name)
        pk_columns = set(pk_constraint.get('constrained_columns', []))
        
        # Get autoincrement info
        autoincrement_cols = set()
        for col in columns:
            if col.get('autoincrement', False):
                autoincrement_cols.add(col['name'])
        
        # Prepare column info
        col_info = []
        for col in columns:
            col_dict = {
                'name': col['name'],
                'type': str(col['type']),
                'nullable': col.get('nullable', True),
                'default': col.get('default'),
                'primary_key': col['name'] in pk_columns,
                'autoincrement': col['name'] in autoincrement_cols
            }
            col_info.append(col_dict)
        
        # Check if table has primary key
        has_primary_key = any(col['primary_key'] for col in col_info)
        
        # Skip tables without primary keys - SQLAlchemy requires PK for ORM models
        # These can still be queried using get_table()
        if not has_primary_key:
            print(f"    ⚠️  Skipping {table_name} (no primary key - use get_table() instead)")
            continue
        
        # Generate model class
        model_code = generate_model_class(table_name, col_info, has_primary_key)
        model_classes.append(model_code)
        model_classes.append("")
    
    # Write to file
    output_file = 'models.py'
    print(f"\nWriting models to {output_file}...")
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('"""\n')
        f.write('SQLAlchemy ORM Models for the database\n')
        f.write('Auto-generated - DO NOT EDIT MANUALLY\n')
        f.write('Run generate_models.py to regenerate\n')
        f.write('"""\n')
        f.write('\n')
        f.write('\n'.join(imports))
        f.write('\n')
        f.write('\n'.join(model_classes))
        f.write('\n')
        f.write('# Dynamic table reflection - allows querying any table without defining a model\n')
        f.write('metadata = MetaData()\n')
        f.write('\n')
        f.write('def get_table(table_name):\n')
        f.write('    """Get a table object by name (for dynamic queries)"""\n')
        f.write('    if table_name not in metadata.tables:\n')
        f.write('        Table(table_name, metadata, autoload_with=engine)\n')
        f.write('    return metadata.tables[table_name]\n')
        f.write('\n')
        f.write('def get_all_tables():\n')
        f.write('    """Get all table names from the database"""\n')
        f.write('    inspector = inspect(engine)\n')
        f.write('    return inspector.get_table_names()\n')
    
    print(f"\n✅ Successfully generated {len(table_names)} models in {output_file}")
    print("\nYou can now use these models in your queries!")

if __name__ == '__main__':
    main()

