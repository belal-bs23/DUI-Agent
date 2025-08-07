#!/usr/bin/env python3
"""
DUI SQL Agent - LangGraph Implementation
A well-organized, workflow-based AI agent for DUI database query generation.
"""

import json
import os
from typing import Dict, List, Any, Optional, TypedDict, Annotated
from pathlib import Path
from langchain_core.messages import HumanMessage, AIMessage, BaseMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from pydantic import BaseModel, Field
import logging
from dotenv import load_dotenv
from langgraph.graph import StateGraph, END
from langgraph.checkpoint.memory import MemorySaver

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ============================================================================
# STATE MANAGEMENT
# ============================================================================

class AgentState(TypedDict):
    """State for the DUI SQL Agent workflow."""
    messages: Annotated[List[BaseMessage], "Chat messages"]
    user_query: Annotated[str, "The user's natural language query"]
    context: Annotated[str, "Additional context for the query"]
    view_schema: Annotated[Dict, "Available database views"]
    database_analysis: Annotated[Dict, "Database analysis data"]
    selected_views: Annotated[List[str], "Views selected for the query"]
    sql_query: Annotated[str, "Generated SQL query"]
    explanation: Annotated[str, "Explanation of the query"]
    security_note: Annotated[str, "Security considerations"]
    model_used: Annotated[str, "AI model used for generation"]
    success: Annotated[bool, "Whether the query generation was successful"]
    error: Annotated[str, "Error message if any"]

# ============================================================================
# DATA MODELS
# ============================================================================

class QueryResponse(BaseModel):
    """Response model for SQL query generation."""
    sql_query: str = Field(description="Generated SQL query")
    explanation: str = Field(description="Explanation of the generated query")
    view_used: str = Field(description="Primary view used for the query")
    security_note: str = Field(description="Security considerations for the query")

class ViewInfo(BaseModel):
    """Information about a database view."""
    name: str = Field(description="View name")
    description: str = Field(description="View description")
    columns: List[str] = Field(description="Available columns")
    type: str = Field(description="View type/category")

# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

def load_comprehensive_view_schema() -> Dict:
    """Load the comprehensive view schema from the analysis."""
    schema_file = Path("db_backup/comprehensive_dui_view_schema.json")
    if not schema_file.exists():
        raise FileNotFoundError(f"Comprehensive view schema not found: {schema_file}")
    
    with open(schema_file, 'r', encoding='utf-8') as f:
        schema_data = json.load(f)
    
    # Extract views from the correct structure
    schema = schema_data.get('views', {})
    
    # Filter out missing views that failed to deploy
    missing_views = ["v_case_summary", "v_evidence_summary", "v_officer_performance", "v_defendant_summary"]
    filtered_schema = {}
    
    for view_name, view_data in schema.items():
        if view_name not in missing_views:
            filtered_schema[view_name] = view_data
    
    logger.info(f"✅ Loaded {len(filtered_schema)} working views (filtered out {len(missing_views)} missing views)")
    return filtered_schema

def load_database_analysis() -> Dict:
    """Load the database analysis data."""
    analysis_file = Path("db_backup/dui_database_analysis.json")
    if not analysis_file.exists():
        raise FileNotFoundError(f"Database analysis not found: {analysis_file}")
    
    with open(analysis_file, 'r', encoding='utf-8') as f:
        return json.load(f)

def get_model_configuration():
    """Get model configuration from environment."""
    return {
        "model_type": os.getenv("AI_MODEL_TYPE", "mock"),
        "model_name": os.getenv("AI_MODEL_NAME", ""),
        "api_key": os.getenv("AI_API_KEY", "")
    }

# ============================================================================
# WORKFLOW NODES
# ============================================================================

def initialize_state(state: AgentState) -> AgentState:
    """Initialize the agent state with schema and analysis data."""
    try:
        state["view_schema"] = load_comprehensive_view_schema()
        state["database_analysis"] = load_database_analysis()
        state["success"] = True
        state["error"] = ""
        logger.info("✅ State initialized successfully")
    except Exception as e:
        state["success"] = False
        state["error"] = f"Failed to initialize state: {e}"
        logger.error(f"❌ State initialization failed: {e}")
    
    return state

