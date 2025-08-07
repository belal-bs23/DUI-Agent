#!/usr/bin/env python3
"""
DUI SQL Agent
AI agent that generates precise SQL queries for DUI schema using configurable models.
"""

import json
import os
from typing import Dict, List, Any, Optional
from pathlib import Path
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from pydantic import BaseModel, Field
import logging
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load comprehensive view schema
def load_comprehensive_view_schema() -> Dict:
    """Load the comprehensive view schema from the analysis."""
    schema_file = Path("db_backup/comprehensive_dui_view_schema.json")
    if not schema_file.exists():
        raise FileNotFoundError(f"Comprehensive view schema not found: {schema_file}")
    
    with open(schema_file, 'r', encoding='utf-8') as f:
        return json.load(f)

# Load database analysis
def load_database_analysis() -> Dict:
    """Load the database analysis data."""
    analysis_file = Path("db_backup/dui_database_analysis.json")
    if not analysis_file.exists():
        raise FileNotFoundError(f"Database analysis not found: {analysis_file}")
    
    with open(analysis_file, 'r', encoding='utf-8') as f:
        return json.load(f)

class QueryResponse(BaseModel):
    """Response model for SQL query generation."""
    sql_query: str = Field(description="Generated SQL query")
    explanation: str = Field(description="Explanation of the generated query")
    view_used: str = Field(description="Primary view used for the query")
    security_note: str = Field(description="Security considerations for the query")

class DUISQLAgent:
    """DUI SQL Agent using configurable models."""
    
    def __init__(self):
        """Initialize the agent with model configuration from environment."""
        try:
            self.view_schema = load_comprehensive_view_schema()
            self.database_analysis = load_database_analysis()
        except FileNotFoundError as e:
            logger.warning(f"Schema files not found: {e}")
            self.view_schema = {"views": {}}
            self.database_analysis = {"tables": {}}
        
        # Get model configuration from environment
        self.model_type = os.getenv("AI_MODEL_TYPE", "mock")
        self.model_name = os.getenv("AI_MODEL_NAME", "")
        self.api_key = os.getenv("AI_API_KEY", "")
        
        self.llm = self._initialize_model()
        
        # Create the prompt template
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", """You are a DUI database expert. Generate precise SQL queries for the DUI schema using the available views.

Available Views:
{view_schema}

Database Analysis:
{db_analysis}

Instructions:
1. Use the most appropriate view(s) for the query
2. Ensure the SQL is valid for SQL Server
3. Include proper WHERE clauses and JOINs as needed
4. Consider security - avoid accessing sensitive data directly
5. Provide clear explanations for your choices

User Query: {user_query}
Context: {context}

