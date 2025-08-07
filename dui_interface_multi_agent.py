#!/usr/bin/env python3
"""
DUI Multi-Agent Interface
Simple interface for the multi-agent SQL generation system.
"""

import json
import sys
from dui_multi_agent_system import get_multi_agent_system

def print_banner():
    """Print the system banner."""
    print("🚀 DUI Multi-Agent SQL System")
    print("=" * 50)
    print("Multi-agent system with optimized context usage")
    print("Context reduction: 100KB+ → ~25KB (~75% reduction)")
    print("=" * 50)

def print_system_status(system):
    """Print system status."""
    status = system.get_system_status()
    print(f"\n📊 System Status: {status['system_status']}")
    print(f"🔧 Agents Loaded: {status['agents_loaded']}")
    print(f"📁 Total Views: {status['data_manager']['total_views']}")
    print(f"💾 Cache Hit Ratio: {status['data_manager']['cache_hit_ratio']}")
    print(f"📉 Context Reduction: {status['context_optimization']['reduction_percentage']}")

def print_result(result):
    """Print query result in a formatted way."""
    print(f"\n{'='*60}")
    print(f"📋 QUERY RESULT")
    print(f"{'='*60}")
    
    # Basic info
    print(f"✅ Success: {result.get('success', False)}")
    print(f"🔍 Query: {result.get('user_query', 'N/A')}")
    print(f"✅ Valid: {result.get('is_valid', False)}")
    
    # Context usage
    context_usage = result.get('context_usage', {})
    print(f"\n📊 Context Usage:")
    print(f"  • Query Analyzer: {context_usage.get('query_analyzer', 'N/A')}")
    print(f"  • View Selector: {context_usage.get('view_selector', 'N/A')}")
    print(f"  • SQL Generator: {context_usage.get('sql_generator', 'N/A')}")
    print(f"  • Validator: {context_usage.get('validator', 'N/A')}")
    print(f"  • Total: {context_usage.get('total_estimated', 'N/A')}")
    print(f"  • Views Used: {context_usage.get('views_used', 0)}")
    
    # Query analysis
    analysis = result.get('query_analysis', {})
    if analysis:
        print(f"\n🔍 Query Analysis:")
        print(f"  • Intent: {analysis.get('intent', 'N/A')}")
        print(f"  • Type: {analysis.get('query_type', 'N/A')}")
        print(f"  • Complexity: {analysis.get('complexity', 'N/A')}")
        print(f"  • Keywords: {', '.join(analysis.get('keywords', []))}")
    
    # View selection
    view_selection = result.get('view_selection', {})
    if view_selection:
        print(f"\n🎯 View Selection:")
        print(f"  • Selected Views: {', '.join(view_selection.get('selected_views', []))}")
        print(f"  • Reasoning: {view_selection.get('reasoning', 'N/A')}")
    
    # SQL generation
    sql_gen = result.get('sql_generation', {})
    if sql_gen:
        print(f"\n⚙️ SQL Generation:")
        print(f"  • Success: {sql_gen.get('success', False)}")
        print(f"  • Model: {sql_gen.get('model_used', 'N/A')}")
        print(f"  • Explanation: {sql_gen.get('explanation', 'N/A')}")
    
    # Validation
    validation = result.get('validation', {})
    if validation:
        print(f"\n✅ Validation:")
        print(f"  • Valid: {validation.get('is_valid', False)}")
        print(f"  • Errors: {len(validation.get('errors', []))}")
        print(f"  • Warnings: {len(validation.get('warnings', []))}")
        print(f"  • Summary: {validation.get('summary', 'N/A')}")
    
    # Final SQL
    final_sql = result.get('final_sql', '')
    if final_sql:
        print(f"\n🔧 Generated SQL:")
        print(f"{'─'*60}")
        print(final_sql)
        print(f"{'─'*60}")
    
    # Recommendations
    recommendations = result.get('recommendations', [])
    if recommendations:
        print(f"\n💡 Recommendations:")
        for rec in recommendations:
            print(f"  • {rec}")
    
    # Execution results
    execution = result.get('execution', {})
    if execution:
        print(f"\n🚀 Execution Results:")
        print(f"  • Executed: {execution.get('executed', False)}")
        if execution.get('executed', False):
            print(f"  • Rows Returned: {execution.get('rows_returned', 0)}")
            print(f"  • Columns: {', '.join(execution.get('columns', []))}")
            if execution.get('truncated', False):
                print(f"  • ⚠️ Results truncated (showing first 100 rows)")
        else:
            print(f"  • Reason: {execution.get('reason', 'N/A')}")

