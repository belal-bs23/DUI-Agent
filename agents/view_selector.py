#!/usr/bin/env python3
"""
View Selector Agent
Selects the most relevant views based on query analysis.
Context: ~1KB
"""

import json
from typing import Dict, List, Any
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate
import logging

logger = logging.getLogger(__name__)

class ViewSelectorAgent:
    """Selects the most relevant views for a given query."""
    
    def __init__(self, data_manager):
        self.data_manager = data_manager
        self.view_mapping = {
            # Case-related views
            "case": ["v_caseheaders", "v_caseoffenses_with_caseheaders"],
            "defendant": ["v_defendants", "v_defendants_with_caseheaders"],
            "offense": ["v_caseoffenses_with_caseheaders", "v_tbl_opt_offense"],
            
            # Evidence and testing views
            "evidence": ["v_physicalevidence", "v_physicalevidence_with_caseheaders"],
            "blood": ["v_specimenreport_with_caseheaders"],
            "alcohol": ["v_specimenreport_with_caseheaders"],
            "bac": ["v_specimenreport_with_caseheaders"],
            "test": ["v_fieldsobrietytests", "v_specimenreport_with_caseheaders"],
            "sobriety": ["v_fieldsobrietytests"],
            "field": ["v_fieldsobrietytests"],
            
            # Officer and personnel views
            "officer": ["v_otherofficers_with_caseheaders", "v_officers"],
            "personnel": ["v_otherofficers_with_caseheaders", "v_officers"],
            
            # Vehicle and property views
            "vehicle": ["v_vehicles", "v_vehicles_with_caseheaders"],
            "property": ["v_vehicles", "v_vehicles_with_caseheaders"],
            
            # Time and date related
            "time": ["v_caseoffenses_with_caseheaders"],
            "date": ["v_caseoffenses_with_caseheaders"],
            "month": ["v_caseoffenses_with_caseheaders"],
            "last": ["v_caseoffenses_with_caseheaders"],
            
            # Court and legal
            "court": ["v_caseheaders"],
            "legal": ["v_caseheaders"],
            
            # Location and geography
            "location": ["v_caseheaders"],
            "address": ["v_caseheaders"],
            
            # Statistics and reporting
            "statistics": ["v_caseheaders", "v_caseoffenses_with_caseheaders"],
            "report": ["v_specimenreport_with_caseheaders", "v_fieldsobrietytests"],
            "summary": ["v_caseheaders", "v_caseoffenses_with_caseheaders"]
        }
    
    def select_views(self, query_analysis: Dict[str, Any]) -> List[str]:
        """Select the most relevant views based on query analysis."""
        try:
            keywords = query_analysis.get("keywords", [])
            intent = query_analysis.get("intent", "list")
            query_type = query_analysis.get("query_type", "general")
            
            # Get all available views
            available_views = self.data_manager.get_view_names()
            
            # Score views based on keywords
            view_scores = self._score_views(keywords, available_views)
            
            # Apply intent-based filtering
            filtered_views = self._filter_by_intent(view_scores, intent, query_type)
            
            # Select top views (limit to 3-5)
            selected_views = self._select_top_views(filtered_views, max_views=5)
            
            # Ensure we have at least one view
            if not selected_views:
                selected_views = ["v_caseheaders"]  # Default fallback
            
            logger.info(f"🎯 Selected views: {selected_views}")
            return selected_views
            
        except Exception as e:
            logger.error(f"❌ View selection failed: {e}")
            return ["v_caseheaders"]  # Fallback
    
    def _score_views(self, keywords: List[str], available_views: List[str]) -> Dict[str, float]:
        """Score views based on keyword relevance."""
        view_scores = {}
        
        for view_name in available_views:
            score = 0.0
            
            # Score based on direct keyword matches
            for keyword in keywords:
                if keyword.lower() in view_name.lower():
                    score += 2.0  # High score for direct matches
                
                # Check view mapping
                if keyword.lower() in self.view_mapping:
                    if view_name in self.view_mapping[keyword.lower()]:
                        score += 3.0  # Very high score for mapped views
            
            # Score based on view category
            view_category = self._get_view_category(view_name)
            if view_category == "primary":
                score += 0.5  # Bonus for primary views
            elif view_category == "supporting":
                score += 0.3  # Bonus for supporting views
            
            # Score based on view name patterns
            if "_with_caseheaders" in view_name:
                score += 1.0  # Bonus for pre-joined views
            
            if score > 0:
                view_scores[view_name] = score
        
        return view_scores
    
    def _filter_by_intent(self, view_scores: Dict[str, float], intent: str, query_type: str) -> Dict[str, float]:
        """Filter views based on query intent and type."""
        filtered_scores = view_scores.copy()
        
        if intent == "count" or query_type == "aggregation":
            # Prefer views with case headers for counting
            for view_name, score in view_scores.items():
                if "_with_caseheaders" in view_name:
                    filtered_scores[view_name] = score * 1.5
        
        elif intent == "filter" or query_type == "filtered":
            # Prefer detailed views for filtering
            for view_name, score in view_scores.items():
                if "detailed" in view_name.lower() or "full" in view_name.lower():
                    filtered_scores[view_name] = score * 1.3
        
        elif intent == "compare" or query_type == "comparison":
            # Prefer summary views for comparisons
            for view_name, score in view_scores.items():
                if "summary" in view_name.lower():
                    filtered_scores[view_name] = score * 1.4
        
        return filtered_scores
    
    def _select_top_views(self, view_scores: Dict[str, float], max_views: int = 5) -> List[str]:
        """Select the top-scoring views."""
        # Sort views by score (descending)
        sorted_views = sorted(view_scores.items(), key=lambda x: x[1], reverse=True)
        
        # Select top views
        selected_views = []
        for view_name, score in sorted_views[:max_views]:
            if score > 0.5:  # Minimum score threshold
                selected_views.append(view_name)
        
        # Ensure we have a good mix of view types
        selected_views = self._balance_view_selection(selected_views)
        
        return selected_views
    
    def _balance_view_selection(self, selected_views: List[str]) -> List[str]:
        """Balance view selection to include different types."""
        if len(selected_views) <= 3:
            return selected_views
        
        # Ensure we have at least one case-related view
        case_views = [v for v in selected_views if "case" in v.lower()]
        if not case_views and len(selected_views) > 0:
            # Add a case view if none selected
            available_case_views = ["v_caseheaders", "v_caseoffenses_with_caseheaders"]
            for case_view in available_case_views:
                if case_view in self.data_manager.get_view_names():
                    selected_views.insert(0, case_view)
                    break
        
        # Limit to top 5 views
        return selected_views[:5]
    
    def _get_view_category(self, view_name: str) -> str:
        """Get the category of a view."""
        view_categories = self.data_manager.get_view_categories()
        
        for category, views in view_categories.items():
            if view_name in views:
                return category
        
        return "supporting"  # Default category
    
    def get_view_recommendations(self, query_analysis: Dict[str, Any]) -> Dict[str, Any]:
        """Get detailed view recommendations with explanations."""
        selected_views = self.select_views(query_analysis)
        
        recommendations = {
            "selected_views": selected_views,
            "reasoning": self._explain_selection(query_analysis, selected_views),
            "alternatives": self._get_alternatives(selected_views),
            "estimated_context_size": len(selected_views) * 3  # ~3KB per view
        }
        
        return recommendations
    
    def _explain_selection(self, query_analysis: Dict[str, Any], selected_views: List[str]) -> str:
        """Explain why these views were selected."""
        keywords = query_analysis.get("keywords", [])
        intent = query_analysis.get("intent", "list")
        
        explanations = []
        
        for view_name in selected_views:
            if any(keyword.lower() in view_name.lower() for keyword in keywords):
                explanations.append(f"{view_name}: Direct keyword match")
            elif "_with_caseheaders" in view_name:
                explanations.append(f"{view_name}: Pre-joined with case data")
            else:
                explanations.append(f"{view_name}: Related to query intent ({intent})")
        
        return "; ".join(explanations)
    
    def _get_alternatives(self, selected_views: List[str]) -> List[str]:
        """Get alternative views that could be used."""
        alternatives = []
        available_views = self.data_manager.get_view_names()
        
        # Find similar views
        for view_name in available_views:
            if view_name not in selected_views:
                # Check if it's similar to selected views
                for selected_view in selected_views:
                    if self._are_views_similar(view_name, selected_view):
                        alternatives.append(view_name)
                        break
        
        return alternatives[:3]  # Return top 3 alternatives
    
    def _are_views_similar(self, view1: str, view2: str) -> bool:
        """Check if two views are similar."""
        # Extract base names (remove suffixes)
        base1 = view1.replace("_with_caseheaders", "").replace("_detailed", "")
        base2 = view2.replace("_with_caseheaders", "").replace("_detailed", "")
        
        return base1 == base2
