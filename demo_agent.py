#!/usr/bin/env python3
"""
Demo script for DUI SQL Agent
Shows the system working with environment configuration.
"""

import json
import os
from dui_sql_agent import DUISQLAgent

def demo_agent():
    """Demonstrate the DUI SQL agent."""
    print("🚔 DUI SQL Agent Demo")
    print("=" * 60)
    print("This demo shows the system working with environment configuration")
    print("=" * 60)
    
    # Show current configuration
    print("\n⚙️  Current Configuration:")
    print("-" * 40)
    model_type = os.getenv("AI_MODEL_TYPE", "mock")
    model_name = os.getenv("AI_MODEL_NAME", "")
    print(f"Model Type: {model_type}")
    if model_name:
        print(f"Model Name: {model_name}")
    
    # Initialize the agent
    print("\n🔧 Initializing agent...")
    try:
        agent = DUISQLAgent()
        print("✅ Agent initialized successfully!")
    except Exception as e:
        print(f"❌ Failed to initialize agent: {e}")
        return
    
    # Demo queries
    demo_queries = [
        "Show me all DUI cases from the last 30 days",
        "Find cases with blood alcohol content above 0.15",
        "List all defendants with multiple DUI offenses",
        "Show officer performance statistics",
        "Find cases with field sobriety test failures"
    ]
    
    print(f"\n🎯 Running {len(demo_queries)} demo queries...")
    print("-" * 60)
    
    for i, query in enumerate(demo_queries, 1):
        print(f"\n📝 Query {i}: {query}")
        print("-" * 40)
        
        result = agent.run_query(query)
        
        if result["success"]:
            print("✅ Query generated successfully!")
            print(f"📊 Model Used: {result['model_used']}")
            print(f"🔍 View Used: {result['view_used']}")
            print(f"🔒 Security: {result['security_note']}")
            print(f"📝 Explanation: {result['explanation']}")
            print(f"\n💻 Generated SQL:")
            print(result['sql_query'])
        else:
            print(f"❌ Query failed: {result['error']}")
        
        print("-" * 40)
    
    # Show available views
    print(f"\n📋 Available Views Summary:")
    views = agent.get_available_views()
    if views:
        print(f"✅ Loaded {len(views)} views from database analysis")
        
        # Show some key views
        key_views = [
            "v_case_summary", "v_evidence_summary", "v_officer_performance",
            "v_defendant_summary", "v_caseheaders", "v_defendants"
        ]
        
        print("\n🔑 Key Views Available:")
        for view_name in key_views:
            if view_name in views:
                view_info = views[view_name]
                description = view_info.get('description', 'No description')
                print(f"  • {view_name}: {description[:60]}...")
    else:
        print("❌ No views available")
    
    print("\n🎉 Demo completed!")
    print("\n💡 To use the interactive interface:")
    print("   python dui_interface.py")
    print("\n💡 To change model configuration:")
    print("   Edit the .env file and set:")
    print("   - AI_MODEL_TYPE=mock (no API needed)")
    print("   - AI_MODEL_TYPE=openai (requires OpenAI API key)")
    print("   - AI_MODEL_TYPE=gemini (requires Google API key - FREE!)")
    print("   - AI_MODEL_TYPE=ollama (requires local Ollama)")
    print("   - AI_MODEL_TYPE=huggingface (requires HuggingFace token)")

if __name__ == "__main__":
    demo_agent() 