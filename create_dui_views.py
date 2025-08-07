#!/usr/bin/env python3
"""
Create DUI Views Script
Executes the comprehensive DUI views SQL file to create all views in the database.
"""

import os
import sys
import pyodbc
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('create_views.log'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

class DUIViewsCreator:
    """Class to create DUI views in the database."""
    
    def __init__(self):
        """Initialize the views creator."""
        self.connection_string = self._get_connection_string()
        self.sql_file_path = "db_backup/comprehensive_dui_views.sql"
        
    def _get_connection_string(self):
        """Get database connection string from environment or use default."""
        # You can set these environment variables or modify the defaults
        server = os.getenv('DB_SERVER', 'localhost')
        database = os.getenv('DB_DATABASE', 'LEADRS_DUI_STAGE')
        username = os.getenv('DB_USERNAME', '')
        password = os.getenv('DB_PASSWORD', '')
        
        if username and password:
            # SQL Server Authentication
            return f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}"
        else:
            # Windows Authentication
            return f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes"
    
    def test_connection(self):
        """Test database connection."""
        try:
            logger.info("Testing database connection...")
            with pyodbc.connect(self.connection_string) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT @@VERSION")
                version = cursor.fetchone()[0]
                logger.info(f"Database connection successful!")
                logger.info(f"Database version: {version[:100]}...")
                return True
        except Exception as e:
            logger.error(f"Database connection failed: {e}")
            return False
    
    def check_sql_file(self):
        """Check if the SQL file exists and is readable."""
        if not os.path.exists(self.sql_file_path):
            logger.error(f"SQL file not found: {self.sql_file_path}")
            return False
        
        file_size = os.path.getsize(self.sql_file_path)
        logger.info(f"SQL file found: {self.sql_file_path} ({file_size:,} bytes)")
        return True
    
    def read_sql_file(self):
        """Read and parse the SQL file."""
        try:
            logger.info("Reading SQL file...")
            with open(self.sql_file_path, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # Split into individual CREATE VIEW statements
            # Look for CREATE VIEW statements (SQL Server format)
            view_statements = []
            lines = content.split('\n')
            current_statement = []
            in_statement = False
            
            for line in lines:
                if line.strip().upper().startswith('CREATE VIEW'):
                    if current_statement:
                        view_statements.append('\n'.join(current_statement))
                    current_statement = [line]
                    in_statement = True
                elif in_statement:
                    current_statement.append(line)
                    # Check for end of statement (empty line or next CREATE VIEW)
                    if line.strip() == '' or line.strip().upper().startswith('CREATE VIEW'):
                        if current_statement and current_statement[-1].strip() == '':
                            current_statement.pop()  # Remove empty line
                        if current_statement:
                            view_statements.append('\n'.join(current_statement))
                        current_statement = []
                        in_statement = False
                        if line.strip().upper().startswith('CREATE VIEW'):
                            current_statement = [line]
                            in_statement = True
            
            # Add any remaining statement
            if current_statement:
                view_statements.append('\n'.join(current_statement))
            
            logger.info(f"Parsed {len(view_statements)} view statements")
            return view_statements
            
        except Exception as e:
            logger.error(f"Error reading SQL file: {e}")
            return []
    
    def convert_to_sql_server_syntax(self, view_statements):
        """Convert statements to SQL Server compatible syntax."""
        converted_statements = []
        
        for statement in view_statements:
            # The statements are already in SQL Server format
            # Just ensure they don't have semicolons at the end
            converted = statement.rstrip().rstrip(';')
            converted_statements.append(converted)
        
        logger.info(f"Processed {len(converted_statements)} statements for SQL Server")
        return converted_statements
    
    def drop_existing_views(self, view_names):
        """Drop existing views before creating new ones."""
        try:
            logger.info("Dropping existing views...")
            with pyodbc.connect(self.connection_string) as conn:
                cursor = conn.cursor()
                
                dropped_count = 0
                
                for view_name in view_names:
                    try:
                        # Drop view if it exists
                        drop_sql = f"IF OBJECT_ID('{view_name}', 'V') IS NOT NULL DROP VIEW {view_name}"
                        cursor.execute(drop_sql)
                        dropped_count += 1
                        logger.info(f"Dropped existing view: {view_name}")
                    except Exception as e:
                        logger.warning(f"Could not drop view {view_name}: {e}")
                        # Continue with next view
                        continue
                
                conn.commit()
                logger.info(f"Dropped {dropped_count} existing views")
                return True
                
        except Exception as e:
            logger.error(f"Error dropping views: {e}")
            return False
    
    def create_views(self, view_statements):
        """Create all views in the database."""
        if not view_statements:
            logger.error("No view statements to execute")
            return False
        
        try:
            logger.info("Creating views in database...")
            with pyodbc.connect(self.connection_string) as conn:
                cursor = conn.cursor()
                
                successful_views = 0
                failed_views = 0
                
                for i, statement in enumerate(view_statements, 1):
                    try:
                        # Extract view name for logging
                        view_name = self._extract_view_name(statement)
                        
                        logger.info(f"Creating view {i}/{len(view_statements)}: {view_name}")
                        
                        # Execute the CREATE VIEW statement
                        cursor.execute(statement)
                        conn.commit()
                        
                        logger.info(f"SUCCESS: Created view: {view_name}")
                        successful_views += 1
                        
                    except Exception as e:
                        logger.error(f"FAILED: View {i}: {e}")
                        failed_views += 1
                        # Continue with next view
                        continue
                
                logger.info(f"View creation completed!")
                logger.info(f"Successful: {successful_views}")
                logger.info(f"Failed: {failed_views}")
                
                return successful_views > 0
                
        except Exception as e:
            logger.error(f"Error creating views: {e}")
            return False
    
    def _extract_view_name(self, statement):
        """Extract view name from CREATE VIEW statement."""
        try:
            # Look for "CREATE VIEW DUI.v_viewname"
            lines = statement.split('\n')
            for line in lines:
                if 'CREATE VIEW' in line.upper():
                    parts = line.strip().split()
                    for i, part in enumerate(parts):
                        if part.upper() == 'VIEW' and i + 1 < len(parts):
                            return parts[i + 1]
            return "Unknown"
        except:
            return "Unknown"
    
    def verify_views(self):
        """Verify that views were created successfully."""
        try:
            logger.info("Verifying created views...")
            with pyodbc.connect(self.connection_string) as conn:
                cursor = conn.cursor()
                
                # Query to get all views in DUI schema
                cursor.execute("""
                    SELECT TABLE_NAME 
                    FROM INFORMATION_SCHEMA.VIEWS 
                    WHERE TABLE_SCHEMA = 'DUI'
                    ORDER BY TABLE_NAME
                """)
                
                views = [row[0] for row in cursor.fetchall()]
                
                logger.info(f"Found {len(views)} views in DUI schema")
                
                # Show first 10 views as examples
                if views:
                    logger.info("Sample views created:")
                    for view in views[:10]:
                        logger.info(f"  • {view}")
                    if len(views) > 10:
                        logger.info(f"  ... and {len(views) - 10} more")
                
                return len(views) > 0
                
        except Exception as e:
            logger.error(f"Error verifying views: {e}")
            return False
    
    def run(self):
        """Main execution method."""
        logger.info("DUI Views Creator")
        logger.info("=" * 50)
        
        # Step 1: Test connection
        if not self.test_connection():
            return False
        
        # Step 2: Check SQL file
        if not self.check_sql_file():
            return False
        
        # Step 3: Read SQL file
        view_statements = self.read_sql_file()
        if not view_statements:
            return False
        
        # Step 4: Convert to SQL Server syntax
        view_statements = self.convert_to_sql_server_syntax(view_statements)
        
        # Step 5: Extract view names for dropping
        view_names = []
        for statement in view_statements:
            view_name = self._extract_view_name(statement)
            if view_name != "Unknown":
                view_names.append(view_name)
        
        # Step 6: Drop existing views
        if not self.drop_existing_views(view_names):
            logger.warning("Failed to drop some existing views, but continuing...")
        
        # Step 7: Create views
        if not self.create_views(view_statements):
            return False
        
        # Step 8: Verify views
        if not self.verify_views():
            return False
        
        logger.info("All operations completed successfully!")
        return True

def main():
    """Main function."""
    creator = DUIViewsCreator()
    success = creator.run()
    
    if success:
        print("\n✅ Views creation completed successfully!")
        print("📋 Check 'create_views.log' for detailed information")
    else:
        print("\n❌ Views creation failed!")
        print("📋 Check 'create_views.log' for error details")
        sys.exit(1)

if __name__ == "__main__":
    main() 