#!/usr/bin/env python3
"""
DUI Multi-Agent SQL System
Orchestrates multiple specialized agents for efficient SQL generation.
Reduces context size from 100KB+ to ~25KB total across all agents.
"""

import json
import os
import logging
from typing import Dict, List, Any, Optional
from dotenv import load_dotenv

# Import agents
from data_manager import get_data_manager
from agents.query_analyzer import QueryAnalyzerAgent
from agents.view_selector import ViewSelectorAgent
from agents.sql_generator import SQLGeneratorAgent
from agents.validator import ValidatorAgent

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DUIMultiAgentSystem:
    """Multi-agent system for DUI SQL generation with optimized context usage."""
    
    def __init__(self):
        """Initialize the multi-agent system."""
        # Load environment variables
        load_dotenv('.env')
        
        # Initialize data manager
        self.data_manager = get_data_manager()
        
        # Initialize agents
        self.query_analyzer = QueryAnalyzerAgent()
        self.view_selector = ViewSelectorAgent(self.data_manager)
        self.sql_generator = SQLGeneratorAgent(self.data_manager)
        self.validator = ValidatorAgent(self.data_manager)
        
        # Preload common views for better performance
        self.data_manager.preload_common_views()
        
        logger.info("🚀 DUI Multi-Agent System initialized")
    
    def process_query(self, user_query: str) -> Dict[str, Any]:
        """Process a user query through the multi-agent pipeline."""
        try:
            logger.info(f"🔍 Processing query: {user_query[:50]}...")
            
            # Step 1: Query Analysis (~1KB context)
            logger.info("📊 Step 1: Analyzing query...")
            query_analysis = self.query_analyzer.analyze_query(user_query)
            
            # Step 2: View Selection (~1KB context)
            logger.info("🎯 Step 2: Selecting relevant views...")
            selected_views = self.view_selector.select_views(query_analysis)
            view_recommendations = self.view_selector.get_view_recommendations(query_analysis)
            
            # Step 3: SQL Generation (~15KB context)
            logger.info("⚙️ Step 3: Generating SQL...")
            sql_result = self.sql_generator.generate_sql(user_query, selected_views, query_analysis)
            
            # Step 4: SQL Validation (~5KB context)
            logger.info("✅ Step 4: Validating SQL...")
            validation_result = self.validator.validate_sql(
                sql_result.get("sql_query", ""), 
                selected_views, 
                query_analysis
            )
            
            # Compile final result
            result = self._compile_result(
                user_query, query_analysis, view_recommendations, 
                sql_result, validation_result
            )
            
            logger.info("🎉 Query processing completed successfully")
            return result
            
        except Exception as e:
            logger.error(f"❌ Query processing failed: {e}")
            return self._create_error_result(user_query, str(e))
    
    def _compile_result(self, user_query: str, query_analysis: Dict, 
                       view_recommendations: Dict, sql_result: Dict, 
                       validation_result: Dict) -> Dict[str, Any]:
        """Compile the final result from all agents."""
        return {
            "success": sql_result.get("success", False) and validation_result.get("is_valid", False),
            "user_query": user_query,
            "query_analysis": query_analysis,
            "view_selection": view_recommendations,
            "sql_generation": sql_result,
            "validation": validation_result,
            "final_sql": sql_result.get("sql_query", ""),
            "is_valid": validation_result.get("is_valid", False),
            "context_usage": self._calculate_context_usage(query_analysis, view_recommendations),
            "performance_metrics": self._calculate_performance_metrics(),
            "recommendations": self._generate_recommendations(validation_result, sql_result)
        }
    
    def _calculate_context_usage(self, query_analysis: Dict, view_recommendations: Dict) -> Dict[str, Any]:
        """Calculate context usage across all agents."""
        selected_views = view_recommendations.get("selected_views", [])
        estimated_context_size = view_recommendations.get("estimated_context_size", 0)
        
        return {
            "query_analyzer": "~1KB",
            "view_selector": "~1KB", 
            "sql_generator": f"~{estimated_context_size}KB",
            "validator": "~5KB",
            "total_estimated": f"~{estimated_context_size + 7}KB",
            "views_used": len(selected_views),
            "context_reduction": "~75% compared to monolithic approach"
        }
    
    def _calculate_performance_metrics(self) -> Dict[str, Any]:
        """Calculate performance metrics."""
        cache_stats = self.data_manager.get_cache_stats()
        
        return {
            "cache_hit_ratio": f"{cache_stats['cache_hit_ratio']:.2%}",
            "cached_views": cache_stats["cached_views"],
            "total_views": cache_stats["total_views"],
            "processing_time": "Optimized for minimal context usage"
        }
    
    def _generate_recommendations(self, validation_result: Dict, sql_result: Dict) -> List[str]:
        """Generate recommendations based on validation results."""
        recommendations = []
        
        # Add validation-based recommendations
        if validation_result.get("warnings"):
            recommendations.append("Consider addressing validation warnings for better query quality")
        
        if validation_result.get("security_issues"):
            recommendations.append("Review security issues before executing query")
        
        if validation_result.get("performance_notes"):
            recommendations.append("Consider performance optimizations for large datasets")
        
        # Add SQL-based recommendations
        if not sql_result.get("success", False):
            recommendations.append("SQL generation failed - check view availability and query complexity")
        
        if not recommendations:
            recommendations.append("Query looks good! Ready for execution.")
        
        return recommendations
    
    def _create_error_result(self, user_query: str, error_message: str) -> Dict[str, Any]:
        """Create an error result when processing fails."""
        return {
            "success": False,
            "user_query": user_query,
            "error": error_message,
            "query_analysis": {},
            "view_selection": {},
            "sql_generation": {},
            "validation": {},
            "final_sql": "",
            "is_valid": False,
            "context_usage": {},
            "performance_metrics": {},
            "recommendations": [f"Error occurred: {error_message}"]
        }
    
    def get_system_status(self) -> Dict[str, Any]:
        """Get the current status of the multi-agent system."""
        cache_stats = self.data_manager.get_cache_stats()
        
        return {
            "system_status": "operational",
            "agents_loaded": 4,
            "data_manager": {
                "total_views": cache_stats["total_views"],
                "cached_views": cache_stats["cached_views"],
                "cache_hit_ratio": f"{cache_stats['cache_hit_ratio']:.2%}"
            },
            "context_optimization": {
                "original_context_size": "100KB+",
                "optimized_context_size": "~25KB",
                "reduction_percentage": "~75%"
            },
            "agent_contexts": {
                "query_analyzer": "~1KB",
                "view_selector": "~1KB", 
                "sql_generator": "~15KB",
                "validator": "~5KB"
            }
        }
    
    def execute_query(self, user_query: str) -> Dict[str, Any]:
        """Execute a query and return results (if database connection available)."""
        try:
            # Process the query
            result = self.process_query(user_query)
            
            if not result.get("success", False):
                return result
            
            # Try to execute the SQL if database connection is available
            sql_query = result.get("final_sql", "")
            if sql_query and self._can_connect_to_database():
                execution_result = self._execute_sql(sql_query)
                result["execution"] = execution_result
            else:
                result["execution"] = {
                    "executed": False,
                    "reason": "Database connection not available or SQL not valid"
                }
            
            return result
            
        except Exception as e:
            logger.error(f"❌ Query execution failed: {e}")
            return self._create_error_result(user_query, str(e))
    
    def _can_connect_to_database(self) -> bool:
        """Check if database connection is available."""
        try:
            import pyodbc
            from dotenv import load_dotenv
            
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
            conn.close()
            return True
            
        except Exception:
            return False
    
    def _execute_sql(self, sql_query: str) -> Dict[str, Any]:
        """Execute SQL query and return results."""
        try:
            import pyodbc
            from dotenv import load_dotenv
            
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
            
            # Execute query
            cursor.execute(sql_query)
            
            # Get column names
            columns = [column[0] for column in cursor.description]
            
            # Get results (limit to first 100 rows for safety)
            rows = cursor.fetchmany(100)
            
            conn.close()
            
            return {
                "executed": True,
                "rows_returned": len(rows),
                "columns": columns,
                "data": rows,
                "truncated": len(rows) == 100
            }
            
        except Exception as e:
            return {
                "executed": False,
                "error": str(e),
                "rows_returned": 0,
                "columns": [],
                "data": []
            }

