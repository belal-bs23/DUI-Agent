#!/usr/bin/env python3
"""
SQL Generator Agent
Generates SQL queries using relevant view schemas.
Context: ~15KB
"""

import json
import os
from typing import Dict, List, Any, Optional
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
import logging

logger = logging.getLogger(__name__)

class SQLGeneratorAgent:
    """Generates SQL queries using AI models with focused context."""
    
    def __init__(self, data_manager):
        self.data_manager = data_manager
        self.model_config = self._get_model_config()
    
    def generate_sql(self, user_query: str, selected_views: List[str], query_analysis: Dict[str, Any]) -> Dict[str, Any]:
        """Generate SQL query using selected views and analysis."""
        try:
            # Get schemas for selected views
            view_schemas = self.data_manager.get_view_schemas(selected_views)
            
            if not view_schemas:
                raise ValueError("No valid schemas found for selected views")
            
            # Create focused context
            context = self._create_focused_context(user_query, view_schemas, query_analysis)
            
            # Generate SQL using AI model
            sql_result = self._generate_with_ai(context)
            
            # Validate and clean the result
            cleaned_result = self._clean_sql_result(sql_result)
            
            logger.info(f"✅ SQL generated successfully using {len(selected_views)} views")
            return cleaned_result
            
        except Exception as e:
            logger.error(f"❌ SQL generation failed: {e}")
            return {
                "success": False,
                "sql_query": "",
                "explanation": f"SQL generation failed: {str(e)}",
                "view_used": ", ".join(selected_views),
                "security_note": "Generation failed",
                "error": str(e)
            }
    
    def _create_focused_context(self, user_query: str, view_schemas: Dict, query_analysis: Dict[str, Any]) -> Dict[str, Any]:
        """Create focused context for SQL generation (~15KB)."""
        # Extract key information from query analysis
        intent = query_analysis.get("intent", "list")
        requirements = query_analysis.get("requirements", {})
        query_type = query_analysis.get("query_type", "general")
        
        # Create schema summary (focused on relevant columns)
        schema_summary = self._create_schema_summary(view_schemas, query_analysis)
        
        # Create SQL generation rules based on query type
        sql_rules = self._get_sql_rules(intent, query_type, requirements)
        
        context = {
            "user_query": user_query,
            "intent": intent,
            "query_type": query_type,
            "requirements": requirements,
            "selected_views": list(view_schemas.keys()),
            "schema_summary": schema_summary,
            "sql_rules": sql_rules,
            "view_schemas": view_schemas  # Full schemas for detailed generation
        }
        
        return context
    
    def _create_schema_summary(self, view_schemas: Dict, query_analysis: Dict[str, Any]) -> Dict[str, Any]:
        """Create a focused schema summary based on query analysis."""
        keywords = query_analysis.get("keywords", [])
        intent = query_analysis.get("intent", "list")
        
        summary = {}
        
        for view_name, schema in view_schemas.items():
            if not isinstance(schema, dict):
                continue
                
            columns = schema.get("columns", [])
            
            # Filter columns based on relevance
            relevant_columns = []
            for column in columns:
                if not isinstance(column, dict):
                    continue
                    
                column_name = column.get("name", "").lower()
                column_desc = column.get("description", "").lower()
                
                # Check if column is relevant to query
                is_relevant = False
                
                # Check keyword matches
                for keyword in keywords:
                    if keyword.lower() in column_name or keyword.lower() in column_desc:
                        is_relevant = True
                        break
                
                # Include common important columns
                if any(common in column_name for common in ["id", "name", "date", "time", "case", "defendant"]):
                    is_relevant = True
                
                # Include columns based on intent
                if intent == "count" and "count" in column_name:
                    is_relevant = True
                elif intent == "filter" and any(filter_word in column_name for filter_word in ["status", "type", "result"]):
                    is_relevant = True
                
                if is_relevant:
                    relevant_columns.append(column)
            
            # If no relevant columns found, include key columns
            if not relevant_columns:
                relevant_columns = [col for col in columns if isinstance(col, dict) and any(key in col.get("name", "").lower() for key in ["id", "name", "date"])]
            
            summary[view_name] = {
                "description": schema.get("description", ""),
                "relevant_columns": relevant_columns,
                "total_columns": len(columns)
            }
        
        return summary
    
    def _get_sql_rules(self, intent: str, query_type: str, requirements: Dict[str, Any]) -> Dict[str, Any]:
        """Get SQL generation rules based on query characteristics."""
        rules = {
            "base_rules": [
                "Always use DUI schema prefix: DUI.view_name",
                "Use proper table aliases for readability",
                "Include appropriate WHERE clauses",
                "Use proper JOIN syntax with correct column names",
                "Avoid using DISTINCT on text columns",
                "Use exact column names from schema"
            ],
            "intent_rules": [],
            "type_rules": [],
            "requirement_rules": []
        }
        
        # Intent-specific rules
        if intent == "count":
            rules["intent_rules"].extend([
                "Use COUNT(*) for counting records",
                "Consider using GROUP BY if needed",
                "Use appropriate aggregation functions"
            ])
        elif intent == "filter":
            rules["intent_rules"].extend([
                "Use specific WHERE conditions",
                "Consider using multiple conditions with AND/OR",
                "Use appropriate comparison operators"
            ])
        elif intent == "compare":
            rules["intent_rules"].extend([
                "Use UNION or multiple SELECT statements",
                "Include comparison columns",
                "Use appropriate sorting"
            ])
        
        # Query type rules
        if query_type == "aggregation":
            rules["type_rules"].extend([
                "Use GROUP BY for aggregations",
                "Include appropriate aggregation functions",
                "Consider HAVING clause for aggregated filters"
            ])
        elif query_type == "filtered":
            rules["type_rules"].extend([
                "Use specific WHERE conditions",
                "Consider using subqueries if needed",
                "Use appropriate comparison operators"
            ])
        
        # Requirement-specific rules
        if requirements.get("time_filter"):
            rules["requirement_rules"].append(f"Add time filter: {requirements['time_filter']}")
        
        if requirements.get("value_filter"):
            filter_info = requirements["value_filter"]
            rules["requirement_rules"].append(f"Add value filter: {filter_info['type']} {filter_info['value']}")
        
        if requirements.get("sort_order"):
            rules["requirement_rules"].append(f"Add sorting: ORDER BY ... {requirements['sort_order']}")
        
        if requirements.get("limit"):
            rules["requirement_rules"].append(f"Add limit: TOP {requirements['limit']}")
        
        return rules
    
    def _generate_with_ai(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Generate SQL using AI model."""
        try:
            # Initialize model
            llm = self._initialize_model()
            
            # Create prompt
            prompt = self._create_sql_prompt()
            
            # Prepare messages
            messages = prompt.format_messages(
                user_query=context["user_query"],
                intent=context["intent"],
                query_type=context["query_type"],
                requirements=json.dumps(context["requirements"], indent=2),
                selected_views=context["selected_views"],
                schema_summary=json.dumps(context["schema_summary"], indent=2),
                sql_rules=json.dumps(context["sql_rules"], indent=2),
                view_schemas=json.dumps(context["view_schemas"], indent=2)
            )
            
            # Generate response
            response = llm.invoke(messages)
            
            # Parse response
            try:
                result = json.loads(response.content)
                return {
                    "success": True,
                    "sql_query": result.get("sql_query", ""),
                    "explanation": result.get("explanation", ""),
                    "view_used": result.get("view_used", ""),
                    "security_note": result.get("security_note", ""),
                    "model_used": self.model_config.get("model_type", "unknown")
                }
            except json.JSONDecodeError:
                # Fallback: treat as plain text
                return {
                    "success": True,
                    "sql_query": response.content,
                    "explanation": "Generated using direct model response",
                    "view_used": ", ".join(context["selected_views"]),
                    "security_note": "Standard security measures applied",
                    "model_used": self.model_config.get("model_type", "unknown")
                }
                
        except Exception as e:
            logger.error(f"❌ AI model generation failed: {e}")
            raise
    
    def _initialize_model(self):
        """Initialize the AI model."""
        model_type = self.model_config.get("model_type", "mock")
        
        if model_type == "openai":
            from langchain_openai import ChatOpenAI
            return ChatOpenAI(
                model=self.model_config.get("model_name", "gpt-3.5-turbo"),
                api_key=self.model_config.get("api_key"),
                temperature=0.1
            )
        elif model_type == "gemini":
            from langchain_google_genai import ChatGoogleGenerativeAI
            return ChatGoogleGenerativeAI(
                model=self.model_config.get("model_name", "gemini-2.0-flash"),
                google_api_key=self.model_config.get("api_key"),
                temperature=0.1
            )
        else:
            # Mock model for testing
            return self._create_mock_model()
    
    def _create_mock_model(self):
        """Create a mock model for testing."""
        class MockLLM:
            def invoke(self, messages):
                class MockResponse:
                    def __init__(self, content):
                        self.content = content
                
                # Generate a simple mock SQL
                mock_sql = """
                SELECT 
                    ch.CaseId,
                    ch.CaseNumber,
                    ch.TimeOfOff,
                    d.FirstName + ' ' + d.LastName as DefendantName,
                    ch.StatusId
                FROM DUI.v_caseheaders ch
                LEFT JOIN DUI.v_defendants_with_caseheaders d ON ch.CaseId = d.CaseId
                WHERE ch.TimeOfOff >= DATEADD(day, -30, GETDATE())
                ORDER BY ch.TimeOfOff DESC
                """
                
                mock_response = {
                    "sql_query": mock_sql.strip(),
                    "explanation": "Generated using mock model for testing",
                    "view_used": "v_caseheaders, v_defendants",
                    "security_note": "Mock response - no actual data access"
                }
                
                return MockResponse(json.dumps(mock_response))
        
        return MockLLM()
    
    def _create_sql_prompt(self):
        """Create the SQL generation prompt."""
        return ChatPromptTemplate.from_messages([
            ("system", """You are a DUI database expert. Generate precise SQL queries using the provided view schemas.

Query Information:
- User Query: {user_query}
- Intent: {intent}
- Query Type: {query_type}
- Requirements: {requirements}

Selected Views: {selected_views}

Schema Summary: {schema_summary}

SQL Generation Rules: {sql_rules}

Full View Schemas: {view_schemas}

CRITICAL INSTRUCTIONS:
1. ALWAYS use DUI schema prefix: DUI.view_name
2. ONLY use views from the selected_views list
3. Use exact column names from the schema
4. Ensure proper JOIN conditions
5. Include appropriate WHERE clauses based on requirements
6. Use proper SQL Server syntax
7. Consider security - avoid accessing sensitive data directly
8. Provide clear explanations for your choices

Generate a JSON response with:
- sql_query: The generated SQL query (must use DUI schema prefix)
- explanation: Why you chose this approach
- view_used: Which view(s) you used
- security_note: Any security considerations"""),
            ("human", "{user_query}")
        ])
    
    def _clean_sql_result(self, result: Dict[str, Any]) -> Dict[str, Any]:
        """Clean and validate the SQL result."""
        if not result.get("success", False):
            return result
        
        sql_query = result.get("sql_query", "")
        
        # Basic SQL cleaning
        if sql_query:
            # Ensure DUI schema prefix
            if "FROM v_" in sql_query and "FROM DUI.v_" not in sql_query:
                sql_query = sql_query.replace("FROM v_", "FROM DUI.v_")
            
            if "JOIN v_" in sql_query and "JOIN DUI.v_" not in sql_query:
                sql_query = sql_query.replace("JOIN v_", "JOIN DUI.v_")
            
            # Remove extra whitespace
            sql_query = " ".join(sql_query.split())
        
        result["sql_query"] = sql_query
        return result
    
    def _get_model_config(self) -> Dict[str, Any]:
        """Get model configuration from environment."""
        return {
            "model_type": os.getenv("AI_MODEL_TYPE", "mock"),
            "model_name": os.getenv("AI_MODEL_NAME", ""),
            "api_key": os.getenv("AI_API_KEY", "")
        }
