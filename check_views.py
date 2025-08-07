#!/usr/bin/env python3
"""
Check Views Script
Verifies what views exist in the database.
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

def check_views():
    """Check what views exist in the database."""
    print("Checking views in database...")
    print(f"Server: {os.getenv('DB_SERVER', 'localhost\\SQLEXPRESS')}")
    print(f"Database: {os.getenv('DB_NAME', 'LEADRS_DUI_STAGE')}")
    
    connection_string = get_connection_string()
    
    try:
        with pyodbc.connect(connection_string) as conn:
            cursor = conn.cursor()
            
            # Check total view count
            cursor.execute("""
                SELECT COUNT(*) as TotalViews 
                FROM INFORMATION_SCHEMA.VIEWS 
                WHERE TABLE_SCHEMA = 'DUI'
            """)
            
            total_views = cursor.fetchone()[0]
            print(f"\nTotal DUI views: {total_views}")
            
            # List all views
            cursor.execute("""
                SELECT TABLE_NAME 
                FROM INFORMATION_SCHEMA.VIEWS 
                WHERE TABLE_SCHEMA = 'DUI'
                ORDER BY TABLE_NAME
            """)
            
            views = [row[0] for row in cursor.fetchall()]
            
            if views:
                print(f"\nFirst 10 views:")
                for i, view in enumerate(views[:10], 1):
                    print(f"  {i}. {view}")
                
                if len(views) > 10:
                    print(f"  ... and {len(views) - 10} more")
                
                print(f"\nLast 10 views:")
                for i, view in enumerate(views[-10:], len(views) - 9):
                    print(f"  {i}. {view}")
            
            # Check specific failed views
            failed_view_names = ['v_tbl_opt_mark43_lookup', 'v_case_summary', 'v_evidence_summary', 'v_officer_performance', 'v_defendant_summary']
            
            print(f"\nChecking specific failed views:")
            for view_name in failed_view_names:
                cursor.execute("""
                    SELECT COUNT(*) 
                    FROM INFORMATION_SCHEMA.VIEWS 
                    WHERE TABLE_SCHEMA = 'DUI' AND TABLE_NAME = ?
                """, view_name)
                
                exists = cursor.fetchone()[0] > 0
                status = "✅ EXISTS" if exists else "❌ MISSING"
                print(f"  {view_name}: {status}")
            
            # Check database version
            cursor.execute("SELECT @@VERSION")
            version = cursor.fetchone()[0]
            print(f"\nDatabase version: {version[:100]}...")
            
    except Exception as e:
        print(f"Database connection failed: {e}")

if __name__ == "__main__":
    check_views() 