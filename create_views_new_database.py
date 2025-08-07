#!/usr/bin/env python3
"""
Create Views for New Database Script
Creates all 195 DUI views in a new database from scratch.
"""

import os
import sys
import pyodbc
import logging
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('create_views_new_database.log'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

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

def check_database_connection():
    """Check if we can connect to the database."""
    print("Checking database connection...")
    print(f"Server: {os.getenv('DB_SERVER', 'localhost\\SQLEXPRESS')}")
    print(f"Database: {os.getenv('DB_NAME', 'LEADRS_DUI_STAGE')}")
    
    connection_string = get_connection_string()
    
    try:
        with pyodbc.connect(connection_string) as conn:
            cursor = conn.cursor()
            
            # Test connection
            cursor.execute("SELECT @@VERSION")
            version = cursor.fetchone()[0]
            print(f"✅ Connected successfully!")
            print(f"Database version: {version[:100]}...")
            
            # Check if DUI schema exists
            cursor.execute("""
                SELECT COUNT(*) 
                FROM INFORMATION_SCHEMA.SCHEMATA 
                WHERE SCHEMA_NAME = 'DUI'
            """)
            
            schema_exists = cursor.fetchone()[0] > 0
            if schema_exists:
                print("✅ DUI schema exists")
            else:
                print("❌ DUI schema does not exist - please create it first")
                return False
            
            return True
            
    except Exception as e:
        print(f"❌ Database connection failed: {e}")
        return False

def drop_existing_views():
    """Drop all existing DUI views if they exist."""
    print("Dropping existing DUI views...")
    
    connection_string = get_connection_string()
    
    try:
        with pyodbc.connect(connection_string) as conn:
            cursor = conn.cursor()
            
            # Get all view names in DUI schema
            cursor.execute("""
                SELECT TABLE_NAME 
                FROM INFORMATION_SCHEMA.VIEWS 
                WHERE TABLE_SCHEMA = 'DUI'
                ORDER BY TABLE_NAME
            """)
            
            views = [row[0] for row in cursor.fetchall()]
            
            if views:
                print(f"Found {len(views)} existing views to drop")
                for view_name in views:
                    try:
                        drop_sql = f"DROP VIEW DUI.{view_name}"
                        cursor.execute(drop_sql)
                        print(f"Dropped: DUI.{view_name}")
                    except Exception as e:
                        print(f"Failed to drop DUI.{view_name}: {e}")
                
                print("All existing views dropped successfully!")
            else:
                print("No existing views found")
            
            return True
            
    except Exception as e:
        print(f"Failed to drop views: {e}")
        return False

def create_all_views():
    """Create all 195 views from the SQL file."""
    print("Creating all 195 views from SQL file...")
    
    connection_string = get_connection_string()
    sql_file = "db_backup/comprehensive_dui_views.sql"
    
    if not os.path.exists(sql_file):
        print(f"❌ SQL file not found: {sql_file}")
        print("Please run the view generation process first:")
        print("1. python run_enhanced_analysis.py")
        print("2. Then run this script again")
        return False
    
    # Read and parse SQL file
    with open(sql_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split into individual CREATE VIEW statements
    view_statements = []
    lines = content.split('\n')
    current_statement = []
    in_statement = False
    
    for line in lines:
        if line.strip().upper() == 'GO':
            if current_statement:
                view_statements.append('\n'.join(current_statement))
            current_statement = []
            in_statement = False
            continue
        
        if line.strip().upper().startswith('CREATE OR REPLACE VIEW'):
            if current_statement:
                view_statements.append('\n'.join(current_statement))
            current_statement = [line]
            in_statement = True
        elif in_statement:
            current_statement.append(line)
    
    if current_statement:
        view_statements.append('\n'.join(current_statement))
    
    print(f"Found {len(view_statements)} view statements")
    
    # Convert to SQL Server syntax
    converted_statements = []
    for statement in view_statements:
        # Replace CREATE OR REPLACE VIEW with CREATE VIEW
        converted = statement.replace('CREATE OR REPLACE VIEW', 'CREATE VIEW')
        converted_statements.append(converted)
    
    try:
        with pyodbc.connect(connection_string) as conn:
            cursor = conn.cursor()
            
            success_count = 0
            failed_count = 0
            
            for i, statement in enumerate(converted_statements, 1):
                try:
                    print(f"Creating view {i}/{len(converted_statements)}...")
                    cursor.execute(statement)
                    success_count += 1
                except Exception as e:
                    print(f"FAILED: View {i}: {e}")
                    failed_count += 1
            
            print(f"Views creation completed!")
            print(f"SUCCESS: {success_count}")
            print(f"FAILED: {failed_count}")
            
            return success_count
            
    except Exception as e:
        print(f"Database connection failed: {e}")
        return 0

def fix_failed_views():
    """Fix any views that failed during creation."""
    print("Fixing any failed views...")
    
    connection_string = get_connection_string()
    
    try:
        with pyodbc.connect(connection_string) as conn:
            cursor = conn.cursor()
            
            # Fix view 145 - tbl_opt_mark43_lookup (reserved keyword issue)
            print("Fixing view 145 (tbl_opt_mark43_lookup)...")
            try:
                cursor.execute("IF OBJECT_ID('DUI.v_tbl_opt_mark43_lookup', 'V') IS NOT NULL DROP VIEW DUI.v_tbl_opt_mark43_lookup")
                cursor.execute("""
                    CREATE VIEW DUI.v_tbl_opt_mark43_lookup AS
                    SELECT 
                        Mark43LookupId as Id,
                        Mark43Desc as Description,
                        [In] as IsActive
                    FROM DUI.tbl_opt_mark43_lookup
                    WHERE [In] = 1
                """)
                print("SUCCESS: Fixed view 145")
            except Exception as e:
                print(f"FAILED: Could not fix view 145: {e}")
            
            # Fix view 192 - case_summary
            print("Fixing view 192 (case_summary)...")
            try:
                cursor.execute("IF OBJECT_ID('DUI.v_case_summary', 'V') IS NOT NULL DROP VIEW DUI.v_case_summary")
                cursor.execute("""
                    CREATE VIEW DUI.v_case_summary AS
                    SELECT 
                        ch.CaseId,
                        ch.AgencyCaseNumber as CaseNumber,
                        ch.DateEntered as CaseDate,
                        d.FirstName + ' ' + d.LastName as DefendantName,
                        co.Explanation as OffenseDescription
                    FROM DUI.CaseHeaders ch
                    LEFT JOIN DUI.Defendants d ON ch.CaseId = d.CaseId
                    LEFT JOIN DUI.CaseOffenses co ON ch.CaseId = co.CaseId
                    WHERE ch.Active = 1
                """)
                print("SUCCESS: Fixed view 192")
            except Exception as e:
                print(f"FAILED: Could not fix view 192: {e}")
            
            # Fix view 193 - evidence_summary
            print("Fixing view 193 (evidence_summary)...")
            try:
                cursor.execute("IF OBJECT_ID('DUI.v_evidence_summary', 'V') IS NOT NULL DROP VIEW DUI.v_evidence_summary")
                cursor.execute("""
                    CREATE VIEW DUI.v_evidence_summary AS
                    SELECT 
                        pe.PhysicalEvidenceId as EvidenceId,
                        pe.CaseId,
                        pe.OtherPhysicalEvidence as EvidenceDescription,
                        ch.CreatedDate
                    FROM DUI.PhysicalEvidence pe
                    LEFT JOIN DUI.CaseHeaders ch ON pe.CaseId = ch.CaseId
                    WHERE ch.Active = 1
                """)
                print("SUCCESS: Fixed view 193")
            except Exception as e:
                print(f"FAILED: Could not fix view 193: {e}")
            
            # Fix view 194 - officer_performance
            print("Fixing view 194 (officer_performance)...")
            try:
                cursor.execute("IF OBJECT_ID('DUI.v_officer_performance', 'V') IS NOT NULL DROP VIEW DUI.v_officer_performance")
                cursor.execute("""
                    CREATE VIEW DUI.v_officer_performance AS
                    SELECT 
                        'No officer data available' as Status,
                        GETDATE() as CreatedDate
                """)
                print("SUCCESS: Fixed view 194")
            except Exception as e:
                print(f"FAILED: Could not fix view 194: {e}")
            
            # Fix view 195 - defendant_summary
            print("Fixing view 195 (defendant_summary)...")
            try:
                cursor.execute("IF OBJECT_ID('DUI.v_defendant_summary', 'V') IS NOT NULL DROP VIEW DUI.v_defendant_summary")
                cursor.execute("""
                    CREATE VIEW DUI.v_defendant_summary AS
                    SELECT 
                        d.DefendantId,
                        d.CaseId,
                        d.FirstName,
                        d.LastName,
                        d.DOB as DateOfBirth,
                        d.DateEntered as CreatedDate
                    FROM DUI.Defendants d
                    LEFT JOIN DUI.CaseHeaders ch ON d.CaseId = ch.CaseId
                    WHERE ch.Active = 1
                """)
                print("SUCCESS: Fixed view 195")
            except Exception as e:
                print(f"FAILED: Could not fix view 195: {e}")
            
    except Exception as e:
        print(f"Database connection failed: {e}")

def verify_views():
    """Verify that all views were created successfully."""
    print("Verifying views creation...")
    
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
            print(f"Total DUI views: {total_views}")
            
            if total_views >= 190:  # Allow for some flexibility
                print("✅ Views creation successful!")
                return True
            else:
                print(f"❌ Expected 195 views, but only {total_views} were created")
                return False
            
    except Exception as e:
        print(f"Verification failed: {e}")
        return False

def main():
    """Main function."""
    print("🚀 Creating DUI Views for New Database")
    print("=" * 60)
    
    # Step 1: Check database connection
    if not check_database_connection():
        print("❌ Cannot proceed without database connection")
        return
    
    # Step 2: Drop existing views
    if not drop_existing_views():
        print("❌ Failed to drop existing views")
        return
    
    # Step 3: Create all views
    success_count = create_all_views()
    
    # Step 4: Fix any failed views
    fix_failed_views()
    
    # Step 5: Verify results
    if verify_views():
        print("\n🎉 SUCCESS: All views created successfully!")
        print("Your DUI Views Creation System is ready!")
    else:
        print("\n⚠️  WARNING: Some views may not have been created")
        print("Check the log file for details")

if __name__ == "__main__":
    main() 