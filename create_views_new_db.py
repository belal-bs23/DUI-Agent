#!/usr/bin/env python3
"""
Create DUI Views in New Database
================================

Script to create DUI views in a new database with custom connection details.
"""

import os
import sys
import pyodbc
from pathlib import Path
from dotenv import load_dotenv

def get_connection_details():
    """Get database connection details from user."""
    print("🔧 Database Connection Setup")
    print("=" * 40)
    
    # Load existing .env if available
    load_dotenv('.env')
    
    # Get connection details
    server = input(f"Database Server [{os.getenv('DB_SERVER', 'localhost\\SQLEXPRESS')}]: ").strip()
    if not server:
        server = os.getenv('DB_SERVER', 'localhost\\SQLEXPRESS')
    
    database = input(f"Database Name [{os.getenv('DB_DATABASE', 'LEADRS_DUI_STAGE')}]: ").strip()
    if not database:
        database = os.getenv('DB_DATABASE', 'LEADRS_DUI_STAGE')
    
    username = input("Database Username (leave empty for Windows Auth): ").strip()
    password = input("Database Password (leave empty for Windows Auth): ").strip()
    
    return server, database, username, password

def test_connection(server, database, username, password):
    """Test database connection."""
    try:
        if username and password:
            conn_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
        else:
            conn_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes'
        
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        
        # Test basic query
        cursor.execute("SELECT @@VERSION")
        version = cursor.fetchone()[0]
        
        conn.close()
        
        print(f"✅ Connection successful!")
        print(f"📊 SQL Server Version: {version[:100]}...")
        return True
        
    except Exception as e:
        print(f"❌ Connection failed: {e}")
        return False

def check_existing_views(server, database, username, password):
    """Check if DUI views already exist."""
    try:
        if username and password:
            conn_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
        else:
            conn_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes'
        
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        
        # Check for existing DUI views
        cursor.execute("SELECT COUNT(*) FROM INFORMATION_SCHEMA.VIEWS WHERE TABLE_SCHEMA = 'DUI'")
        view_count = cursor.fetchone()[0]
        
        conn.close()
        
        if view_count > 0:
            print(f"⚠️  Found {view_count} existing DUI views in database '{database}'")
            response = input("Do you want to continue and create additional views? (y/n): ").strip().lower()
            return response == 'y'
        else:
            print(f"✅ No existing DUI views found in database '{database}'")
            return True
            
    except Exception as e:
        print(f"❌ Error checking existing views: {e}")
        return False

def create_views(server, database, username, password):
    """Create DUI views in the database."""
    sql_file = Path("db_backup/comprehensive_dui_views.sql")
    
    if not sql_file.exists():
        print(f"❌ SQL file not found: {sql_file}")
        return False
    
    try:
        if username and password:
            conn_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
        else:
            conn_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes'
        
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        
        print("🔧 Creating DUI views...")
        print("=" * 40)
        
        # Read SQL file
        with open(sql_file, 'r', encoding='utf-8') as f:
            sql_content = f.read()
        
        # Split into individual statements
        statements = [stmt.strip() for stmt in sql_content.split(';') if stmt.strip()]
        
        successful = 0
        failed = 0
        
        for i, statement in enumerate(statements, 1):
            if statement:
                try:
                    cursor.execute(statement)
                    successful += 1
                    print(f"  ✅ Statement {i}/{len(statements)} executed")
                except Exception as e:
                    failed += 1
                    print(f"  ⚠️  Statement {i} failed: {e}")
        
        conn.commit()
        conn.close()
        
        print("=" * 40)
        print(f"📊 Results: {successful} successful, {failed} failed")
        
        if successful > 0:
            print("✅ Views created successfully!")
            return True
        else:
            print("❌ No views were created successfully")
            return False
            
    except Exception as e:
        print(f"❌ Error creating views: {e}")
        return False

def update_env_file(server, database, username, password):
    """Update .env file with new database details."""
    env_file = Path('.env')
    
    # Read existing .env content
    env_content = ""
    if env_file.exists():
        with open(env_file, 'r') as f:
            env_content = f.read()
    
    # Update database settings
    lines = env_content.split('\n')
    updated_lines = []
    
    db_updated = False
    for line in lines:
        if line.startswith('DB_SERVER='):
            updated_lines.append(f'DB_SERVER={server}')
            db_updated = True
        elif line.startswith('DB_DATABASE='):
            updated_lines.append(f'DB_DATABASE={database}')
            db_updated = True
        elif line.startswith('DB_USERNAME='):
            updated_lines.append(f'DB_USERNAME={username}')
            db_updated = True
        elif line.startswith('DB_PASSWORD='):
            updated_lines.append(f'DB_PASSWORD={password}')
            db_updated = True
        else:
            updated_lines.append(line)
    
    # Add database settings if they don't exist
    if not db_updated:
        updated_lines.extend([
            '',
            '# Database Configuration',
            f'DB_SERVER={server}',
            f'DB_DATABASE={database}',
            f'DB_USERNAME={username}',
            f'DB_PASSWORD={password}'
        ])
    
    # Write updated .env file
    with open(env_file, 'w') as f:
        f.write('\n'.join(updated_lines))
    
    print(f"✅ Updated .env file with new database settings")

def main():
    """Main function."""
    print("🚀 Create DUI Views in New Database")
    print("=" * 50)
    
    # Get connection details
    server, database, username, password = get_connection_details()
    
    print(f"\n📋 Connection Details:")
    print(f"  Server: {server}")
    print(f"  Database: {database}")
    print(f"  Username: {username if username else 'Windows Authentication'}")
    
    # Test connection
    print(f"\n🔍 Testing connection...")
    if not test_connection(server, database, username, password):
        print("❌ Cannot proceed without database connection")
        return
    
    # Check existing views
    print(f"\n🔍 Checking existing views...")
    if not check_existing_views(server, database, username, password):
        print("❌ Operation cancelled")
        return
    
    # Create views
    print(f"\n🔧 Creating views...")
    if create_views(server, database, username, password):
        # Update .env file
        print(f"\n📝 Updating configuration...")
        update_env_file(server, database, username, password)
        
        print(f"\n🎉 Success! DUI views created in database '{database}'")
        print(f"💡 You can now use the DUI SQL Agent with the new database")
    else:
        print(f"\n❌ Failed to create views in database '{database}'")

if __name__ == "__main__":
    main()
