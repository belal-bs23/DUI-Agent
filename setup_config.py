#!/usr/bin/env python3
"""
Configuration Setup Script for DUI SQL Agent
Helps set up the proper configuration for different AI models.
"""

import os
import sys
from pathlib import Path

def create_env_file():
    """Create or update the .env file with proper configuration."""
    env_content = """# AI Model Configuration
# Choose one of the following model types:
AI_MODEL_TYPE=mock
# AI_MODEL_TYPE=openai
# AI_MODEL_TYPE=gemini
# AI_MODEL_TYPE=ollama
# AI_MODEL_TYPE=huggingface

# Model-specific configuration
AI_MODEL_NAME=gpt-4
AI_API_KEY=your-api-key-here

# OpenAI Configuration (if using OpenAI models)
OPENAI_API_KEY=your-openai-api-key-here

# Database Configuration (if needed for direct connection)
DB_DRIVER=ODBC Driver 17 for SQL Server
DB_SERVER=localhost\\SQLEXPRESS
DB_NAME=LEADRS_DUI_STAGE

# Configuration Guide:
# 1. For testing (no API needed): AI_MODEL_TYPE=mock
# 2. For OpenAI: AI_MODEL_TYPE=openai, set OPENAI_API_KEY
# 3. For Gemini: AI_MODEL_TYPE=gemini, set AI_API_KEY
# 4. For Ollama: AI_MODEL_TYPE=ollama, install Ollama locally
# 5. For HuggingFace: AI_MODEL_TYPE=huggingface, set AI_API_KEY
"""
    
    env_path = Path(".env")
    
    if env_path.exists():
        print("⚠️  .env file already exists")
        print("Current configuration:")
        with open(env_path, 'r') as f:
            print(f.read())
        
        response = input("\nDo you want to overwrite it? (y/N): ")
        if response.lower() != 'y':
            print("Configuration not changed.")
            return
    
    with open(env_path, "w") as f:
        f.write(env_content)
    
    print("✅ Created .env file template")
    print("⚠️  Please update .env with your actual API keys")

def show_current_config():
    """Show the current configuration."""
    print("\n📋 Current Configuration:")
    print("-" * 40)
    
    # Load from .env if it exists
    env_path = Path(".env")
    if env_path.exists():
        from dotenv import load_dotenv
        load_dotenv()
    
    model_type = os.getenv("AI_MODEL_TYPE", "mock")
    model_name = os.getenv("AI_MODEL_NAME", "")
    api_key = os.getenv("AI_API_KEY", "")
    openai_key = os.getenv("OPENAI_API_KEY", "")
    
    print(f"Model Type: {model_type}")
    print(f"Model Name: {model_name}")
    print(f"API Key Set: {'Yes' if api_key and api_key != 'your-api-key-here' else 'No'}")
    print(f"OpenAI Key Set: {'Yes' if openai_key and openai_key != 'your-openai-api-key-here' else 'No'}")

def test_configuration():
    """Test the current configuration."""
    print("\n🧪 Testing Configuration:")
    print("-" * 40)
    
    # Load environment
    from dotenv import load_dotenv
    load_dotenv()
    
    model_type = os.getenv("AI_MODEL_TYPE", "mock")
    
    if model_type == "mock":
        print("✅ Mock model - no API needed")
        print("   This is perfect for testing the system")
        return True
    
    elif model_type == "openai":
        api_key = os.getenv("OPENAI_API_KEY", "")
        if not api_key or api_key == "your-openai-api-key-here":
            print("❌ OpenAI API key not set")
            print("   Please set OPENAI_API_KEY in your .env file")
            return False
        else:
            print("✅ OpenAI API key is set")
            print("   Note: You may still hit rate limits with premium subscription")
            return True
    
    elif model_type == "gemini":
        api_key = os.getenv("AI_API_KEY", "")
        if not api_key or api_key == "your-api-key-here":
            print("❌ Gemini API key not set")
            print("   Please set AI_API_KEY in your .env file")
            return False
        else:
            print("✅ Gemini API key is set")
            return True
    
    else:
        print(f"⚠️  Unknown model type: {model_type}")
        return False

def recommend_configuration():
    """Recommend the best configuration based on the situation."""
    print("\n💡 Configuration Recommendations:")
    print("-" * 40)
    
    print("1. 🧪 For Testing (Recommended):")
    print("   AI_MODEL_TYPE=mock")
    print("   - No API key needed")
    print("   - Perfect for testing the workflow")
    print("   - No rate limits or costs")
    
    print("\n2. 🚀 For Production with OpenAI:")
    print("   AI_MODEL_TYPE=openai")
    print("   OPENAI_API_KEY=your-actual-key")
    print("   - Best for production use")
    print("   - Note: Premium subscription still has rate limits")
    
    print("\n3. 🔄 For Rate Limit Issues:")
    print("   - Switch to mock model for testing")
    print("   - Use OpenAI with proper rate limiting")
    print("   - Consider using Ollama for local models")

def main():
    """Main configuration setup function."""
    print("🔧 DUI SQL Agent Configuration Setup")
    print("=" * 50)
    
    while True:
        print("\n📋 Available Options:")
        print("1. Create/Update .env file")
        print("2. Show current configuration")
        print("3. Test configuration")
        print("4. Show recommendations")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == "1":
            create_env_file()
        elif choice == "2":
            show_current_config()
        elif choice == "3":
            test_configuration()
        elif choice == "4":
            recommend_configuration()
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter 1-5.")

if __name__ == "__main__":
    main() 