def analyze_query(state: AgentState) -> AgentState:
    """Analyze the user query to understand intent and requirements."""
    user_query = state["user_query"]
    
    # Add analysis message
    analysis_message = f"Analyzing query: {user_query}"
    state["messages"].append(HumanMessage(content=analysis_message))
    
    # Simple keyword analysis for view selection
    query_lower = user_query.lower()
    selected_views = []
    
    # Map keywords to view categories (using only working views)
    view_mapping = {
        "case": ["v_caseheaders", "v_caseoffenses_with_caseheaders"],
        "defendant": ["v_defendants"],
        "evidence": ["v_physicalevidence"],
        "officer": ["v_otherofficers_with_caseheaders"],
        "blood": ["v_specimenreport_with_caseheaders"],
        "alcohol": ["v_specimenreport_with_caseheaders"],
        "bac": ["v_specimenreport_with_caseheaders"],
        "offense": ["v_caseoffenses_with_caseheaders", "v_tbl_opt_offense"],
        "court": ["v_caseheaders"],
        "field": ["v_fieldsobrietytests"],
        "sobriety": ["v_fieldsobrietytests"],
        "test": ["v_fieldsobrietytests", "v_specimenreport_with_caseheaders"],
        "time": ["v_caseoffenses_with_caseheaders"],
        "date": ["v_caseoffenses_with_caseheaders"],
        "month": ["v_caseoffenses_with_caseheaders"],
        "last": ["v_caseoffenses_with_caseheaders"]
    }
    
    for keyword, views in view_mapping.items():
        if keyword in query_lower:
            selected_views.extend(views)
    
    # Remove duplicates and limit to top 3 most relevant
    selected_views = list(set(selected_views))[:3]
    
    if not selected_views:
        selected_views = ["v_caseheaders"]  # Default fallback using working view
    
    state["selected_views"] = selected_views
    state["messages"].append(AIMessage(content=f"Selected views: {', '.join(selected_views)}"))
    
    logger.info(f"🔍 Query analysis complete. Selected views: {selected_views}")
    return state

def generate_sql(state: AgentState) -> AgentState:
    """Generate SQL query using the selected views and AI model."""
    try:
        # Get model configuration
        config = get_model_configuration()
        model_type = config["model_type"]
        
        # Initialize model
        llm = initialize_model(model_type, config)
        
        # Create prompt for SQL generation
        prompt = create_sql_generation_prompt()
        
        # Prepare context
        context = {
            "user_query": state["user_query"],
            "context": state["context"],
            "selected_views": state["selected_views"],
            "view_schema": json.dumps(state["view_schema"], indent=2),
            "database_analysis": json.dumps(state["database_analysis"], indent=2)
        }
        
        # Generate SQL
        response = llm.invoke(prompt.format_messages(**context))
        
        # Parse response
        try:
            result = json.loads(response.content)
            state["sql_query"] = result.get("sql_query", "")
            state["explanation"] = result.get("explanation", "")
            state["security_note"] = result.get("security_note", "")
            state["model_used"] = model_type
            state["success"] = True
            state["error"] = ""
        except json.JSONDecodeError:
            # Fallback: treat as plain text
            state["sql_query"] = response.content
            state["explanation"] = "Generated using direct model response"
            state["security_note"] = "Standard security measures applied"
            state["model_used"] = model_type
            state["success"] = True
            state["error"] = ""
        
        state["messages"].append(AIMessage(content=f"SQL generated using {model_type} model"))
        logger.info(f"✅ SQL generation successful using {model_type}")
        
    except Exception as e:
        error_msg = str(e)
        
        # Handle specific error types
        if "429" in error_msg or "quota" in error_msg.lower() or "rate limit" in error_msg.lower():
            # Rate limit or quota exceeded - inform user
            logger.warning(f"⚠️ Rate limit/quota exceeded with {model_type}")
            state["success"] = False
            state["error"] = f"Rate limit exceeded with {model_type}. Please try again later or switch to a different model in your .env file."
            state["messages"].append(AIMessage(content=f"Rate limit error: {error_msg}"))
            logger.error(f"❌ Rate limit exceeded: {error_msg}")
            
        elif "api key" in error_msg.lower() or "invalid" in error_msg.lower():
            # API key issues
            state["success"] = False
            state["error"] = f"API key configuration error: {error_msg}"
            state["messages"].append(AIMessage(content=f"API key error: {error_msg}"))
            logger.error(f"❌ API key configuration error: {error_msg}")
            
        else:
            # Other errors
            state["success"] = False
            state["error"] = f"SQL generation failed: {error_msg}"
            state["messages"].append(AIMessage(content=f"Error: {error_msg}"))
            logger.error(f"❌ SQL generation failed: {error_msg}")
    
    return state

