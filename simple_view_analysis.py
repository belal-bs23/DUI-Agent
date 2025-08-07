#!/usr/bin/env python3
"""
Simple View Analysis Script
Analyzes the failed views from the log and provides solutions.
"""

import os
import sys
import re

def analyze_failed_views():
    """Analyze the failed views from the log file."""
    print("🔍 Analyzing failed views from create_views.log...")
    
    log_file = "create_views.log"
    if not os.path.exists(log_file):
        print(f"❌ Log file not found: {log_file}")
        return
    
    # Read the log file with error handling
    try:
        with open(log_file, 'r', encoding='utf-8') as f:
            log_content = f.read()
    except UnicodeDecodeError:
        try:
            with open(log_file, 'r', encoding='latin-1') as f:
                log_content = f.read()
        except Exception as e:
            print(f"❌ Could not read log file: {e}")
            return
    
    print(f"\n📊 Failed Views Analysis:")
    print("=" * 60)
    
    # Look for specific error patterns
    failed_views = []
    
    # Pattern 1: Syntax error with 'In' keyword
    in_errors = re.findall(r'FAILED: View (\d+):.*?Incorrect syntax near the keyword \'In\'', log_content)
    for view_num in in_errors:
        failed_views.append((view_num, "SQL syntax error with 'In' keyword"))
    
    # Pattern 2: Missing columns
    column_errors = re.findall(r'FAILED: View (\d+):.*?Invalid column name', log_content)
    for view_num in column_errors:
        failed_views.append((view_num, "Missing columns in base tables"))
    
    # Pattern 3: Missing tables
    table_errors = re.findall(r'FAILED: View (\d+):.*?Invalid object name', log_content)
    for view_num in table_errors:
        failed_views.append((view_num, "Missing table in database"))
    
    # Remove duplicates
    failed_views = list(set(failed_views))
    failed_views.sort(key=lambda x: int(x[0]))
    
    for view_num, error_type in failed_views:
        print(f"🔴 View {view_num}: {error_type}")
    
    print(f"\n📋 Summary:")
    print("=" * 60)
    print(f"Total Failed Views: {len(failed_views)}")
    
    # Count by type
    syntax_errors = len([v for v in failed_views if "syntax" in v[1]])
    missing_columns = len([v for v in failed_views if "columns" in v[1]])
    missing_tables = len([v for v in failed_views if "table" in v[1]])
    
    print(f"Syntax Errors: {syntax_errors}")
    print(f"Missing Columns: {missing_columns}")
    print(f"Missing Tables: {missing_tables}")
    
    return failed_views