Generate a JSON response with:
- sql_query: The generated SQL query
- explanation: Why you chose this approach
- view_used: Which view(s) you used
- security_note: Any security considerations"""),
            ("human", "{user_query}")
        ])
    
    def _initialize_model(self):
        """Initialize the appropriate model based on environment configuration."""
        if self.model_type == "openai":
            try:
                from langchain_openai import ChatOpenAI
                model_name = self.model_name or "gpt-3.5-turbo"
                print(f"Using free OpenAI model: {model_name}")
                return ChatOpenAI(
                    model=model_name,
                    temperature=0.1
                )
            except Exception as e:
                logger.warning(f"OpenAI model failed: {e}")
                return self._create_mock_model()
        
        elif self.model_type == "ollama":
            try:
                from langchain_community.llms import Ollama
                model_name = self.model_name or "llama2"
                return Ollama(model=model_name)
            except Exception as e:
                logger.warning(f"Ollama model failed: {e}")
                return self._create_mock_model()
        
        elif self.model_type == "gemini":
            try:
                from langchain_google_genai import ChatGoogleGenerativeAI
                model_name = self.model_name or "gemini-2.0-flash"
                print(f"Using free Gemini model: {model_name}")
                return ChatGoogleGenerativeAI(
                    model=model_name,
                    temperature=0.1,
                    google_api_key=os.getenv("GOOGLE_API_KEY")
                )
            except Exception as e:
                logger.warning(f"Gemini model failed: {e}")
                return self._create_mock_model()
        
        elif self.model_type == "huggingface":
            try:
                from langchain_community.llms import HuggingFaceHub
                repo_id = self.model_name or "microsoft/DialoGPT-medium"
                return HuggingFaceHub(
                    repo_id=repo_id,
                    model_kwargs={"temperature": 0.1}
                )
            except Exception as e:
                logger.warning(f"HuggingFace model failed: {e}")
                return self._create_mock_model()
        
        else:  # mock model as fallback
            return self._create_mock_model()
    
    def _create_mock_model(self):
        """Create a mock model for testing without API calls."""
        class MockLLM:
            def invoke(self, messages):
                class MockResponse:
                    def __init__(self, content):
                        self.content = content
                
                # Generate a simple SQL query based on the prompt
                prompt_content = str(messages)
                if "DUI cases" in prompt_content:
                    sql = """SELECT TOP 100 
                            CaseId, 
                            CaseNumber, 
                            CaseDate, 
                            DefendantName,
                            OffenseDescription
                        FROM DUI.v_case_summary 
                        WHERE CaseDate >= DATEADD(day, -30, GETDATE())
                        ORDER BY CaseDate DESC"""
                else:
                    sql = """SELECT TOP 50 * FROM DUI.v_case_summary"""
                
                response_json = {
                    "sql_query": sql,
                    "explanation": "Generated SQL query for DUI cases using secure views",
                    "view_used": "v_case_summary",
                    "security_note": "Query uses secure views that exclude sensitive data"
                }
                
                return MockResponse(json.dumps(response_json))
        
        return MockLLM()
    
    def run_query(self, user_query: str, context: str = "") -> Dict:
        """Run a query and return the result."""
        try:
            # Format the prompt
            formatted_prompt = self.prompt.format_messages(
                user_query=user_query,
                context=context,
                view_schema=json.dumps(self.view_schema.get('views', {}), indent=2),
                db_analysis=json.dumps(self.database_analysis.get('tables', {}), indent=2)
            )
            
            # Generate response
            response = self.llm.invoke(formatted_prompt)
            
            # Parse the response
            try:
                # Try to parse as JSON first
                if isinstance(response.content, str) and response.content.strip().startswith('{'):
                    result = json.loads(response.content)
                    return {
                        "success": True,
                        "sql_query": result.get("sql_query", response.content),
                        "explanation": result.get("explanation", "Generated SQL query"),
                        "view_used": result.get("view_used", "v_case_summary"),
                        "security_note": result.get("security_note", "Uses secure views"),
                        "model_used": self.model_type
                    }
                else:
                    # Fallback to direct response
                    return {
                        "success": True,
                        "sql_query": response.content,
                        "explanation": "Generated using direct LLM response",
                        "view_used": "v_case_summary",
                        "security_note": "Standard security measures applied",
                        "model_used": self.model_type
                    }
            except Exception as parse_error:
                # Fallback to direct response parsing
                logger.warning(f"Parser failed, using direct response: {parse_error}")
                return {
                    "success": True,
                    "sql_query": response.content,
                    "explanation": "Generated using direct LLM response",
                    "view_used": "Multiple views",
                    "security_note": "Standard security measures applied",
                    "model_used": self.model_type
                }
                
        except Exception as e:
            logger.error(f"Error running query: {e}")
            return {
                "success": False,
                "error": str(e),
                "sql_query": "",
                "explanation": "",
                "view_used": "",
                "security_note": "",
                "model_used": self.model_type
            }
    
    def get_available_views(self) -> Dict:
        """Get information about available views."""
        return self.view_schema.get('views', {})
    
    def get_view_info(self, view_name: str) -> Dict:
        """Get detailed information about a specific view."""
        return self.view_schema.get('views', {}).get(view_name, {})

def main():
    """Main function for testing."""
    print("DUI SQL Agent")
    print("=" * 40)
    
    # Show current configuration
    model_type = os.getenv("AI_MODEL_TYPE", "mock")
    model_name = os.getenv("AI_MODEL_NAME", "")
    print(f"Model Type: {model_type}")
    if model_name:
        print(f"Model Name: {model_name}")
    
    try:
        agent = DUISQLAgent()
        
        # Test query
        test_query = "Show me all DUI cases from the last 30 days"
        result = agent.run_query(test_query)
        
        if result["success"]:
            print("✅ Query generated successfully!")
            print(f"SQL: {result['sql_query'][:100]}...")
            print(f"Model: {result['model_used']}")
        else:
            print(f"❌ Query failed: {result['error']}")
            
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main() 