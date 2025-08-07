#!/usr/bin/env python3
"""
DUI SQL Agent Setup
==================

Comprehensive setup script for the DUI SQL Agent.
Handles environment configuration, database views setup, and system verification.
"""

import os
import sys
import json
import subprocess
from pathlib import Path
from dotenv import load_dotenv

def check_python_version():
    """Check if Python version is compatible."""
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 or higher is required")
        return False
    print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor} detected")
    return True

def check_dependencies():
    """Check if required dependencies are installed."""
    required_packages = [
        'langchain', 'langchain-core', 'langchain-openai', 'langgraph',
        'openai', 'pydantic', 'pyodbc', 'python-dotenv'
    ]
    
    missing_packages = []
    for package in required_packages:
        try:
            __import__(package.replace('-', '_'))
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        print(f"❌ Missing packages: {', '.join(missing_packages)}")
        print("Run: pip install -r requirements.txt")
        return False
    
    print("✅ All required packages are installed")
    return True

def create_env_template():
    """Create a .env template file."""
    env_template = """# Database Configuration
DB_SERVER=localhost\\SQLEXPRESS
DB_DATABASE=LEADRS_DUI_STAGE
DB_USERNAME=
DB_PASSWORD=

# AI Model Configuration
OPENAI_API_KEY=your_openai_api_key_here
GOOGLE_API_KEY=your_google_api_key_here

# Optional: Model Settings
OPENAI_MODEL=gpt-4
GOOGLE_MODEL=gemini-pro
"""
    
    env_file = Path('.env')
    if not env_file.exists():
        with open(env_file, 'w') as f:
            f.write(env_template)
        print("✅ Created .env template file")
        print("⚠️  Please update .env with your actual API keys and database credentials")
    else:
        print("✅ .env file already exists")

def show_current_config():
    """Show current configuration."""
    load_dotenv('.env')
    
    print("\n📋 Current Configuration:")
    print("-" * 40)
    
    # Database config
    db_server = os.getenv('DB_SERVER', 'Not set')
    db_database = os.getenv('DB_DATABASE', 'Not set')
    db_username = os.getenv('DB_USERNAME', 'Not set')
    db_password = os.getenv('DB_PASSWORD', 'Not set')
    
    print(f"Database Server: {db_server}")
    print(f"Database Name: {db_database}")
    print(f"Database Username: {'Set' if db_username else 'Not set'}")
    print(f"Database Password: {'Set' if db_password else 'Not set'}")
    
    # AI config
    openai_key = os.getenv('OPENAI_API_KEY', 'Not set')
    google_key = os.getenv('GOOGLE_API_KEY', 'Not set')
    openai_model = os.getenv('OPENAI_MODEL', 'gpt-4')
    google_model = os.getenv('GOOGLE_MODEL', 'gemini-pro')
    
    print(f"OpenAI API Key: {'Set' if openai_key != 'Not set' else 'Not set'}")
    print(f"Google API Key: {'Set' if google_key != 'Not set' else 'Not set'}")
    print(f"OpenAI Model: {openai_model}")
    print(f"Google Model: {google_model}")

def test_database_connection():
    """Test database connection."""
    try:
        import pyodbc
        load_dotenv('.env')
        
        server = os.getenv('DB_SERVER', 'localhost\\SQLEXPRESS')
        database = os.getenv('DB_DATABASE', 'LEADRS_DUI_STAGE')
        username = os.getenv('DB_USERNAME', '')
        password = os.getenv('DB_PASSWORD', '')
        
        if username and password:
            conn_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
        else:
            conn_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes'
        
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        
        # Test basic query
        cursor.execute("SELECT COUNT(*) FROM INFORMATION_SCHEMA.VIEWS WHERE TABLE_SCHEMA = 'DUI'")
        view_count = cursor.fetchone()[0]
        
        conn.close()
        
        print(f"✅ Database connection successful")
        print(f"✅ Found {view_count} DUI views in database")
        return True
        
    except Exception as e:
        print(f"❌ Database connection failed: {e}")
        print("💡 Make sure SQL Server is running and credentials are correct")
        return False