def validate_query(state: AgentState) -> AgentState:
    """Validate the generated SQL query."""
    if not state["success"]:
        return state
    
    sql_query = state["sql_query"]
    
    # Basic SQL validation
    validation_checks = [
        ("SELECT", "Query must start with SELECT"),
        ("FROM", "Query must include FROM clause"),
    ]
    
    validation_errors = []
    for check, message in validation_checks:
        if check not in sql_query.upper():
            validation_errors.append(message)
    
    # Check for DUI schema usage (warn but don't fail)
    if "DUI." not in sql_query.upper():
        logger.warning("⚠️ Query doesn't use DUI schema prefix - this may cause issues")
        # Try to fix the query by adding DUI schema prefix
        if not validation_errors:  # Only fix if other validations pass
            fixed_query = sql_query.replace("FROM v_", "FROM DUI.v_")
            fixed_query = fixed_query.replace("JOIN v_", "JOIN DUI.v_")
            if fixed_query != sql_query:
                state["sql_query"] = fixed_query
                logger.info("✅ Auto-fixed DUI schema prefix")
    
    if validation_errors:
        state["error"] = f"Validation errors: {'; '.join(validation_errors)}"
        state["success"] = False
        logger.warning(f"⚠️ SQL validation failed: {validation_errors}")
    else:
        logger.info("✅ SQL validation passed")
    
    return state

def finalize_response(state: AgentState) -> AgentState:
    """Finalize the response and add summary."""
    if state["success"]:
        summary = f"Query generated successfully using {state['model_used']} model. Views used: {', '.join(state['selected_views'])}"
        state["messages"].append(AIMessage(content=summary))
        logger.info("🎉 Query generation workflow completed successfully")
    else:
        error_summary = f"Query generation failed: {state['error']}"
        state["messages"].append(AIMessage(content=error_summary))
        logger.error(f"💥 Query generation workflow failed: {state['error']}")
    
    return state

# ============================================================================
# MODEL INITIALIZATION
# ============================================================================

def initialize_model(model_type: str, config: Dict):
    """Initialize the appropriate AI model."""
    if model_type == "mock":
        return create_mock_model()
    elif model_type == "openai":
        from langchain_openai import ChatOpenAI
        return ChatOpenAI(
            model=config.get("model_name", "gpt-3.5-turbo"),
            api_key=config.get("api_key"),
            temperature=0.1
        )
    elif model_type == "gemini":
        from langchain_google_genai import ChatGoogleGenerativeAI
        return ChatGoogleGenerativeAI(
            model=config.get("model_name", "gemini-2.0-flash"),
            google_api_key=config.get("api_key"),
            temperature=0.1
        )
    elif model_type == "ollama":
        from langchain_community.llms import Ollama
        return Ollama(
            model=config.get("model_name", "llama2"),
            temperature=0.1
        )
    elif model_type == "huggingface":
        from langchain_community.llms import HuggingFaceEndpoint
        return HuggingFaceEndpoint(
            endpoint_url=config.get("model_name"),
            huggingfacehub_api_token=config.get("api_key"),
            temperature=0.1
        )
    else:
        logger.warning(f"Unknown model type: {model_type}, using mock")
        return create_mock_model()