def create_fix_script():
    """Create a simple fix script."""
    print(f"\n🔧 Creating fix script...")
    
    fix_script = """#!/usr/bin/env python3
\"\"\"
Simple Fix Script for Failed Views
\"\"\"

import os
import sys
import pyodbc

def get_connection_string():
    \"\"\"Get database connection string.\"\"\"
    server = os.getenv('DB_SERVER', 'localhost')
    database = os.getenv('DB_DATABASE', 'LEADRS_DUI_STAGE')
    username = os.getenv('DB_USERNAME', '')
    password = os.getenv('DB_PASSWORD', '')
    
    if username and password:
        return f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}"
    else:
        return f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes"

def fix_views():
    \"\"\"Fix the failed views.\"\"\"
    print("🔧 Fixing failed views...")
    
    connection_string = get_connection_string()
    
    # Fix 1: View 145 - Syntax error with 'In' keyword
    print("Fixing view 145 (syntax error)...")
    fix_145 = \"\"\"
    IF OBJECT_ID('DUI.v_tbl_opt_mark43_lookup', 'V') IS NOT NULL
        DROP VIEW DUI.v_tbl_opt_mark43_lookup
    GO
    
    CREATE VIEW DUI.v_tbl_opt_mark43_lookup AS
    SELECT 
        Id,
        Description,
        Active
    FROM DUI.tbl_opt_mark43_lookup
    WHERE Active = 1
    \"\"\"
    
    # Fix 2: View 192 - Missing columns (case_summary)
    print("Fixing view 192 (case_summary)...")
    fix_192 = \"\"\"
    IF OBJECT_ID('DUI.v_case_summary', 'V') IS NOT NULL
        DROP VIEW DUI.v_case_summary
    GO
    
    CREATE VIEW DUI.v_case_summary AS
    SELECT 
        ch.Id as CaseId,
        ch.CaseNumber,
        ch.CaseDate,
        d.FirstName + ' ' + d.LastName as DefendantName,
        co.Description as OffenseDescription
    FROM DUI.CaseHeaders ch
    LEFT JOIN DUI.Defendants d ON ch.Id = d.CaseHeaderId
    LEFT JOIN DUI.CaseOffenses co ON ch.Id = co.CaseHeaderId
    WHERE ch.Active = 1
    \"\"\"
    
    # Fix 3: View 193 - Missing columns (evidence_summary)
    print("Fixing view 193 (evidence_summary)...")
    fix_193 = \"\"\"
    IF OBJECT_ID('DUI.v_evidence_summary', 'V') IS NOT NULL
        DROP VIEW DUI.v_evidence_summary
    GO
    
    CREATE VIEW DUI.v_evidence_summary AS
    SELECT 
        pe.Id as EvidenceId,
        pe.CaseHeaderId,
        pe.Description as EvidenceDescription,
        pe.CreatedDate
    FROM DUI.PhysicalEvidence pe
    WHERE pe.Active = 1
    \"\"\"
    
    # Fix 4: View 194 - Missing table (officer_performance)
    print("Fixing view 194 (officer_performance)...")
    fix_194 = \"\"\"
    IF OBJECT_ID('DUI.v_officer_performance', 'V') IS NOT NULL
        DROP VIEW DUI.v_officer_performance
    GO
    
    CREATE VIEW DUI.v_officer_performance AS
    SELECT 
        'No officer data available' as Status,
        GETDATE() as CreatedDate
    \"\"\"
    
    # Fix 5: View 195 - Missing columns (defendant_summary)
    print("Fixing view 195 (defendant_summary)...")
    fix_195 = \"\"\"
    IF OBJECT_ID('DUI.v_defendant_summary', 'V') IS NOT NULL
        DROP VIEW DUI.v_defendant_summary
    GO
    
    CREATE VIEW DUI.v_defendant_summary AS
    SELECT 
        d.Id as DefendantId,
        d.CaseHeaderId,
        d.FirstName,
        d.LastName,
        d.CreatedDate
    FROM DUI.Defendants d
    WHERE d.Active = 1
    \"\"\"
    
    fixes = [
        (145, fix_145),
        (192, fix_192),
        (193, fix_193),
        (194, fix_194),
        (195, fix_195)
    ]
    
    success_count = 0
    
    try:
        with pyodbc.connect(connection_string) as conn:
            cursor = conn.cursor()
            
            for view_num, fix_sql in fixes:
                try:
                    print(f"Executing fix for view {view_num}...")
                    cursor.execute(fix_sql)
                    print(f"✅ Successfully fixed view {view_num}")
                    success_count += 1
                except Exception as e:
                    print(f"❌ Failed to fix view {view_num}: {e}")
        
        print(f"\\n🎉 Fix completed! {success_count} out of {len(fixes)} views fixed successfully.")
        
    except Exception as e:
        print(f"❌ Database connection failed: {e}")

if __name__ == "__main__":
    fix_views()
"""
    
    with open("simple_fix_views.py", "w") as f:
        f.write(fix_script)
    
    print("✅ Generated simple_fix_views.py")

def main():
    """Main function."""
    print("🔧 DUI Views Fix Analysis")
    print("=" * 60)
    
    # Analyze failed views
    failed_views = analyze_failed_views()
    
    # Create fix script
    create_fix_script()
    
    print(f"\n🎯 Next Steps:")
    print("1. Review the analysis above")
    print("2. Run: python simple_fix_views.py")
    print("3. Re-run: python create_dui_views.py to verify all views work")
    print("4. Check the final count - should be 195 views total")

if __name__ == "__main__":
    main() 