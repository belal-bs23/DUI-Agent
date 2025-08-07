#!/usr/bin/env python3
"""
DUI SQL Agent Interface - LangGraph Version
Interactive interface for the LangGraph-based DUI SQL agent.
"""

import json
import os
from dui_sql_agent_langgraph import DUISQLAgentLangGraph

def print_banner():
    """Print the application banner."""
    print("=" * 60)
    print("🚔 DUI SQL Agent - LangGraph Edition")
    print("=" * 60)
    print("Generate SQL queries using organized workflow")
    print("=" * 60)

def print_help():
    """Print help information."""
    print("\n📖 Available Commands:")
    print("  query <your question>  - Generate SQL for your question")
    print("  views                  - Show available database views")
    print("  info <view_name>       - Get info about a specific view")
    print("  test                   - Run a test query")
    print("  config                 - Show current configuration")
    print("  workflow               - Show workflow steps")
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

def show_workflow():
    """Show the LangGraph workflow steps."""
    print("\n🔄 LangGraph Workflow:")
    print("-" * 40)
    workflow_steps = [
        "1. Initialize State - Load schema and analysis data",
        "2. Analyze Query - Understand intent and select views",
        "3. Generate SQL - Use AI model to create query",
        "4. Validate Query - Check SQL syntax and security",
        "5. Finalize Response - Format and return results"
    ]
    
    for step in workflow_steps:
        print(f"  {step}")
    
    print("\n✨ Benefits of LangGraph workflow:")
    print("  • Clear separation of concerns")
    print("  • Better error handling and debugging")
    print("  • State management throughout the process")
    print("  • Easy to extend and modify")
    print("  • Better logging and monitoring")

def run_test_query(agent):
    """Run a test query to demonstrate the system."""
    print("\n🧪 Running test query...")
    test_query = "Show me all DUI cases from the last 30 days"
    print(f"Query: {test_query}")
    
    result = agent.run_query(test_query)
    
    if result["success"]:
        print("✅ Query generated successfully!")
        print(f"\n📊 Model Used: {result['model_used']}")
        print(f"🔍 Views Used: {result['view_used']}")
        print(f"🔒 Security: {result['security_note']}")
        print(f"📝 Explanation: {result['explanation']}")
        print(f"\n💻 Generated SQL:")
        print("-" * 40)
        print(result['sql_query'])
        print("-" * 40)
        
        # Show workflow messages
        print(f"\n🔄 Workflow Messages:")
        for i, message in enumerate(result['messages'], 1):
            content = message.content[:100] + "..." if len(message.content) > 100 else message.content
            print(f"  {i}. {type(message).__name__}: {content}")
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
            print(f"    ... and {len(view_list) - 10} more {view_type} views")

def show_view_info(agent, view_name):
    """Show detailed information about a specific view."""
    view_info = agent.get_view_info(view_name)
    
    if not view_info:
        print(f"❌ View '{view_name}' not found.")
        return
    
    print(f"\n📊 View Information: {view_name}")
    print("-" * 50)
    print(f"Description: {view_info.get('description', 'No description')}")
    print(f"Type: {view_info.get('type', 'Unknown')}")
    
    columns = view_info.get('columns', [])
    if columns:
        print(f"\nColumns ({len(columns)}):")
        for col in columns[:20]:  # Show first 20 columns
            print(f"  • {col}")
        
        if len(columns) > 20:
            print(f"  ... and {len(columns) - 20} more columns")
    
    # Show relationships if available
    relationships = view_info.get('relationships', [])
    if relationships:
        print(f"\nRelationships:")
        for rel in relationships[:5]:  # Show first 5 relationships
            print(f"  • {rel}")
        
        if len(relationships) > 5:
            print(f"  ... and {len(relationships) - 5} more relationships")

def process_query(agent, user_input):
    """Process a user query."""
    # Extract the query from the input
    if user_input.startswith("query "):
        query = user_input[6:].strip()
    else:
        query = user_input.strip()
    
    if not query:
        print("❌ Please provide a query.")
        return
    
    print(f"\n🔍 Processing query: {query}")
    print("-" * 50)
    
    result = agent.run_query(query)
    
    if result["success"]:
        print("✅ Query generated successfully!")
        print(f"📊 Model Used: {result['model_used']}")
        print(f"🔍 Views Used: {result['view_used']}")
        print(f"🔒 Security: {result['security_note']}")
        print(f"📝 Explanation: {result['explanation']}")
        print(f"\n💻 Generated SQL:")
        print("-" * 40)
        print(result['sql_query'])
        print("-" * 40)
        
        # Show workflow summary
        print(f"\n🔄 Workflow Summary:")
        message_count = len(result['messages'])
        print(f"  • Total workflow steps: {message_count}")
        print(f"  • Views selected: {result['view_used']}")
        print(f"  • Model used: {result['model_used']}")
        print(f"  • Status: Success ✅")
    else:
        print(f"❌ Query failed: {result['error']}")
        print(f"\n🔄 Workflow Summary:")
        print(f"  • Status: Failed ❌")
        print(f"  • Error: {result['error']}")

def main():
    """Main function for the interactive interface."""
    print_banner()
    
    # Initialize the LangGraph agent
    print("\n🔧 Initializing LangGraph agent...")
    try:
        agent = DUISQLAgentLangGraph()
        print("✅ LangGraph agent initialized successfully!")
    except Exception as e:
        print(f"❌ Failed to initialize agent: {e}")
        return
    
    print_help()
    
    # Main interaction loop
    while True:
        try:
            user_input = input("\n🚔 DUI Agent> ").strip()
            
            if not user_input:
                continue
            
            # Handle commands
            if user_input.lower() in ['quit', 'exit']:
                print("👋 Goodbye!")
                break
            elif user_input.lower() == 'help':
                print_help()
            elif user_input.lower() == 'config':
                show_configuration()
            elif user_input.lower() == 'workflow':
                show_workflow()
            elif user_input.lower() == 'test':
                run_test_query(agent)
            elif user_input.lower() == 'views':
                show_views(agent)
            elif user_input.startswith('info '):
                view_name = user_input[5:].strip()
                show_view_info(agent, view_name)
            elif user_input.startswith('query ') or not user_input.startswith(('query ', 'info ', 'help', 'config', 'workflow', 'test', 'views')):
                process_query(agent, user_input)
            else:
                print("❌ Unknown command. Type 'help' for available commands.")
                
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    main() 