def setup_database_views():
    """Setup database views if needed."""
    try:
        import pyodbc
        load_dotenv('.env')
        
        server = os.getenv('DB_SERVER', 'localhost\\SQLEXPRESS')
        database = os.getenv('DB_DATABASE', 'LEADRS_DUI_STAGE')
        username = os.getenv('DB_USERNAME', '')
        password = os.getenv('DB_PASSWORD', '')
        
        if username and password:
            conn_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
        else:
            conn_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes'
        
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        
        # Check if views exist
        cursor.execute("SELECT COUNT(*) FROM INFORMATION_SCHEMA.VIEWS WHERE TABLE_SCHEMA = 'DUI'")
        view_count = cursor.fetchone()[0]
        
        if view_count > 0:
            print(f"✅ Database views already exist ({view_count} views)")
            conn.close()
            return True
        
        print("⚠️  No DUI views found. Would you like to create them? (y/n): ", end="")
        response = input().lower().strip()
        
        if response != 'y':
            print("⏭️  Skipping view creation")
            conn.close()
            return False
        
        # Check if SQL file exists
        sql_file = Path("db_backup/comprehensive_dui_views.sql")
        if not sql_file.exists():
            print("❌ SQL file not found: db_backup/comprehensive_dui_views.sql")
            print("💡 Please ensure the SQL file exists before creating views")
            conn.close()
            return False
        
        print("🔧 Creating database views...")
        
        # Read and execute SQL file
        with open(sql_file, 'r', encoding='utf-8') as f:
            sql_content = f.read()
        
        # Split into individual statements
        statements = [stmt.strip() for stmt in sql_content.split(';') if stmt.strip()]
        
        for i, statement in enumerate(statements, 1):
            if statement:
                try:
                    cursor.execute(statement)
                    print(f"  ✅ Statement {i}/{len(statements)} executed")
                except Exception as e:
                    print(f"  ⚠️  Statement {i} failed: {e}")
        
        conn.commit()
        conn.close()
        
        print("✅ Database views created successfully")
        return True
        
    except Exception as e:
        print(f"❌ View setup failed: {e}")
        return False

def test_ai_connection():
    """Test AI model connections."""
    load_dotenv('.env')
    
    openai_key = os.getenv('OPENAI_API_KEY')
    google_key = os.getenv('GOOGLE_API_KEY')
    
    if not openai_key and not google_key:
        print("⚠️  No AI API keys configured")
        print("💡 Set OPENAI_API_KEY or GOOGLE_API_KEY in .env file")
        return False
    
    if openai_key:
        try:
            from openai import OpenAI
            client = OpenAI(api_key=openai_key)
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": "Hello"}],
                max_tokens=5
            )
            print("✅ OpenAI connection successful")
            return True
        except Exception as e:
            print(f"❌ OpenAI connection failed: {e}")
    
    if google_key:
        try:
            import google.generativeai as genai
            genai.configure(api_key=google_key)
            model = genai.GenerativeModel('gemini-pro')
            response = model.generate_content("Hello")
            print("✅ Google AI connection successful")
            return True
        except Exception as e:
            print(f"❌ Google AI connection failed: {e}")
    
    return False

def run_comprehensive_test():
    """Run comprehensive system test."""
    print("\n🧪 Running comprehensive system test...")
    print("=" * 50)
    
    tests = [
        ("Python Version", check_python_version),
        ("Dependencies", check_dependencies),
        ("Database Connection", test_database_connection),
        ("AI Connection", test_ai_connection),
    ]
    
    results = []
    for test_name, test_func in tests:
        print(f"\n🔍 Testing: {test_name}")
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"❌ Test failed with error: {e}")
            results.append((test_name, False))
    
    print("\n📊 Test Results:")
    print("-" * 30)
    passed = 0
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{test_name}: {status}")
        if result:
            passed += 1
    
    print(f"\n🎯 Overall: {passed}/{len(results)} tests passed")
    
    if passed == len(results):
        print("🎉 All tests passed! System is ready to use.")
        return True
    else:
        print("⚠️  Some tests failed. Please fix the issues above.")
        return False

def main():
    """Main setup function."""
    print("🚀 DUI SQL Agent Setup")
    print("=" * 30)
    
    if len(sys.argv) > 1:
        command = sys.argv[1].lower()
        
        if command == "config":
            show_current_config()
        elif command == "test":
            run_comprehensive_test()
        elif command == "views":
            setup_database_views()
        elif command == "env":
            create_env_template()
        elif command == "db":
            test_database_connection()
        elif command == "ai":
            test_ai_connection()
        else:
            print(f"❌ Unknown command: {command}")
            show_help()
    else:
        # Interactive setup
        print("\nChoose an option:")
        print("1. Show current configuration")
        print("2. Create .env template")
        print("3. Test database connection")
        print("4. Setup database views")
        print("5. Test AI connections")
        print("6. Run comprehensive test")
        print("7. Exit")
        
        while True:
            try:
                choice = input("\nEnter your choice (1-7): ").strip()
                
                if choice == "1":
                    show_current_config()
                elif choice == "2":
                    create_env_template()
                elif choice == "3":
                    test_database_connection()
                elif choice == "4":
                    setup_database_views()
                elif choice == "5":
                    test_ai_connection()
                elif choice == "6":
                    run_comprehensive_test()
                elif choice == "7":
                    print("👋 Goodbye!")
                    break
                else:
                    print("❌ Invalid choice. Please enter 1-7.")
                    
            except KeyboardInterrupt:
                print("\n👋 Setup interrupted. Goodbye!")
                break

def show_help():
    """Show help information."""
    print("""
Usage: python setup.py [command]

Commands:
  config    - Show current configuration
  test      - Run comprehensive system test
  views     - Setup database views
  env       - Create .env template
  db        - Test database connection
  ai        - Test AI connections

Examples:
  python setup.py config
  python setup.py test
  python setup.py views
""")

if __name__ == "__main__":
    main()
