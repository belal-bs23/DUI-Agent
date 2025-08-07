#!/usr/bin/env python3
"""
Analyze Table Structure Script
Analyzes the actual table structure to understand what columns are available.
"""

import os
import sys
import pyodbc
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def get_connection_string():
    """Get database connection string."""
    server = os.getenv('DB_SERVER', 'localhost\\SQLEXPRESS')
    database = os.getenv('DB_NAME', 'LEADRS_DUI_STAGE')
    username = os.getenv('DB_USERNAME', '')
    password = os.getenv('DB_PASSWORD', '')
    
    if username and password:
        return f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}"
    else:
        return f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes"

def analyze_table_structure():
    """Analyze the actual table structure."""
    print("Analyzing table structure...")
    print(f"Server: {os.getenv('DB_SERVER', 'localhost\\SQLEXPRESS')}")
    print(f"Database: {os.getenv('DB_NAME', 'LEADRS_DUI_STAGE')}")
    
    connection_string = get_connection_string()
    
    # Tables that the failed views are trying to reference
    tables_to_analyze = [
        'tbl_opt_mark43_lookup',
        'CaseHeaders', 
        'Defendants',
        'CaseOffenses',
        'PhysicalEvidence'
    ]
    
    try:
        with pyodbc.connect(connection_string) as conn:
            cursor = conn.cursor()
            
            for table_name in tables_to_analyze:
                print(f"\n{'='*60}")
                print(f"Table: DUI.{table_name}")
                print(f"{'='*60}")
                
                # Check if table exists
                cursor.execute("""
                    SELECT COUNT(*) 
                    FROM INFORMATION_SCHEMA.TABLES 
                    WHERE TABLE_SCHEMA = 'DUI' AND TABLE_NAME = ?
                """, table_name)
                
                exists = cursor.fetchone()[0] > 0
                if not exists:
                    print(f"❌ Table DUI.{table_name} does not exist!")
                    continue
                
                # Get column information
                cursor.execute("""
                    SELECT 
                        COLUMN_NAME,
                        DATA_TYPE,
                        IS_NULLABLE,
                        COLUMN_DEFAULT
                    FROM INFORMATION_SCHEMA.COLUMNS 
                    WHERE TABLE_SCHEMA = 'DUI' AND TABLE_NAME = ?
                    ORDER BY ORDINAL_POSITION
                """, table_name)
                
                columns = cursor.fetchall()
                
                if columns:
                    print(f"Columns ({len(columns)}):")
                    for col in columns:
                        col_name, data_type, nullable, default_val = col
                        nullable_str = "NULL" if nullable == "YES" else "NOT NULL"
                        default_str = f" DEFAULT {default_val}" if default_val else ""
                        print(f"  - {col_name}: {data_type} {nullable_str}{default_str}")
                else:
                    print("No columns found!")
                
                # Get sample data (first 3 rows)
                try:
                    cursor.execute(f"SELECT TOP 3 * FROM DUI.{table_name}")
                    sample_rows = cursor.fetchall()
                    
                    if sample_rows:
                        print(f"\nSample data (first 3 rows):")
                        for i, row in enumerate(sample_rows, 1):
                            print(f"  Row {i}: {row}")
                    else:
                        print(f"\nNo data in table")
                        
                except Exception as e:
                    print(f"\nCould not get sample data: {e}")
            
    except Exception as e:
        print(f"Database connection failed: {e}")

if __name__ == "__main__":
    analyze_table_structure() 