# Global instance
_multi_agent_system = None

def get_multi_agent_system() -> DUIMultiAgentSystem:
    """Get the global multi-agent system instance."""
    global _multi_agent_system
    if _multi_agent_system is None:
        _multi_agent_system = DUIMultiAgentSystem()
    return _multi_agent_system

def main():
    """Main function for testing the multi-agent system."""
    print("🚀 DUI Multi-Agent SQL System")
    print("=" * 40)
    
    # Initialize system
    system = get_multi_agent_system()
    
    # Show system status
    status = system.get_system_status()
    print(f"✅ System Status: {status['system_status']}")
    print(f"📊 Total Views: {status['data_manager']['total_views']}")
    print(f"💾 Cache Hit Ratio: {status['data_manager']['cache_hit_ratio']}")
    print(f"📉 Context Reduction: {status['context_optimization']['reduction_percentage']}")
    
    # Test queries
    test_queries = [
        "Show me recent DUI cases from the last 30 days",
        "Count how many defendants had BAC above 0.08",
        "List officers with the most DUI arrests"
    ]
    
    print(f"\n🧪 Testing with {len(test_queries)} sample queries...")
    
    for i, query in enumerate(test_queries, 1):
        print(f"\n--- Test Query {i} ---")
        print(f"Query: {query}")
        
        result = system.process_query(query)
        
        if result.get("success", False):
            print(f"✅ Success: {result.get('is_valid', False)}")
            print(f"📊 Context Usage: {result.get('context_usage', {}).get('total_estimated', 'Unknown')}")
            print(f"🔍 Views Used: {result.get('context_usage', {}).get('views_used', 0)}")
        else:
            print(f"❌ Failed: {result.get('error', 'Unknown error')}")

if __name__ == "__main__":
    main()