def create_mock_model():
    """Create a mock model for testing."""
    class MockLLM:
        def invoke(self, messages):
            class MockResponse:
                def __init__(self, content):
                    self.content = content
            
            # Generate a simple mock response
            mock_sql = """
            SELECT 
                ch.CaseId,
                ch.CaseNumber,
                ch.CaseDate,
                d.FirstName + ' ' + d.LastName as DefendantName
            FROM DUI.v_case_summary ch
            LEFT JOIN DUI.v_defendant_summary d ON ch.CaseId = d.CaseId
            WHERE ch.CaseDate >= DATEADD(day, -30, GETDATE())
            ORDER BY ch.CaseDate DESC
            """
            
            mock_response = {
                "sql_query": mock_sql,
                "explanation": "Generated using mock model for testing",
                "view_used": "v_case_summary, v_defendant_summary",
                "security_note": "Mock response - no actual data access"
            }
            
            return MockResponse(json.dumps(mock_response))
    
    return MockLLM()

def create_sql_generation_prompt():
    """Create the prompt template for SQL generation."""
    return ChatPromptTemplate.from_messages([
        ("system", """You are a DUI database expert. Generate precise SQL queries for the DUI schema using the available views.

Available Views:
{view_schema}

Database Analysis:
{database_analysis}

Selected Views for this query:
{selected_views}

CRITICAL INSTRUCTIONS:
1. ALWAYS use the DUI schema prefix: DUI.view_name (e.g., DUI.v_case_summary)
2. ONLY use views that exist in the available views list above
3. Ensure the SQL is valid for SQL Server
4. Include proper WHERE clauses and JOINs as needed
5. Consider security - avoid accessing sensitive data directly
6. Provide clear explanations for your choices
7. Use proper table aliases and column references
8. Make sure all JOIN conditions use existing columns from the views
9. Use EXACT column names as shown in the view schema (no prefixes like "CaseOffenses_")

IMPORTANT: 
- All views must be prefixed with "DUI." in your SQL query
- Only use views that are listed in the available views
- Check that all column references exist in the specified views
- Use proper JOIN syntax with correct column names
- Use the exact column names from the view schema (e.g., "CaseId" not "CaseOffenses_CaseId")
- WARNING: DateEntered column does NOT exist in any view - use TimeOfOff, TimeOfArrest, TimeOfBooking, or TimeOfEventEnd instead
- For date filtering, use the time columns available in the selected views
- NOTE: v_caseoffenses_with_caseheaders already includes case header data - no need to join with v_caseheaders again
- Use the exact column names from the view schema without prefixes
- IMPORTANT: For BAC results, use LabBACResult column (not Result1) in v_specimenreport_with_caseheaders
- IMPORTANT: For field sobriety tests, use FSTGiven, DefendantRefused, PhysicalInjuries, DefMoreThan65 columns (not HGNTestResult, WalkTurnTestResult, OneLegStandTestResult)
- CRITICAL: Do NOT use DISTINCT on text columns (like ProbableCause) - this will cause SQL errors
- CRITICAL: Use exact column names from the schema - for case headers use CaseHeaders_UniqueId, CaseHeaders_StatusId, etc.
- CRITICAL: Only use views that exist in the available views list - do not reference non-existent views

User Query: {user_query}
Context: {context}

Generate a JSON response with:
- sql_query: The generated SQL query (must use DUI schema prefix)
- explanation: Why you chose this approach
- view_used: Which view(s) you used
- security_note: Any security considerations"""),
        ("human", "{user_query}")
    ])

# ============================================================================
# LANGGRAPH WORKFLOW
# ============================================================================

