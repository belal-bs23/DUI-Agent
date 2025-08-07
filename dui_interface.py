#!/usr/bin/env python3
"""
DUI SQL Agent Interface
Interactive interface for the DUI SQL agent using environment configuration.
"""

import json
import os
from dui_sql_agent import DUISQLAgent

def print_banner():
    """Print the application banner."""
    print("=" * 60)
    print("🚔 DUI SQL Agent")
    print("=" * 60)
    print("Generate SQL queries for DUI database")
    print("=" * 60)

def print_help():
    """Print help information."""
    print("\n📖 Available Commands:")
    print("  query <your question>  - Generate SQL for your question")
    print("  views                  - Show available database views")
    print("  info <view_name>       - Get info about a specific view")
    print("  test                   - Run a test query")
    print("  config                 - Show current configuration")
    print("  help                   - Show this help")
    print("  quit/exit              - Exit the application")
    
    print("\n🎯 Example Queries:")
    print("  query Show me all DUI cases from last month")
    print("  query Find cases with blood alcohol content above 0.15")
    print("  query List all defendants with multiple DUI offenses")
    print("  query Show officer performance statistics")
    print("  query Find cases with field sobriety test failures")

def show_configuration():
    """Show current configuration."""
    print("\n⚙️  Current Configuration:")
    print("-" * 40)
    model_type = os.getenv("AI_MODEL_TYPE", "mock")
    model_name = os.getenv("AI_MODEL_NAME", "")
    api_key = os.getenv("AI_API_KEY", "")
    
    print(f"Model Type: {model_type}")
    if model_name:
        print(f"Model Name: {model_name}")
    if api_key:
        print(f"API Key: {api_key[:10]}...")
    else:
        print("API Key: Not set")
    
    print(f"\n💡 To change configuration, edit the .env file")

def run_test_query(agent):
    """Run a test query to demonstrate the system."""
    print("\n🧪 Running test query...")
    test_query = "Show me all DUI cases from the last 30 days"
    print(f"Query: {test_query}")
    
    result = agent.run_query(test_query)
    
    if result["success"]:
        print("✅ Query generated successfully!")
        print(f"\n📊 Model Used: {result['model_used']}")
        print(f"🔍 View Used: {result['view_used']}")
        print(f"🔒 Security: {result['security_note']}")
        print(f"📝 Explanation: {result['explanation']}")
        print(f"\n💻 Generated SQL:")
        print("-" * 40)
        print(result['sql_query'])
        print("-" * 40)
    else:
        print(f"❌ Query failed: {result['error']}")

def show_views(agent):
    """Show available database views."""
    views = agent.get_available_views()
    
    if not views:
        print("❌ No views available. Please check if schema files exist.")
        return
    
    print(f"\n📋 Available Views ({len(views)} total):")
    print("-" * 60)
    
    # Group views by type
    view_types = {}
    for view_name, view_info in views.items():
        view_type = view_info.get('type', 'General')
        if view_type not in view_types:
            view_types[view_type] = []
        view_types[view_type].append((view_name, view_info))
    
    for view_type, view_list in view_types.items():
        print(f"\n🔹 {view_type} Views:")
        for view_name, view_info in view_list[:10]:  # Show first 10 of each type
            description = view_info.get('description', 'No description')
            print(f"  • {view_name}: {description[:60]}...")
        
        if len(view_list) > 10:
            print(f"  ... and {len(view_list) - 10} more")

def show_view_info(agent, view_name):
    """Show detailed information about a specific view."""
    view_info = agent.get_view_info(view_name)
    
    if not view_info or 'error' in view_info:
        print(f"❌ View '{view_name}' not found")
        return
    
    print(f"\n📊 View Information: {view_name}")
    print("-" * 50)
    print(f"Description: {view_info.get('description', 'No description')}")
    print(f"Type: {view_info.get('type', 'Unknown')}")
    print(f"Security Level: {view_info.get('security_level', 'Standard')}")
    
    columns = view_info.get('columns', {})
    if columns:
        print(f"\n📋 Columns ({len(columns)}):")
        for col_name, col_info in list(columns.items())[:10]:  # Show first 10 columns
            col_type = col_info.get('type', 'Unknown')
            col_desc = col_info.get('description', 'No description')
            print(f"  • {col_name} ({col_type}): {col_desc[:50]}...")
        
        if len(columns) > 10:
            print(f"  ... and {len(columns) - 10} more columns")

def main():
    """Main application loop."""
    print_banner()
    
    # Show current configuration
    show_configuration()
    
    # Initialize the agent
    print("\n🔧 Initializing agent...")
    try:
        agent = DUISQLAgent()
        print("✅ Agent initialized successfully!")
        print(f"Model Type: {agent.model_type}")
        print(f"Model Name: {agent.model_name}")
        print(f"API Key: {agent.api_key[:10]}...")
        print(agent.llm)
    except Exception as e:
        print(f"❌ Failed to initialize agent: {e}")
        return
    
    print_help()
    
    # Main command loop
    while True:
        try:
            command = input("\n🎯 Enter command: ").strip()
            
            if not command:
                continue
            
            if command.lower() in ['quit', 'exit', 'q']:
                print("👋 Goodbye!")
                break
            
            elif command.lower() == 'help':
                print_help()
            
            elif command.lower() == 'config':
                show_configuration()
            
            elif command.lower() == 'test':
                run_test_query(agent)
            
            elif command.lower() == 'views':
                show_views(agent)
            
            elif command.lower().startswith('info '):
                view_name = command[5:].strip()
                if view_name:
                    show_view_info(agent, view_name)
                else:
                    print("❌ Please specify a view name: info <view_name>")
            
            elif command.lower().startswith('query '):
                user_query = command[6:].strip()
                if user_query:
                    print(f"\n🔍 Processing query: {user_query}")
                    result = agent.run_query(user_query)
                    
                    if result["success"]:
                        print("✅ Query generated successfully!")
                        print(f"\n📊 Model Used: {result['model_used']}")
                        print(f"🔍 View Used: {result['view_used']}")
                        print(f"🔒 Security: {result['security_note']}")
                        print(f"📝 Explanation: {result['explanation']}")
                        print(f"\n💻 Generated SQL:")
                        print("-" * 40)
                        print(result['sql_query'])
                        print("-" * 40)
                    else:
                        print(f"❌ Query failed: {result['error']}")
                else:
                    print("❌ Please enter a query: query <your question>")
            
            else:
                print("❌ Unknown command. Type 'help' for available commands.")
                
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    main() 