def interactive_mode():
    """Run in interactive mode."""
    print_banner()
    
    # Initialize system
    try:
        system = get_multi_agent_system()
        print_system_status(system)
    except Exception as e:
        print(f"❌ Failed to initialize system: {e}")
        return
    
    print(f"\n💬 Interactive Mode - Type 'quit' to exit")
    print(f"💡 Example queries:")
    print(f"  • Show me recent DUI cases from the last 30 days")
    print(f"  • Count how many defendants had BAC above 0.08")
    print(f"  • List officers with the most DUI arrests")
    print(f"  • Find cases with field sobriety test failures")
    
    while True:
        try:
            print(f"\n{'─'*60}")
            query = input("🔍 Enter your query: ").strip()
            
            if query.lower() in ['quit', 'exit', 'q']:
                print("👋 Goodbye!")
                break
            
            if not query:
                continue
            
            print(f"🔄 Processing query...")
            result = system.process_query(query)
            print_result(result)
            
        except KeyboardInterrupt:
            print(f"\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

def batch_mode(queries):
    """Run in batch mode with predefined queries."""
    print_banner()
    
    # Initialize system
    try:
        system = get_multi_agent_system()
        print_system_status(system)
    except Exception as e:
        print(f"❌ Failed to initialize system: {e}")
        return
    
    print(f"\n🧪 Batch Mode - Testing {len(queries)} queries")
    
    results = []
    for i, query in enumerate(queries, 1):
        print(f"\n{'─'*60}")
        print(f"🔍 Query {i}/{len(queries)}: {query}")
        print(f"🔄 Processing...")
        
        result = system.process_query(query)
        results.append(result)
        
        # Print summary
        success = result.get('success', False)
        context_usage = result.get('context_usage', {})
        views_used = context_usage.get('views_used', 0)
        
        print(f"✅ Success: {success}")
        print(f"📊 Context: {context_usage.get('total_estimated', 'N/A')}")
        print(f"🔍 Views: {views_used}")
    
    # Print summary
    print(f"\n{'='*60}")
    print(f"📊 BATCH SUMMARY")
    print(f"{'='*60}")
    
    successful = sum(1 for r in results if r.get('success', False))
    total_context = sum(
        int(r.get('context_usage', {}).get('total_estimated', '0KB').replace('~', '').replace('KB', ''))
        for r in results
    )
    total_views = sum(
        r.get('context_usage', {}).get('views_used', 0)
        for r in results
    )
    
    print(f"✅ Successful Queries: {successful}/{len(queries)}")
    print(f"📊 Total Context Used: ~{total_context}KB")
    print(f"🔍 Total Views Used: {total_views}")
    print(f"📉 Average Context per Query: ~{total_context//len(queries)}KB")

def main():
    """Main function."""
    if len(sys.argv) > 1:
        command = sys.argv[1].lower()
        
        if command == "test":
            # Test with sample queries
            test_queries = [
                "Show me recent DUI cases from the last 30 days",
                "Count how many defendants had BAC above 0.08",
                "List officers with the most DUI arrests",
                "Find cases with field sobriety test failures"
            ]
            batch_mode(test_queries)
        elif command == "status":
            # Show system status only
            print_banner()
            system = get_multi_agent_system()
            print_system_status(system)
        else:
            print(f"❌ Unknown command: {command}")
            print(f"Usage: python dui_interface_multi_agent.py [test|status]")
    else:
        # Interactive mode
        interactive_mode()

if __name__ == "__main__":
    main()
