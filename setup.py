#!/usr/bin/env python3
"""
Setup script for DUI SQL Agent System
"""

import os
import sys
from pathlib import Path

def create_env_file():
    """Create a .env file template."""
    env_content = """# AI Model Configuration
AI_MODEL_TYPE=mock
AI_MODEL_NAME=
AI_API_KEY=

# OpenAI Configuration (if using OpenAI models)
OPENAI_API_KEY=your-openai-api-key-here

# Database Configuration (if needed for direct connection)
DB_DRIVER=ODBC Driver 17 for SQL Server
DB_SERVER=localhost\\SQLEXPRESS
DB_NAME=LEADRS_DUI_STAGE

# Model Configuration Examples:
# AI_MODEL_TYPE=mock (no API needed, for testing)
# AI_MODEL_TYPE=openai (requires OpenAI API key)
# AI_MODEL_TYPE=ollama (requires local Ollama installation)
# AI_MODEL_TYPE=huggingface (requires HuggingFace API token)
"""
    
    env_path = Path(".env")
    if not env_path.exists():
        with open(env_path, "w") as f:
            f.write(env_content)
        print("✅ Created .env file template")
        print("⚠️  Please update .env with your OpenAI API key")
    else:
        print("ℹ️  .env file already exists")

def check_dependencies():
    """Check if required dependencies are installed."""
    required_packages = [
        "langchain",
        "langchain_openai", 
        "langgraph",
        "openai",
        "pydantic",
        "python-dotenv",
        "pyodbc"
    ]
    
    missing_packages = []
    for package in required_packages:
        try:
            if package == "python-dotenv":
                __import__("dotenv")
            else:
                __import__(package.replace("-", "_"))
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        print(f"❌ Missing packages: {', '.join(missing_packages)}")
        print("Run: pip install -r requirements.txt")
        return False
    else:
        print("✅ All required packages are installed")
        return True

def check_files():
    """Check if required files exist."""
    required_files = [
        "db_backup/schema_dui.json",
        "db_backup/comprehensive_dui_view_generator.py",
        "dui_sql_agent.py",
        "dui_interface.py"
    ]
    
    missing_files = []
    for file_path in required_files:
        if not Path(file_path).exists():
            missing_files.append(file_path)
    
    if missing_files:
        print(f"❌ Missing files: {', '.join(missing_files)}")
        return False
    else:
        print("✅ All required files are present")
        return True

def generate_views():
    """Generate the secure views for the DUI database."""
    try:
        print("\n🔄 Generating secure views...")
        from db_backup.comprehensive_dui_view_generator import ComprehensiveDUIViewGenerator
        generator = ComprehensiveDUIViewGenerator()
        generator.generate_all_views()
        print("✅ Views generated successfully")
        return True
    except Exception as e:
        print(f"❌ Error generating views: {e}")
        return False

def test_system():
    """Test the system with a simple query."""
    try:
        print("\n🧪 Testing system...")
        from dui_sql_agent import DUISQLAgent
        
        # Initialize the agent
        agent = DUISQLAgent()
        
        test_query = "Show me all DUI cases from the last 30 days"
        result = agent.run_query(test_query)
        
        if result and "sql_query" in result:
            print("✅ System test passed")
            print(f"Generated SQL: {result['sql_query'][:100]}...")
        else:
            print(f"❌ System test failed: {result}")
            return False
        
        return True
    except Exception as e:
        print(f"❌ System test failed: {e}")
        return False

def main():
    """Main setup function."""
    print("DUI SQL Agent System Setup")
    print("=" * 40)
    
    # Step 1: Check files
    print("\n1. Checking files...")
    if not check_files():
        print("❌ Setup failed: Missing required files")
        return
    
    # Step 2: Check dependencies
    print("\n2. Checking dependencies...")
    if not check_dependencies():
        print("❌ Setup failed: Missing dependencies")
        return
    
    # Step 3: Create .env file
    print("\n3. Setting up environment...")
    create_env_file()
    
    # Step 4: Generate views
    print("\n4. Generating secure views...")
    if not generate_views():
        print("⚠️  View generation failed, but you can continue")
    
    # Step 5: Test system
    print("\n5. Testing system...")
    if not test_system():
        print("⚠️  System test failed, but you can continue")
    
    print("\n🎉 Setup complete!")
    print("\nNext steps:")
    print("1. Update .env file with your OpenAI API key")
    print("2. Run: python dui_interface.py")
    print("3. Or test with: python dui_interface.py test")
    print("\nFor help, type 'help' in the interface")

if __name__ == "__main__":
    main() 