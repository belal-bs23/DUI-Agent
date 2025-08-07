#!/usr/bin/env python3
"""
Enhanced DUI Database Analysis and View Generation Script
This script runs the comprehensive database analysis and generates enhanced views.
"""

import os
import sys
import subprocess
from pathlib import Path

def activate_venv():
    """Activate the virtual environment."""
    venv_path = Path("venv")
    if not venv_path.exists():
        print("❌ Virtual environment not found. Please create it first.")
        return False
    
    # Set environment variables for virtual environment
    if sys.platform == "win32":
        python_path = venv_path / "Scripts" / "python.exe"
        pip_path = venv_path / "Scripts" / "pip.exe"
    else:
        python_path = venv_path / "bin" / "python"
        pip_path = venv_path / "bin" / "pip"
    
    if not python_path.exists():
        print(f"❌ Python not found in virtual environment: {python_path}")
        return False
    
    # Set environment variables
    os.environ["VIRTUAL_ENV"] = str(venv_path.absolute())
    os.environ["PATH"] = f"{venv_path / 'Scripts' if sys.platform == 'win32' else venv_path / 'bin'}{os.pathsep}{os.environ['PATH']}"
    
    print(f"✅ Virtual environment activated: {venv_path}")
    return True

def install_dependencies():
    """Install required dependencies in the virtual environment."""
    print("\n📦 Installing dependencies...")
    
    try:
        # Install from requirements.txt
        result = subprocess.run([
            sys.executable, "-m", "pip", "install", "-r", "requirements.txt"
        ], capture_output=True, text=True, check=True)
        
        print("✅ Dependencies installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install dependencies: {e}")
        print(f"Error output: {e.stderr}")
        return False

def run_database_analysis():
    """Run the database analysis."""
    print("\n🔍 Running database analysis...")
    
    try:
        result = subprocess.run([
            sys.executable, "db_backup/database_analyzer.py"
        ], capture_output=True, text=True, check=True)
        
        print("✅ Database analysis completed successfully")
        print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Database analysis failed: {e}")
        print(f"Error output: {e.stderr}")
        return False

def run_enhanced_view_generation():
    """Run the enhanced view generation."""
    print("\n🔧 Running enhanced view generation...")
    
    try:
        result = subprocess.run([
            sys.executable, "db_backup/comprehensive_dui_view_generator.py"
        ], capture_output=True, text=True, check=True)
        
        print("✅ Enhanced view generation completed successfully")
        print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Enhanced view generation failed: {e}")
        print(f"Error output: {e.stderr}")
        return False

def check_files():
    """Check if required files exist."""
    print("\n📋 Checking required files...")
    
    required_files = [
        "requirements.txt",
        "db_backup/database_analyzer.py",
        "db_backup/comprehensive_dui_view_generator.py"
    ]
    
    missing_files = []
    for file_path in required_files:
        if not Path(file_path).exists():
            missing_files.append(file_path)
    
    if missing_files:
        print(f"❌ Missing files: {', '.join(missing_files)}")
        return False
    
    print("✅ All required files found")
    return True

def check_database_connection():
    """Test database connection."""
    print("\n🔌 Testing database connection...")
    
    try:
        import pyodbc
        
        # Connection details
        DRIVER = "ODBC Driver 17 for SQL Server"
        SERVER = "localhost\\SQLEXPRESS"
        DATABASE = "LEADRS_DUI_STAGE"
        conn_str = f"DRIVER={{{DRIVER}}};SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection=yes"
        
        # Test connection
        connection = pyodbc.connect(conn_str)
        cursor = connection.cursor()
        
        # Test a simple query
        cursor.execute("SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'DUI'")
        table_count = cursor.fetchone()[0]
        
        cursor.close()
        connection.close()
        
        print(f"✅ Database connection successful. Found {table_count} tables.")
        return True
        
    except Exception as e:
        print(f"❌ Database connection failed: {e}")
        print("\nPlease check:")
        print("1. SQL Server is running")
        print("2. Database 'LEADRS_DUI_STAGE' exists")
        print("3. Windows Authentication is enabled")
        print("4. ODBC Driver 17 for SQL Server is installed")
        return False

def main():
    """Main function to run the complete enhanced analysis."""
    print("Enhanced DUI Database Analysis and View Generation")
    print("=" * 60)
    
    # Step 1: Check files
    if not check_files():
        print("❌ Setup failed: Missing required files")
        return
    
    # Step 2: Activate virtual environment
    if not activate_venv():
        print("❌ Setup failed: Could not activate virtual environment")
        return
    
    # Step 3: Install dependencies
    if not install_dependencies():
        print("❌ Setup failed: Could not install dependencies")
        return
    
    # Step 4: Test database connection
    if not check_database_connection():
        print("❌ Setup failed: Database connection failed")
        return
    
    # Step 5: Run database analysis
    if not run_database_analysis():
        print("❌ Analysis failed: Database analysis failed")
        return
    
    # Step 6: Run enhanced view generation
    if not run_enhanced_view_generation():
        print("❌ View generation failed: Enhanced view generation failed")
        return
    
    # Success summary
    print("\n" + "=" * 60)
    print("🎉 ENHANCED ANALYSIS COMPLETE!")
    print("=" * 60)
    
    print("\n📁 Generated Files:")
    generated_files = [
        "db_backup/database_analysis.json",
        "db_backup/enhanced_dui_views.sql",
        "db_backup/enhanced_dui_view_schema.json"
    ]
    
    for file_path in generated_files:
        if Path(file_path).exists():
            print(f"  ✅ {file_path}")
        else:
            print(f"  ❌ {file_path} (not found)")
    
    print("\n🎯 Next Steps:")
    print("1. Review database_analysis.json for detailed database structure")
    print("2. Review enhanced_dui_views.sql for generated views")
    print("3. Review enhanced_dui_view_schema.json for view metadata")
    print("4. Execute the SQL file in your database:")
    print("   sqlcmd -S localhost\\SQLEXPRESS -d LEADRS_DUI_STAGE -i db_backup/enhanced_dui_views.sql")
    print("5. Update the AI agent to use the enhanced views")
    print("6. Test the system with the new comprehensive views")
    
    print("\n🔒 Security Features Implemented:")
    print("  - Sensitive data exclusion (SSN, addresses, phone numbers)")
    print("  - Comprehensive column descriptions")
    print("  - View-based access control")
    print("  - Active records only")
    print("  - Relationship-aware view generation")
    
    print("\n📊 Analysis Features:")
    print("  - Complete database structure analysis")
    print("  - Table relationship mapping")
    print("  - Column content analysis")
    print("  - Data pattern recognition")
    print("  - Automated description generation")

if __name__ == "__main__":
    main() 