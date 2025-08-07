#!/usr/bin/env python3
"""
Setup script for DUI Views Creation
Helps configure and run the views creation process.
"""

import os
import sys
from pathlib import Path

def check_prerequisites():
    """Check if all prerequisites are met."""
    print("🔍 Checking prerequisites...")
    
    # Check if SQL file exists
    sql_file = Path("db_backup/comprehensive_dui_views.sql")
    if not sql_file.exists():
        print("❌ SQL file not found: db_backup/comprehensive_dui_views.sql")
        print("   Make sure you have run the database analysis first.")
        return False
    
    print(f"✅ SQL file found: {sql_file} ({sql_file.stat().st_size:,} bytes)")
    
    # Check if pyodbc is available
    try:
        import pyodbc
        print("✅ pyodbc module available")
    except ImportError:
        print("❌ pyodbc module not found")
        print("   Install it with: pip install pyodbc")
        return False
    
    return True

def setup_environment():
    """Set up environment variables for database connection."""
    print("\n⚙️  Database Configuration")
    print("=" * 40)
    
    # Check if .env file exists
    env_file = Path(".env")
    if env_file.exists():
        print("✅ .env file found")
        load_env_file(env_file)
    else:
        print("📝 No .env file found. Let's create one...")
        create_env_file()
    
    # Show current configuration
    print("\n📋 Current Configuration:")
    print(f"  Server: {os.getenv('DB_SERVER', 'localhost')}")
    print(f"  Database: {os.getenv('DB_DATABASE', 'LEADRS_DUI_STAGE')}")
    print(f"  Username: {os.getenv('DB_USERNAME', '(Windows Auth)')}")
    print(f"  Password: {'*' * len(os.getenv('DB_PASSWORD', '')) if os.getenv('DB_PASSWORD') else '(Windows Auth)'}")

def load_env_file(env_file):
    """Load environment variables from .env file."""
    try:
        with open(env_file, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    os.environ[key.strip()] = value.strip()
    except Exception as e:
        print(f"⚠️  Warning: Could not load .env file: {e}")

def create_env_file():
    """Create a new .env file with user input."""
    print("\nPlease provide your database configuration:")
    
    server = input("Database Server (default: localhost): ").strip() or "localhost"
    database = input("Database Name (default: LEADRS_DUI_STAGE): ").strip() or "LEADRS_DUI_STAGE"
    
    auth_type = input("Authentication type (1=Windows, 2=SQL Server): ").strip()
    
    if auth_type == "2":
        username = input("Username: ").strip()
        password = input("Password: ").strip()
    else:
        username = ""
        password = ""
    
    # Create .env file
    env_content = f"""# Database Configuration for DUI Views Creator
DB_SERVER={server}
DB_DATABASE={database}
DB_USERNAME={username}
DB_PASSWORD={password}
"""
    
    try:
        with open(".env", 'w') as f:
            f.write(env_content)
        print("✅ .env file created successfully!")
    except Exception as e:
        print(f"❌ Failed to create .env file: {e}")

def run_views_creation():
    """Run the views creation process."""
    print("\n🚀 Starting Views Creation Process")
    print("=" * 40)
    
    try:
        from create_dui_views import DUIViewsCreator
        creator = DUIViewsCreator()
        success = creator.run()
        
        if success:
            print("\n🎉 Views creation completed successfully!")
            print("📋 Check 'create_views.log' for detailed information")
        else:
            print("\n❌ Views creation failed!")
            print("📋 Check 'create_views.log' for error details")
            return False
            
    except Exception as e:
        print(f"❌ Error running views creation: {e}")
        return False
    
    return True

def main():
    """Main function."""
    print("🚔 DUI Views Creator Setup")
    print("=" * 50)
    
    # Check prerequisites
    if not check_prerequisites():
        print("\n❌ Prerequisites not met. Please fix the issues above.")
        sys.exit(1)
    
    # Setup environment
    setup_environment()
    
    # Ask user if they want to proceed
    print("\n" + "=" * 40)
    proceed = input("Do you want to proceed with creating the views? (y/N): ").strip().lower()
    
    if proceed in ['y', 'yes']:
        success = run_views_creation()
        if not success:
            sys.exit(1)
    else:
        print("👋 Setup cancelled. You can run 'python create_dui_views.py' later.")
    
    print("\n✅ Setup completed!")

if __name__ == "__main__":
    main() 