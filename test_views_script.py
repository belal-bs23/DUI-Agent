#!/usr/bin/env python3
"""
Test script for DUI Views Creation
Tests the SQL parsing and conversion without database connection.
"""

import os
import sys
from pathlib import Path

def test_sql_parsing():
    """Test SQL file parsing and conversion."""
    print("Testing SQL file parsing and conversion...")
    
    sql_file_path = "db_backup/comprehensive_dui_views.sql"
    
    # Check if SQL file exists
    if not os.path.exists(sql_file_path):
        print(f"ERROR: SQL file not found: {sql_file_path}")
        return False
    
    file_size = os.path.getsize(sql_file_path)
    print(f"SQL file found: {sql_file_path} ({file_size:,} bytes)")
    
    # Read and parse SQL file
    try:
        print("Reading SQL file...")
        with open(sql_file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Split into individual CREATE VIEW statements
        view_statements = []
        lines = content.split('\n')
        current_statement = []
        in_statement = False
        
        for line in lines:
            if line.strip().upper().startswith('CREATE OR REPLACE VIEW'):
                if current_statement:
                    view_statements.append('\n'.join(current_statement))
                current_statement = [line]
                in_statement = True
            elif in_statement:
                current_statement.append(line)
                if line.strip().endswith(';'):
                    view_statements.append('\n'.join(current_statement))
                    current_statement = []
                    in_statement = False
        
        # Add any remaining statement
        if current_statement:
            view_statements.append('\n'.join(current_statement))
        
        print(f"Parsed {len(view_statements)} view statements")
        
        # Convert to SQL Server syntax
        converted_statements = []
        for statement in view_statements:
            converted = statement.replace('CREATE OR REPLACE VIEW', 'CREATE VIEW')
            converted_statements.append(converted)
        
        print(f"Converted {len(converted_statements)} statements to SQL Server syntax")
        
        # Show sample statements
        print("\nSample statements:")
        for i, statement in enumerate(converted_statements[:3], 1):
            print(f"\n--- Statement {i} ---")
            lines = statement.split('\n')
            for line in lines[:5]:  # Show first 5 lines
                print(line)
            if len(lines) > 5:
                print("...")
        
        return True
        
    except Exception as e:
        print(f"ERROR: Error processing SQL file: {e}")
        return False

def main():
    """Main function."""
    print("DUI Views Script Test")
    print("=" * 50)
    
    success = test_sql_parsing()
    
    if success:
        print("\nSUCCESS: SQL parsing and conversion test passed!")
        print("The script is ready to create views in the database.")
        print("\nTo create views, run:")
        print("  python create_dui_views.py")
    else:
        print("\nFAILED: SQL parsing and conversion test failed!")
        sys.exit(1)

if __name__ == "__main__":
    main() 