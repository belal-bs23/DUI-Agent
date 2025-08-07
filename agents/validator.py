#!/usr/bin/env python3
"""
Validator Agent
Validates generated SQL queries for syntax, security, and correctness.
Context: ~5KB
"""

import json
import re
from typing import Dict, List, Any, Optional
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate
import logging

logger = logging.getLogger(__name__)

class ValidatorAgent:
    """Validates SQL queries for syntax, security, and correctness."""
    
    def __init__(self, data_manager):
        self.data_manager = data_manager
        self.validation_rules = self._load_validation_rules()
    
    def validate_sql(self, sql_query: str, selected_views: List[str], query_analysis: Dict[str, Any]) -> Dict[str, Any]:
        """Validate the generated SQL query."""
        try:
            validation_result = {
                "is_valid": True,
                "errors": [],
                "warnings": [],
                "security_issues": [],
                "performance_notes": [],
                "suggestions": []
            }
            
            # Basic syntax validation
            syntax_result = self._validate_syntax(sql_query)
            validation_result["errors"].extend(syntax_result["errors"])
            validation_result["warnings"].extend(syntax_result["warnings"])
            
            # Security validation
            security_result = self._validate_security(sql_query)
            validation_result["security_issues"].extend(security_result["issues"])
            
            # Schema validation
            schema_result = self._validate_schema(sql_query, selected_views)
            validation_result["errors"].extend(schema_result["errors"])
            validation_result["warnings"].extend(schema_result["warnings"])
            
            # Performance validation
            performance_result = self._validate_performance(sql_query)
            validation_result["performance_notes"].extend(performance_result["notes"])
            
            # Business logic validation
            business_result = self._validate_business_logic(sql_query, query_analysis)
            validation_result["suggestions"].extend(business_result["suggestions"])
            
            # Update overall validity
            validation_result["is_valid"] = len(validation_result["errors"]) == 0
            
            # Add validation summary
            validation_result["summary"] = self._create_validation_summary(validation_result)
            
            logger.info(f"✅ SQL validation completed: {validation_result['is_valid']}")
            return validation_result
            
        except Exception as e:
            logger.error(f"❌ SQL validation failed: {e}")
            return {
                "is_valid": False,
                "errors": [f"Validation process failed: {str(e)}"],
                "warnings": [],
                "security_issues": [],
                "performance_notes": [],
                "suggestions": [],
                "summary": "Validation process encountered an error"
            }
    
    def _validate_syntax(self, sql_query: str) -> Dict[str, List[str]]:
        """Validate basic SQL syntax."""
        errors = []
        warnings = []
        
        # Check for basic SQL structure
        if not sql_query.strip().upper().startswith("SELECT"):
            errors.append("Query must start with SELECT")
        
        # Check for required clauses
        if "FROM" not in sql_query.upper():
            errors.append("Missing FROM clause")
        
        # Check for proper schema prefix
        if "FROM v_" in sql_query and "FROM DUI.v_" not in sql_query:
            errors.append("Missing DUI schema prefix in FROM clause")
        
        if "JOIN v_" in sql_query and "JOIN DUI.v_" not in sql_query:
            errors.append("Missing DUI schema prefix in JOIN clause")
        
        # Check for common syntax issues
        if sql_query.count("(") != sql_query.count(")"):
            warnings.append("Mismatched parentheses detected")
        
        if sql_query.count("'") % 2 != 0:
            warnings.append("Unmatched quotes detected")
        
        # Check for SQL injection patterns
        dangerous_patterns = [
            r"DROP\s+TABLE",
            r"DELETE\s+FROM",
            r"TRUNCATE\s+TABLE",
            r"ALTER\s+TABLE",
            r"CREATE\s+TABLE",
            r"INSERT\s+INTO",
            r"UPDATE\s+SET"
        ]
        
        for pattern in dangerous_patterns:
            if re.search(pattern, sql_query, re.IGNORECASE):
                errors.append(f"Dangerous SQL operation detected: {pattern}")
        
        return {"errors": errors, "warnings": warnings}
    
    def _validate_security(self, sql_query: str) -> Dict[str, List[str]]:
        """Validate SQL for security issues."""
        issues = []
        
        # Check for potential SQL injection
        injection_patterns = [
            r"';",
            r"';--",
            r"';/*",
            r"UNION\s+SELECT",
            r"OR\s+1\s*=\s*1",
            r"OR\s+'1'\s*=\s*'1'"
        ]
        
        for pattern in injection_patterns:
            if re.search(pattern, sql_query, re.IGNORECASE):
                issues.append(f"Potential SQL injection pattern detected: {pattern}")
        
        # Check for excessive data access
        if "SELECT *" in sql_query.upper():
            issues.append("Using SELECT * - consider selecting specific columns for security")
        
        # Check for sensitive column access
        sensitive_columns = [
            "password", "ssn", "credit_card", "social_security",
            "phone", "email", "address", "date_of_birth"
        ]
        
        for column in sensitive_columns:
            if column in sql_query.lower():
                issues.append(f"Accessing potentially sensitive column: {column}")
        
        return {"issues": issues}
    
    def _validate_schema(self, sql_query: str, selected_views: List[str]) -> Dict[str, List[str]]:
        """Validate SQL against available schema."""
        errors = []
        warnings = []
        
        # Extract view names from SQL
        view_pattern = r"FROM\s+DUI\.([a-zA-Z_][a-zA-Z0-9_]*)"
        join_pattern = r"JOIN\s+DUI\.([a-zA-Z_][a-zA-Z0-9_]*)"
        
        sql_views = set()
        for match in re.finditer(view_pattern, sql_query, re.IGNORECASE):
            sql_views.add(match.group(1))
        for match in re.finditer(join_pattern, sql_query, re.IGNORECASE):
            sql_views.add(match.group(1))
        
        # Check if all referenced views are in selected views
        available_views = set(selected_views)
        for view in sql_views:
            if view not in available_views:
                errors.append(f"Referenced view '{view}' not in selected views")
        
        # Check for column existence (basic check)
        for view_name in sql_views:
            if view_name in available_views:
                schema = self.data_manager.get_view_schema(view_name)
                if schema and isinstance(schema, dict):
                    columns = []
                    for col in schema.get("columns", []):
                        if isinstance(col, dict):
                            columns.append(col.get("name", "").lower())
                    
                    # Extract column references for this view
                    view_alias = self._extract_view_alias(sql_query, view_name)
                    column_pattern = rf"{view_alias}\.([a-zA-Z_][a-zA-Z0-9_]*)"
                    
                    for match in re.finditer(column_pattern, sql_query, re.IGNORECASE):
                        column_name = match.group(1).lower()
                        if column_name not in columns:
                            warnings.append(f"Column '{column_name}' not found in view '{view_name}'")
        
        return {"errors": errors, "warnings": warnings}
    
    def _validate_performance(self, sql_query: str) -> Dict[str, List[str]]:
        """Validate SQL for performance issues."""
        notes = []
        
        # Check for potential performance issues
        if "SELECT *" in sql_query.upper():
            notes.append("SELECT * may impact performance - consider specific columns")
        
        if "DISTINCT" in sql_query.upper():
            notes.append("DISTINCT operation may be expensive on large datasets")
        
        if "ORDER BY" in sql_query.upper() and "TOP" not in sql_query.upper():
            notes.append("ORDER BY without TOP may return large result sets")
        
        # Check for missing WHERE clauses
        if "WHERE" not in sql_query.upper() and "JOIN" in sql_query.upper():
            notes.append("Consider adding WHERE clause to limit results")
        
        # Check for potential cartesian products
        if sql_query.upper().count("JOIN") > 2:
            notes.append("Multiple JOINs detected - ensure proper join conditions")
        
        return {"notes": notes}
    
    def _validate_business_logic(self, sql_query: str, query_analysis: Dict[str, Any]) -> Dict[str, List[str]]:
        """Validate SQL against business logic requirements."""
        suggestions = []
        
        intent = query_analysis.get("intent", "list")
        requirements = query_analysis.get("requirements", {})
        
        # Check intent alignment
        if intent == "count" and "COUNT(" not in sql_query.upper():
            suggestions.append("Query intent is 'count' but no COUNT function found")
        
        if intent == "filter" and "WHERE" not in sql_query.upper():
            suggestions.append("Query intent is 'filter' but no WHERE clause found")
        
        # Check requirements alignment
        if requirements.get("time_filter") and "DATE" not in sql_query.upper():
            suggestions.append("Time filter requirement not implemented in query")
        
        if requirements.get("sort_order") and "ORDER BY" not in sql_query.upper():
            suggestions.append("Sort order requirement not implemented in query")
        
        if requirements.get("limit") and "TOP" not in sql_query.upper():
            suggestions.append("Limit requirement not implemented in query")
        
        return {"suggestions": suggestions}
    
    def _extract_view_alias(self, sql_query: str, view_name: str) -> str:
        """Extract the alias used for a view in the SQL query."""
        # Look for FROM DUI.view_name alias pattern
        from_pattern = rf"FROM\s+DUI\.{re.escape(view_name)}\s+([a-zA-Z_][a-zA-Z0-9_]*)"
        match = re.search(from_pattern, sql_query, re.IGNORECASE)
        if match:
            return match.group(1)
        
        # Look for JOIN DUI.view_name alias pattern
        join_pattern = rf"JOIN\s+DUI\.{re.escape(view_name)}\s+([a-zA-Z_][a-zA-Z0-9_]*)"
        match = re.search(join_pattern, sql_query, re.IGNORECASE)
        if match:
            return match.group(1)
        
        # Return view name as default alias
        return view_name
    
    def _create_validation_summary(self, validation_result: Dict[str, Any]) -> str:
        """Create a summary of validation results."""
        total_issues = (
            len(validation_result["errors"]) +
            len(validation_result["warnings"]) +
            len(validation_result["security_issues"]) +
            len(validation_result["performance_notes"]) +
            len(validation_result["suggestions"])
        )
        
        if validation_result["is_valid"]:
            if total_issues == 0:
                return "✅ Query is valid and ready for execution"
            else:
                return f"⚠️ Query is valid but has {total_issues} issues to consider"
        else:
            return f"❌ Query has {len(validation_result['errors'])} errors that must be fixed"
    
    def _load_validation_rules(self) -> Dict[str, Any]:
        """Load validation rules and patterns."""
        return {
            "required_clauses": ["SELECT", "FROM"],
            "forbidden_operations": [
                "DROP", "DELETE", "TRUNCATE", "ALTER", "CREATE", "INSERT", "UPDATE"
            ],
            "sensitive_columns": [
                "password", "ssn", "credit_card", "social_security",
                "phone", "email", "address", "date_of_birth"
            ],
            "performance_indicators": [
                "SELECT *", "DISTINCT", "ORDER BY", "GROUP BY"
            ]
        }
    
    def get_validation_report(self, validation_result: Dict[str, Any]) -> str:
        """Generate a human-readable validation report."""
        report = []
        
        # Overall status
        status = "✅ VALID" if validation_result["is_valid"] else "❌ INVALID"
        report.append(f"SQL Validation Status: {status}")
        report.append("=" * 50)
        
        # Errors
        if validation_result["errors"]:
            report.append("\n❌ ERRORS (Must Fix):")
            for error in validation_result["errors"]:
                report.append(f"  • {error}")
        
        # Warnings
        if validation_result["warnings"]:
            report.append("\n⚠️ WARNINGS:")
            for warning in validation_result["warnings"]:
                report.append(f"  • {warning}")
        
        # Security issues
        if validation_result["security_issues"]:
            report.append("\n🔒 SECURITY ISSUES:")
            for issue in validation_result["security_issues"]:
                report.append(f"  • {issue}")
        
        # Performance notes
        if validation_result["performance_notes"]:
            report.append("\n⚡ PERFORMANCE NOTES:")
            for note in validation_result["performance_notes"]:
                report.append(f"  • {note}")
        
        # Suggestions
        if validation_result["suggestions"]:
            report.append("\n💡 SUGGESTIONS:")
            for suggestion in validation_result["suggestions"]:
                report.append(f"  • {suggestion}")
        
        # Summary
        report.append(f"\n📋 SUMMARY:")
        report.append(f"  {validation_result['summary']}")
        
        return "\n".join(report)
