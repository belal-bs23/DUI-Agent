#!/usr/bin/env python3
"""
Query Analyzer Agent
Analyzes user queries to extract intent, keywords, and requirements.
Context: ~1KB
"""

import json
import re
from typing import Dict, List, Any
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate
import logging

logger = logging.getLogger(__name__)

class QueryAnalyzerAgent:
    """Analyzes natural language queries to extract structured information."""
    
    def __init__(self):
        self.analysis_rules = {
            "time_keywords": ["last", "recent", "today", "yesterday", "week", "month", "year", "ago"],
            "comparison_keywords": ["above", "below", "over", "under", "more than", "less than", "equal"],
            "aggregation_keywords": ["count", "sum", "average", "total", "how many"],
            "filter_keywords": ["where", "with", "having", "only", "just"],
            "sort_keywords": ["order by", "sort by", "highest", "lowest", "top", "bottom"]
        }
    
    def analyze_query(self, user_query: str) -> Dict[str, Any]:
        """Analyze user query and extract structured information."""
        try:
            # Extract basic information
            intent = self._extract_intent(user_query)
            keywords = self._extract_keywords(user_query)
            requirements = self._extract_requirements(user_query)
            
            analysis = {
                "original_query": user_query,
                "intent": intent,
                "keywords": keywords,
                "requirements": requirements,
                "query_type": self._classify_query_type(user_query),
                "complexity": self._assess_complexity(user_query)
            }
            
            logger.info(f"🔍 Query analyzed: {intent} | Keywords: {keywords}")
            return analysis
            
        except Exception as e:
            logger.error(f"❌ Query analysis failed: {e}")
            return {
                "original_query": user_query,
                "intent": "unknown",
                "keywords": [],
                "requirements": {},
                "query_type": "unknown",
                "complexity": "simple",
                "error": str(e)
            }
    
    def _extract_intent(self, query: str) -> str:
        """Extract the main intent of the query."""
        query_lower = query.lower()
        
        # Define intent patterns
        intent_patterns = {
            "list": ["show", "list", "get", "find", "display", "retrieve"],
            "count": ["count", "how many", "total number", "number of"],
            "filter": ["where", "filter", "only", "just", "with"],
            "compare": ["compare", "versus", "vs", "difference", "between"],
            "aggregate": ["sum", "average", "total", "maximum", "minimum"],
            "search": ["search", "look for", "find", "locate"]
        }
        
        for intent, patterns in intent_patterns.items():
            if any(pattern in query_lower for pattern in patterns):
                return intent
        
        return "list"  # Default intent
    
    def _extract_keywords(self, query: str) -> List[str]:
        """Extract relevant keywords from the query."""
        # Remove common words
        stop_words = {
            "the", "a", "an", "and", "or", "but", "in", "on", "at", "to", "for", 
            "of", "with", "by", "is", "are", "was", "were", "be", "been", "being",
            "have", "has", "had", "do", "does", "did", "will", "would", "could",
            "should", "may", "might", "can", "this", "that", "these", "those"
        }
        
        # Extract words
        words = re.findall(r'\b\w+\b', query.lower())
        
        # Filter out stop words and short words
        keywords = [word for word in words if word not in stop_words and len(word) > 2]
        
        # Add domain-specific keywords
        domain_keywords = [
            "case", "defendant", "officer", "evidence", "test", "report",
            "blood", "alcohol", "bac", "sobriety", "field", "vehicle",
            "offense", "charge", "court", "date", "time", "location"
        ]
        
        # Add domain keywords if found
        for keyword in domain_keywords:
            if keyword in query.lower() and keyword not in keywords:
                keywords.append(keyword)
        
        return list(set(keywords))
    
    def _extract_requirements(self, query: str) -> Dict[str, Any]:
        """Extract specific requirements from the query."""
        requirements = {
            "time_filter": None,
            "value_filter": None,
            "sort_order": None,
            "limit": None,
            "group_by": None
        }
        
        query_lower = query.lower()
        
        # Extract time filters
        time_patterns = {
            "last_30_days": r"last\s+30\s+days?|past\s+30\s+days?|recent\s+30\s+days?",
            "last_month": r"last\s+month|past\s+month|recent\s+month",
            "last_week": r"last\s+week|past\s+week|recent\s+week",
            "today": r"today|current\s+day",
            "yesterday": r"yesterday"
        }
        
        for time_type, pattern in time_patterns.items():
            if re.search(pattern, query_lower):
                requirements["time_filter"] = time_type
                break
        
        # Extract value filters
        value_patterns = {
            "above": r"above\s+(\d+\.?\d*)",
            "below": r"below\s+(\d+\.?\d*)",
            "over": r"over\s+(\d+\.?\d*)",
            "under": r"under\s+(\d+\.?\d*)"
        }
        
        for filter_type, pattern in value_patterns.items():
            match = re.search(pattern, query_lower)
            if match:
                requirements["value_filter"] = {
                    "type": filter_type,
                    "value": float(match.group(1))
                }
                break
        
        # Extract sort order
        if "highest" in query_lower or "top" in query_lower:
            requirements["sort_order"] = "desc"
        elif "lowest" in query_lower or "bottom" in query_lower:
            requirements["sort_order"] = "asc"
        
        # Extract limit
        limit_match = re.search(r"top\s+(\d+)", query_lower)
        if limit_match:
            requirements["limit"] = int(limit_match.group(1))
        
        return requirements
    
    def _classify_query_type(self, query: str) -> str:
        """Classify the type of query."""
        query_lower = query.lower()
        
        if any(word in query_lower for word in ["count", "how many", "total"]):
            return "aggregation"
        elif any(word in query_lower for word in ["compare", "versus", "vs"]):
            return "comparison"
        elif any(word in query_lower for word in ["where", "filter", "only"]):
            return "filtered"
        elif any(word in query_lower for word in ["list", "show", "get"]):
            return "listing"
        else:
            return "general"
    
    def _assess_complexity(self, query: str) -> str:
        """Assess the complexity of the query."""
        complexity_score = 0
        
        # Count clauses
        if "where" in query.lower():
            complexity_score += 1
        if "order by" in query.lower():
            complexity_score += 1
        if "group by" in query.lower():
            complexity_score += 1
        if "join" in query.lower():
            complexity_score += 2
        
        # Count conditions
        conditions = query.lower().count("and") + query.lower().count("or")
        complexity_score += conditions
        
        if complexity_score <= 1:
            return "simple"
        elif complexity_score <= 3:
            return "moderate"
        else:
            return "complex"
