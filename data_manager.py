#!/usr/bin/env python3
"""
Data Manager for Multi-Agent DUI SQL System
Handles data restructuring, caching, and efficient data fetching.
"""

import json
import os
from pathlib import Path
from typing import Dict, List, Optional, Any
import logging

logger = logging.getLogger(__name__)

class DataManager:
    """Manages data storage, caching, and retrieval for multi-agent system."""
    
    def __init__(self, data_dir: str = "data"):
        self.data_dir = Path(data_dir)
        self.cache = {}
        self.view_names = []
        self.view_categories = {}
        self.view_relationships = {}
        
        # Ensure data directory exists
        self.data_dir.mkdir(exist_ok=True)
        (self.data_dir / "views" / "schemas").mkdir(parents=True, exist_ok=True)
        (self.data_dir / "analysis").mkdir(exist_ok=True)
        (self.data_dir / "cache").mkdir(exist_ok=True)
        
        # Initialize data
        self._initialize_data()
    
    def _initialize_data(self):
        """Initialize data by restructuring large JSON files."""
        logger.info("🔧 Initializing Data Manager...")
        
        # Check if data is already restructured
        if self._is_data_restructured():
            logger.info("✅ Data already restructured, loading...")
            self._load_restructured_data()
        else:
            logger.info("🔄 Restructuring data...")
            self._restructure_data()
            self._load_restructured_data()
        
        logger.info(f"✅ Data Manager initialized with {len(self.view_names)} views")
    
    def _is_data_restructured(self) -> bool:
        """Check if data has been restructured."""
        view_names_file = self.data_dir / "views" / "view_names.json"
        return view_names_file.exists()
    
    def _restructure_data(self):
        """Restructure large JSON files into smaller, focused files."""
        try:
            # Load original data
            schema_file = Path("db_backup/comprehensive_dui_view_schema.json")
            analysis_file = Path("db_backup/dui_database_analysis.json")
            
            if not schema_file.exists() or not analysis_file.exists():
                raise FileNotFoundError("Original data files not found")
            
            # Load schema data
            with open(schema_file, 'r', encoding='utf-8') as f:
                schema_data = json.load(f)
            
            # Load analysis data
            with open(analysis_file, 'r', encoding='utf-8') as f:
                analysis_data = json.load(f)
            
            # Extract views from schema
            views = schema_data.get('views', {})
            
            # Create view names list
            view_names = []
            view_categories = {}
            view_relationships = {}
            
            for view_name, view_data in views.items():
                view_names.append({
                    "name": view_name,
                    "description": view_data.get('description', ''),
                    "columns_count": len(view_data.get('columns', [])),
                    "type": self._categorize_view(view_name, view_data)
                })
                
                # Categorize view
                category = self._categorize_view(view_name, view_data)
                if category not in view_categories:
                    view_categories[category] = []
                view_categories[category].append(view_name)
                
                # Store individual view schema
                schema_file_path = self.data_dir / "views" / "schemas" / f"{view_name}.json"
                with open(schema_file_path, 'w', encoding='utf-8') as f:
                    json.dump(view_data, f, indent=2)
            
            # Save view names
            with open(self.data_dir / "views" / "view_names.json", 'w', encoding='utf-8') as f:
                json.dump(view_names, f, indent=2)
            
            # Save view categories
            with open(self.data_dir / "views" / "view_categories.json", 'w', encoding='utf-8') as f:
                json.dump(view_categories, f, indent=2)
            
            # Save view relationships
            with open(self.data_dir / "views" / "view_relationships.json", 'w', encoding='utf-8') as f:
                json.dump(view_relationships, f, indent=2)
            
            # Save analysis summary
            analysis_summary = {
                "total_views": len(views),
                "total_tables": analysis_data.get('total_tables', 0),
                "database_name": analysis_data.get('database_name', ''),
                "last_updated": analysis_data.get('last_updated', ''),
                "key_statistics": {
                    "primary_views": len([v for v in view_names if v['type'] == 'primary']),
                    "supporting_views": len([v for v in view_names if v['type'] == 'supporting']),
                    "reference_views": len([v for v in view_names if v['type'] == 'reference'])
                }
            }
            
            with open(self.data_dir / "analysis" / "database_summary.json", 'w', encoding='utf-8') as f:
                json.dump(analysis_summary, f, indent=2)
            
            logger.info(f"✅ Restructured {len(views)} views into individual files")
            
        except Exception as e:
            logger.error(f"❌ Failed to restructure data: {e}")
            raise
    
    def _categorize_view(self, view_name: str, view_data: Dict) -> str:
        """Categorize a view based on its name and data."""
        name_lower = view_name.lower()
        
        # Primary views (high-volume data)
        if any(keyword in name_lower for keyword in ['case', 'defendant', 'offense', 'evidence']):
            return 'primary'
        
        # Supporting views (medium-volume data)
        if any(keyword in name_lower for keyword in ['officer', 'vehicle', 'test', 'report']):
            return 'supporting'
        
        # Reference views (lookup data)
        if any(keyword in name_lower for keyword in ['lookup', 'reference', 'type', 'status']):
            return 'reference'
        
        return 'supporting'
    
    def _load_restructured_data(self):
        """Load restructured data into memory."""
        try:
            # Load view names
            with open(self.data_dir / "views" / "view_names.json", 'r', encoding='utf-8') as f:
                view_data = json.load(f)
                self.view_names = [v['name'] for v in view_data]
            
            # Load view categories
            with open(self.data_dir / "views" / "view_categories.json", 'r', encoding='utf-8') as f:
                self.view_categories = json.load(f)
            
            # Load view relationships
            with open(self.data_dir / "views" / "view_relationships.json", 'r', encoding='utf-8') as f:
                self.view_relationships = json.load(f)
            
            logger.info(f"✅ Loaded {len(self.view_names)} view names")
            
        except Exception as e:
            logger.error(f"❌ Failed to load restructured data: {e}")
            raise
    
    def get_view_names(self) -> List[str]:
        """Get all view names (~1KB)."""
        return self.view_names.copy()
    
    def get_view_names_with_descriptions(self) -> List[Dict]:
        """Get view names with descriptions (~2KB)."""
        try:
            with open(self.data_dir / "views" / "view_names.json", 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            logger.error(f"❌ Failed to load view names with descriptions: {e}")
            return []
    
    def get_view_categories(self) -> Dict:
        """Get view categories (~2KB)."""
        return self.view_categories.copy()
    
    def get_view_schema(self, view_name: str) -> Optional[Dict]:
        """Get schema for specific view (~2-5KB)."""
        if view_name not in self.cache:
            try:
                schema_file = self.data_dir / "views" / "schemas" / f"{view_name}.json"
                if schema_file.exists():
                    with open(schema_file, 'r', encoding='utf-8') as f:
                        self.cache[view_name] = json.load(f)
                else:
                    logger.warning(f"⚠️ Schema file not found for view: {view_name}")
                    return None
            except Exception as e:
                logger.error(f"❌ Failed to load schema for {view_name}: {e}")
                return None
        
        return self.cache[view_name]
    
    def get_view_schemas(self, view_names: List[str]) -> Dict:
        """Get schemas for multiple views (~10-15KB)."""
        schemas = {}
        for view_name in view_names:
            schema = self.get_view_schema(view_name)
            if schema:
                schemas[view_name] = schema
        
        return schemas
    
    def get_database_summary(self) -> Dict:
        """Get database summary (~5KB)."""
        try:
            with open(self.data_dir / "analysis" / "database_summary.json", 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            logger.error(f"❌ Failed to load database summary: {e}")
            return {}
    
    def get_views_by_category(self, category: str) -> List[str]:
        """Get views by category."""
        return self.view_categories.get(category, [])
    
    def search_views(self, keywords: List[str]) -> List[str]:
        """Search views by keywords."""
        matching_views = []
        view_data = self.get_view_names_with_descriptions()
        
        for view in view_data:
            name_lower = view['name'].lower()
            desc_lower = view.get('description', '').lower()
            
            for keyword in keywords:
                if keyword.lower() in name_lower or keyword.lower() in desc_lower:
                    matching_views.append(view['name'])
                    break
        
        return list(set(matching_views))
    
    def get_cache_stats(self) -> Dict:
        """Get cache statistics."""
        return {
            "cached_views": len(self.cache),
            "total_views": len(self.view_names),
            "cache_hit_ratio": len(self.cache) / len(self.view_names) if self.view_names else 0
        }
    
    def clear_cache(self):
        """Clear the cache."""
        self.cache.clear()
        logger.info("🧹 Cache cleared")
    
    def preload_common_views(self):
        """Preload commonly used views."""
        common_views = [
            "v_caseheaders",
            "v_defendants", 
            "v_caseoffenses_with_caseheaders",
            "v_specimenreport_with_caseheaders",
            "v_fieldsobrietytests"
        ]
        
        for view_name in common_views:
            if view_name in self.view_names:
                self.get_view_schema(view_name)
        
        logger.info(f"✅ Preloaded {len(common_views)} common views")

# Global data manager instance
_data_manager = None

def get_data_manager() -> DataManager:
    """Get the global data manager instance."""
    global _data_manager
    if _data_manager is None:
        _data_manager = DataManager()
    return _data_manager
