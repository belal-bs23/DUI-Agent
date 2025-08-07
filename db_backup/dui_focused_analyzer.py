#!/usr/bin/env python3
"""
Focused DUI Database Analyzer
Analyzes DUI schema tables and generates comprehensive views based on real data.
"""

import pyodbc
import json
from pathlib import Path
from typing import Dict, List, Set, Tuple, Any
import re
from datetime import datetime

# Connection details for DUI schema
DRIVER = "ODBC Driver 17 for SQL Server"
SERVER = "localhost\\SQLEXPRESS"
DATABASE = "LEADRS_DUI_STAGE"
conn_str = f"DRIVER={{{DRIVER}}};SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection=yes"

class DUIFocusedAnalyzer:
    """Focused analyzer for DUI schema tables."""
    
    def __init__(self):
        self.connection = None
        self.dui_tables = set()
        self.tables_info = {}
        self.relationships = {}
        
    def connect(self):
        """Establish database connection."""
        try:
            self.connection = pyodbc.connect(conn_str)
            print("✅ Database connection established")
            return True
        except Exception as e:
            print(f"❌ Database connection failed: {e}")
            return False
    
    def disconnect(self):
        """Close database connection."""
        if self.connection:
            self.connection.close()
            print("✅ Database connection closed")
    
    def identify_dui_tables(self) -> List[str]:
        """Get all tables in the DUI schema."""
        cursor = self.connection.cursor()
        
        # Get all tables in DUI schema
        query = """
        SELECT TABLE_NAME 
        FROM INFORMATION_SCHEMA.TABLES 
        WHERE TABLE_TYPE = 'BASE TABLE' 
        AND TABLE_SCHEMA = 'DUI'
        ORDER BY TABLE_NAME
        """
        cursor.execute(query)
        dui_tables = [row[0] for row in cursor.fetchall()]
        
        cursor.close()
        return sorted(dui_tables)
    
    def get_table_columns(self, table_name: str) -> List[Dict]:
        """Get detailed column information for a table."""
        cursor = self.connection.cursor()
        query = """
        SELECT 
            COLUMN_NAME,
            DATA_TYPE,
            IS_NULLABLE,
            COLUMN_DEFAULT,
            CHARACTER_MAXIMUM_LENGTH,
            NUMERIC_PRECISION,
            NUMERIC_SCALE
        FROM INFORMATION_SCHEMA.COLUMNS 
        WHERE TABLE_NAME = ? 
        AND TABLE_SCHEMA = 'DUI'
        ORDER BY ORDINAL_POSITION
        """
        cursor.execute(query, table_name)
        columns = []
        for row in cursor.fetchall():
            columns.append({
                "name": row[0],
                "data_type": row[1],
                "is_nullable": row[2],
                "default_value": row[3],
                "max_length": row[4],
                "numeric_precision": row[5],
                "numeric_scale": row[6]
            })
        cursor.close()
        return columns
    
    def get_primary_keys(self, table_name: str) -> List[str]:
        """Get primary key columns for a table."""
        cursor = self.connection.cursor()
        query = """
        SELECT COLUMN_NAME
        FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
        WHERE TABLE_NAME = ? 
        AND TABLE_SCHEMA = 'DUI'
        AND CONSTRAINT_NAME LIKE '%PK%'
        """
        cursor.execute(query, table_name)
        pk_columns = [row[0] for row in cursor.fetchall()]
        cursor.close()
        return pk_columns
    
    def get_foreign_keys(self, table_name: str) -> List[Dict]:
        """Get foreign key relationships for a table."""
        cursor = self.connection.cursor()
        query = """
        SELECT 
            fk.COLUMN_NAME,
            fk.CONSTRAINT_NAME,
            pk.TABLE_NAME as REFERENCED_TABLE_NAME,
            pk.COLUMN_NAME as REFERENCED_COLUMN_NAME
        FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE fk
        INNER JOIN INFORMATION_SCHEMA.REFERENTIAL_CONSTRAINTS rc 
            ON fk.CONSTRAINT_NAME = rc.CONSTRAINT_NAME
        INNER JOIN INFORMATION_SCHEMA.KEY_COLUMN_USAGE pk 
            ON rc.UNIQUE_CONSTRAINT_NAME = pk.CONSTRAINT_NAME
        WHERE fk.TABLE_NAME = ? 
        AND fk.TABLE_SCHEMA = 'DUI'
        """
        cursor.execute(query, table_name)
        foreign_keys = []
        for row in cursor.fetchall():
            foreign_keys.append({
                "column_name": row[0],
                "constraint_name": row[1],
                "referenced_table": row[2],
                "referenced_column": row[3]
            })
        cursor.close()
        return foreign_keys
    
    def get_data_sample(self, table_name: str, limit: int = 5) -> List[Dict]:
        """Get sample data from a table."""
        cursor = self.connection.cursor()
        try:
            query = f"SELECT TOP {limit} * FROM {table_name}"
            cursor.execute(query)
            
            # Get column names
            columns = [column[0] for column in cursor.description]
            
            # Get sample data
            sample_data = []
            for row in cursor.fetchall():
                row_dict = {}
                for i, value in enumerate(row):
                    # Convert non-serializable types
                    if isinstance(value, (datetime, bytes)):
                        row_dict[columns[i]] = str(value)
                    else:
                        row_dict[columns[i]] = value
                sample_data.append(row_dict)
            
            cursor.close()
            return sample_data
        except Exception as e:
            print(f"  ⚠️  Could not sample data from {table_name}: {e}")
            cursor.close()
            return []
    
    def analyze_table_relationships(self, table_name: str) -> Dict:
        """Analyze relationships for a table."""
        primary_keys = self.get_primary_keys(table_name)
        foreign_keys = self.get_foreign_keys(table_name)
        
        # Find tables that reference this table
        cursor = self.connection.cursor()
        query = """
        SELECT 
            fk.TABLE_NAME, 
            fk.COLUMN_NAME
        FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE fk
        INNER JOIN INFORMATION_SCHEMA.REFERENTIAL_CONSTRAINTS rc 
            ON fk.CONSTRAINT_NAME = rc.CONSTRAINT_NAME
        INNER JOIN INFORMATION_SCHEMA.KEY_COLUMN_USAGE pk 
            ON rc.UNIQUE_CONSTRAINT_NAME = pk.CONSTRAINT_NAME
        WHERE pk.TABLE_NAME = ? 
        AND pk.TABLE_SCHEMA = 'DUI'
        """
        cursor.execute(query, table_name)
        referenced_by = []
        for row in cursor.fetchall():
            referenced_by.append({
                "table": row[0],
                "column": row[1]
            })
        cursor.close()
        
        return {
            "primary_keys": primary_keys,
            "foreign_keys": foreign_keys,
            "referenced_by": referenced_by
        }
    
    def generate_column_description(self, table_name: str, column_name: str, column_info: Dict) -> str:
        """Generate a description for a column based on its properties."""
        data_type = column_info["data_type"]
        is_nullable = column_info["is_nullable"]
        
        # Base description from column name
        name_parts = re.findall(r'[A-Z][a-z]*', column_name)
        base_desc = ' '.join(name_parts).lower()
        
        # Enhance based on data type and patterns
        if column_name.lower() in ['id', 'pk']:
            return f"Primary key identifier for {table_name}"
        elif column_name.lower().endswith('id'):
            return f"Foreign key reference to related table"
        elif column_name.lower() in ['created', 'createddate', 'createdat']:
            return f"Timestamp when the record was created"
        elif column_name.lower() in ['modified', 'modifieddate', 'modifiedat', 'updated', 'updatedat']:
            return f"Timestamp when the record was last modified"
        elif column_name.lower() in ['isactive', 'active', 'enabled']:
            return f"Flag indicating if the record is active/enabled"
        elif data_type in ['bit', 'boolean']:
            return f"Boolean flag: {base_desc}"
        elif data_type in ['datetime', 'datetime2', 'date']:
            return f"Date/time value: {base_desc}"
        elif data_type in ['int', 'bigint', 'smallint']:
            return f"Numeric identifier or count: {base_desc}"
        elif data_type in ['varchar', 'nvarchar', 'char', 'nchar']:
            return f"Text field: {base_desc}"
        else:
            return f"{data_type} field: {base_desc}"
    
    def analyze_dui_tables(self):
        """Analyze all DUI-related tables."""
        print("🔍 Starting focused DUI database analysis...")
        
        if not self.connect():
            return False
        
        try:
            # Identify DUI tables
            dui_tables = self.identify_dui_tables()
            print(f"📋 Found {len(dui_tables)} DUI-related tables: {', '.join(dui_tables)}")
            
            # Analyze each DUI table
            for table_name in dui_tables:
                print(f"\n📊 Analyzing DUI table: {table_name}")
                
                # Get table structure
                columns = self.get_table_columns(table_name)
                relationships = self.analyze_table_relationships(table_name)
                sample_data = self.get_data_sample(table_name, 3)
                
                # Generate column descriptions
                column_descriptions = {}
                for column in columns:
                    column_name = column["name"]
                    description = self.generate_column_description(table_name, column_name, column)
                    column_descriptions[column_name] = {
                        "description": description,
                        "column_info": column
                    }
                
                self.tables_info[table_name] = {
                    "columns": columns,
                    "relationships": relationships,
                    "sample_data": sample_data,
                    "column_descriptions": column_descriptions
                }
            
            # Save analysis results
            self.save_analysis_results()
            
            print(f"\n✅ DUI analysis complete! Analyzed {len(dui_tables)} tables")
            return True
            
        except Exception as e:
            print(f"❌ Analysis failed: {e}")
            import traceback
            traceback.print_exc()
            return False
        finally:
            self.disconnect()
    
    def save_analysis_results(self):
        """Save analysis results to JSON files."""
        
        # Save table information
        analysis_file = Path("db_backup/dui_database_analysis.json")
        analysis_data = {
            "analysis_date": datetime.now().isoformat(),
            "tables": self.tables_info,
            "summary": {
                "total_tables": len(self.tables_info),
                "total_columns": sum(len(info["columns"]) for info in self.tables_info.values()),
                "tables_with_relationships": len([t for t in self.tables_info.values() if t["relationships"]["foreign_keys"]])
            }
        }
        
        with open(analysis_file, 'w', encoding='utf-8') as f:
            json.dump(analysis_data, f, indent=2)
        
        print(f"✅ Analysis results saved to: {analysis_file}")
    
    def generate_relationship_summary(self) -> str:
        """Generate a summary of all table relationships."""
        summary = "DUI Database Relationship Summary:\n\n"
        
        for table_name, table_info in self.tables_info.items():
            relationships = table_info["relationships"]
            
            summary += f"📋 {table_name}:\n"
            summary += f"  Primary Keys: {', '.join(relationships['primary_keys'])}\n"
            
            if relationships["foreign_keys"]:
                summary += f"  Foreign Keys:\n"
                for fk in relationships["foreign_keys"]:
                    summary += f"    {fk['column_name']} → {fk['referenced_table']}.{fk['referenced_column']}\n"
            
            if relationships["referenced_by"]:
                summary += f"  Referenced by:\n"
                for ref in relationships["referenced_by"]:
                    summary += f"    {ref['table']}.{ref['column']} → {table_name}\n"
            
            summary += "\n"
        
        return summary

def main():
    """Main function to run DUI database analysis."""
    print("DUI Focused Database Analyzer")
    print("=" * 50)
    
    analyzer = DUIFocusedAnalyzer()
    
    if analyzer.analyze_dui_tables():
        print("\n" + "=" * 50)
        print("DUI RELATIONSHIP SUMMARY")
        print("=" * 50)
        print(analyzer.generate_relationship_summary())
        
        print("\n🎯 Next steps:")
        print("1. Review dui_database_analysis.json for detailed information")
        print("2. Use the analysis to create comprehensive DUI views")
        print("3. Generate view descriptions based on column analysis")
    else:
        print("❌ DUI database analysis failed")

if __name__ == "__main__":
    main() 