def create_workflow() -> StateGraph:
    """Create the LangGraph workflow for DUI SQL generation."""
    
    # Create the workflow graph
    workflow = StateGraph(AgentState)
    
    # Add nodes
    workflow.add_node("initialize", initialize_state)
    workflow.add_node("analyze", analyze_query)
    workflow.add_node("generate", generate_sql)
    workflow.add_node("validate", validate_query)
    workflow.add_node("finalize", finalize_response)
    
    # Define the workflow
    workflow.set_entry_point("initialize")
    workflow.add_edge("initialize", "analyze")
    workflow.add_edge("analyze", "generate")
    workflow.add_edge("generate", "validate")
    workflow.add_edge("validate", "finalize")
    workflow.add_edge("finalize", END)
    
    return workflow

# ============================================================================
# MAIN AGENT CLASS
# ============================================================================

class DUISQLAgentLangGraph:
    """DUI SQL Agent using LangGraph for workflow management."""
    
    def __init__(self):
        """Initialize the LangGraph-based agent."""
        self.workflow = create_workflow().compile()
        logger.info("🚀 LangGraph-based DUI SQL Agent initialized")
    
    def run_query(self, user_query: str, context: str = "") -> Dict:
        """Run a query through the LangGraph workflow."""
        try:
            # Initialize state
            initial_state = {
                "messages": [HumanMessage(content=user_query)],
                "user_query": user_query,
                "context": context,
                "view_schema": {},
                "database_analysis": {},
                "selected_views": [],
                "sql_query": "",
                "explanation": "",
                "security_note": "",
                "model_used": "",
                "success": False,
                "error": ""
            }
            
            # Run the workflow
            result = self.workflow.invoke(initial_state)
            
            # Extract the final state - LangGraph returns the final state directly
            final_state = result
            
            # Return formatted response
            return {
                "success": final_state["success"],
                "sql_query": final_state["sql_query"],
                "explanation": final_state["explanation"],
                "view_used": ", ".join(final_state["selected_views"]),
                "security_note": final_state["security_note"],
                "model_used": final_state["model_used"],
                "error": final_state["error"],
                "messages": final_state["messages"]
            }
            
        except Exception as e:
            logger.error(f"❌ Workflow execution failed: {e}")
            return {
                "success": False,
                "error": f"Workflow execution failed: {e}",
                "sql_query": "",
                "explanation": "",
                "view_used": "",
                "security_note": "",
                "model_used": "",
                "messages": []
            }
    
    def get_available_views(self) -> Dict:
        """Get available database views."""
        try:
            schema = load_comprehensive_view_schema()
            return schema.get("views", {})
        except Exception as e:
            logger.error(f"Failed to load views: {e}")
            return {}
    
    def get_view_info(self, view_name: str) -> Dict:
        """Get information about a specific view."""
        views = self.get_available_views()
        return views.get(view_name, {})

# ============================================================================
# MAIN FUNCTION
# ============================================================================

def main():
    """Main function for testing the LangGraph agent."""
    print("🚔 DUI SQL Agent - LangGraph Implementation")
    print("=" * 60)
    
    # Initialize agent
    agent = DUISQLAgentLangGraph()
    
    # Test queries
    test_queries = [
        "Show me all DUI cases from the last 30 days",
        "Find cases with blood alcohol content above 0.15",
        "List all defendants with multiple DUI offenses"
    ]
    
    for i, query in enumerate(test_queries, 1):
        print(f"\n📝 Test Query {i}: {query}")
        print("-" * 40)
        
        result = agent.run_query(query)
        
        if result["success"]:
            print("✅ Query generated successfully!")
            print(f"📊 Model Used: {result['model_used']}")
            print(f"🔍 Views Used: {result['view_used']}")
            print(f"🔒 Security: {result['security_note']}")
            print(f"📝 Explanation: {result['explanation']}")
            print(f"\n💻 Generated SQL:")
            print(result['sql_query'])
        else:
            print(f"❌ Query failed: {result['error']}")
        
        print("-" * 40)
    
    print("\n🎉 LangGraph workflow testing completed!")

if __name__ == "__main__":
    main() 