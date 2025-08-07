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

class DatabaseAnalyzer:
    """Comprehensive database analyzer for DUI schema."""
    
    def __init__(self):
        self.connection = None
        self.tables_info = {}
        self.relationships = {}
        self.column_descriptions = {}
        self.data_samples = {}
        
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
    
    def get_all_tables(self) -> List[str]:
        """Get all tables in the database."""
        cursor = self.connection.cursor()
        query = """
        SELECT TABLE_NAME 
        FROM INFORMATION_SCHEMA.TABLES 
        WHERE TABLE_TYPE = 'BASE TABLE' 
        AND TABLE_SCHEMA = 'DUI'
        ORDER BY TABLE_NAME
        """
        cursor.execute(query)
        tables = [row[0] for row in cursor.fetchall()]
        cursor.close()
        return tables
    
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
            COLUMN_NAME,
            CONSTRAINT_NAME,
            REFERENCED_TABLE_NAME,
            REFERENCED_COLUMN_NAME
        FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
        WHERE TABLE_NAME = ? 
        AND TABLE_SCHEMA = 'DUI'
        AND REFERENCED_TABLE_NAME IS NOT NULL
        """
        cursor.execute(query, table_name)
        fk_relationships = []
        for row in cursor.fetchall():
            fk_relationships.append({
                "column_name": row[0],
                "constraint_name": row[1],
                "referenced_table": row[2],
                "referenced_column": row[3]
            })
        cursor.close()
        return fk_relationships
    
    def get_data_sample(self, table_name: str, limit: int = 10) -> List[Dict]:
        """Get sample data from a table to understand content."""
        cursor = self.connection.cursor()
        try:
            query = f"SELECT TOP {limit} * FROM {table_name}"
            cursor.execute(query)
            
            # Get column names
            columns = [column[0] for column in cursor.description]
            
            # Get sample data
            sample_data = []
            for row in cursor.fetchall():
                sample_data.append(dict(zip(columns, row)))
            
            cursor.close()
            return sample_data
        except Exception as e:
            print(f"Warning: Could not get sample data for {table_name}: {e}")
            cursor.close()
            return []
    
    def analyze_column_content(self, table_name: str, column_name: str) -> Dict:
        """Analyze column content to understand its purpose."""
        cursor = self.connection.cursor()
        analysis = {
            "unique_values": 0,
            "null_count": 0,
            "sample_values": [],
            "data_patterns": [],
            "suggested_description": ""
        }
        
        try:
            # Get basic statistics
            query = f"""
            SELECT 
                COUNT(*) as total_count,
                COUNT(DISTINCT {column_name}) as unique_count,
                COUNT(CASE WHEN {column_name} IS NULL THEN 1 END) as null_count
            FROM {table_name}
            """
            cursor.execute(query)
            stats = cursor.fetchone()
            
            if stats:
                analysis["unique_values"] = stats[1]
                analysis["null_count"] = stats[2]
            
            # Get sample values
            query = f"""
            SELECT DISTINCT TOP 5 {column_name}
            FROM {table_name}
            WHERE {column_name} IS NOT NULL
            ORDER BY {column_name}
            """
            cursor.execute(query)
            sample_values = [row[0] for row in cursor.fetchall()]
            analysis["sample_values"] = sample_values
            
            # Analyze patterns
            if sample_values:
                # Check for common patterns
                if any('id' in str(val).lower() for val in sample_values):
                    analysis["data_patterns"].append("ID")
                if any('date' in str(val).lower() for val in sample_values):
                    analysis["data_patterns"].append("Date")
                if any('name' in str(val).lower() for val in sample_values):
                    analysis["data_patterns"].append("Name")
                if any('code' in str(val).lower() for val in sample_values):
                    analysis["data_patterns"].append("Code")
                if any('status' in str(val).lower() for val in sample_values):
                    analysis["data_patterns"].append("Status")
            
            cursor.close()
        except Exception as e:
            print(f"Warning: Could not analyze column {table_name}.{column_name}: {e}")
            cursor.close()
        
        return analysis
    
    def generate_column_description(self, table_name: str, column_name: str, column_info: Dict, content_analysis: Dict) -> str:
        """Generate a meaningful description for a column based on its structure and content."""
        
        # Base description from column name
        column_lower = column_name.lower()
        description = ""
        
        # Common patterns
        if 'id' in column_lower:
            if column_lower.endswith('id'):
                description = f"Unique identifier for {column_lower[:-2]}"
            else:
                description = f"Identifier field for {column_lower.replace('id', '')}"
        elif 'name' in column_lower:
            description = f"Name of the {column_lower.replace('name', '')}"
        elif 'date' in column_lower:
            description = f"Date when {column_lower.replace('date', '')} occurred"
        elif 'time' in column_lower:
            description = f"Time when {column_lower.replace('time', '')} occurred"
        elif 'status' in column_lower:
            description = f"Current status of the {column_lower.replace('status', '')}"
        elif 'type' in column_lower:
            description = f"Type or category of the {column_lower.replace('type', '')}"
        elif 'code' in column_lower:
            description = f"Code representing {column_lower.replace('code', '')}"
        elif 'description' in column_lower:
            description = f"Detailed description of the {column_lower.replace('description', '')}"
        elif 'count' in column_lower:
            description = f"Number of {column_lower.replace('count', '')}"
        elif 'amount' in column_lower:
            description = f"Monetary amount for {column_lower.replace('amount', '')}"
        elif 'result' in column_lower:
            description = f"Result of {column_lower.replace('result', '')}"
        elif 'test' in column_lower:
            description = f"Test result for {column_lower.replace('test', '')}"
        elif 'bac' in column_lower:
            description = "Blood Alcohol Content level"
        elif 'officer' in column_lower:
            description = f"Information about the {column_lower.replace('officer', '')} officer"
        elif 'defendant' in column_lower:
            description = f"Information about the {column_lower.replace('defendant', '')} defendant"
        elif 'vehicle' in column_lower:
            description = f"Information about the {column_lower.replace('vehicle', '')} vehicle"
        elif 'case' in column_lower:
            description = f"Information about the {column_lower.replace('case', '')} case"
        elif 'offense' in column_lower:
            description = f"Information about the {column_lower.replace('offense', '')} offense"
        elif 'evidence' in column_lower:
            description = f"Information about the {column_lower.replace('evidence', '')} evidence"
        elif 'witness' in column_lower:
            description = f"Information about the {column_lower.replace('witness', '')} witness"
        else:
            # Generic description based on data type
            if column_info["data_type"] in ['int', 'bigint', 'smallint']:
                description = f"Numeric identifier or count for {column_lower}"
            elif column_info["data_type"] in ['varchar', 'nvarchar', 'char', 'nchar']:
                description = f"Text field containing {column_lower}"
            elif column_info["data_type"] in ['datetime', 'date', 'time']:
                description = f"Date/time field for {column_lower}"
            elif column_info["data_type"] in ['decimal', 'numeric', 'float', 'real']:
                description = f"Numeric value for {column_lower}"
            elif column_info["data_type"] == 'bit':
                description = f"Boolean flag for {column_lower}"
            else:
                description = f"Field containing {column_lower}"
        
        # Add context from data analysis
        if content_analysis["sample_values"]:
            sample_str = ", ".join(str(v) for v in content_analysis["sample_values"][:3])
            description += f" (Sample values: {sample_str})"
        
        return description
    
    def analyze_table_relationships(self, table_name: str) -> Dict:
        """Analyze relationships for a specific table."""
        relationships = {
            "primary_keys": self.get_primary_keys(table_name),
            "foreign_keys": self.get_foreign_keys(table_name),
            "referenced_by": [],
            "suggested_joins": []
        }
        
        # Find tables that reference this table
        cursor = self.connection.cursor()
        query = """
        SELECT TABLE_NAME, COLUMN_NAME
        FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
        WHERE REFERENCED_TABLE_NAME = ? 
        AND TABLE_SCHEMA = 'DUI'
        """
        cursor.execute(query, table_name)
        for row in cursor.fetchall():
            relationships["referenced_by"].append({
                "table": row[0],
                "column": row[1]
            })
        cursor.close()
        
        return relationships
    
    def analyze_all_tables(self):
        """Comprehensive analysis of all tables in the database."""
        print("🔍 Starting comprehensive database analysis...")
        
        if not self.connect():
            return False
        
        try:
            # Get all tables
            tables = self.get_all_tables()
            print(f"📋 Found {len(tables)} tables: {', '.join(tables)}")
            
            # Analyze each table
            for table_name in tables:
                print(f"\n📊 Analyzing table: {table_name}")
                
                # Get table structure
                columns = self.get_table_columns(table_name)
                self.tables_info[table_name] = {
                    "columns": columns,
                    "relationships": self.analyze_table_relationships(table_name),
                    "sample_data": self.get_data_sample(table_name, 5)
                }
                
                # Analyze each column
                column_descriptions = {}
                for column in columns:
                    column_name = column["name"]
                    print(f"  🔍 Analyzing column: {column_name}")
                    
                    content_analysis = self.analyze_column_content(table_name, column_name)
                    description = self.generate_column_description(
                        table_name, column_name, column, content_analysis
                    )
                    
                    column_descriptions[column_name] = {
                        "description": description,
                        "content_analysis": content_analysis,
                        "column_info": column
                    }
                
                self.column_descriptions[table_name] = column_descriptions
            
            # Save analysis results
            self.save_analysis_results()
            
            print(f"\n✅ Analysis complete! Analyzed {len(tables)} tables")
            return True
            
        except Exception as e:
            print(f"❌ Analysis failed: {e}")
            return False
        finally:
            self.disconnect()
    
    def save_analysis_results(self):
        """Save analysis results to JSON files."""
        
        # Save table information
        tables_file = Path("db_backup/database_analysis.json")
        analysis_data = {
            "analysis_date": datetime.now().isoformat(),
            "tables": self.tables_info,
            "column_descriptions": self.column_descriptions,
            "summary": {
                "total_tables": len(self.tables_info),
                "total_columns": sum(len(info["columns"]) for info in self.tables_info.values()),
                "tables_with_relationships": len([t for t in self.tables_info.values() if t["relationships"]["foreign_keys"]])
            }
        }
        
        with open(tables_file, 'w', encoding='utf-8') as f:
            json.dump(analysis_data, f, indent=2)
        
        print(f"✅ Analysis results saved to: {tables_file}")
    
    def generate_relationship_summary(self) -> str:
        """Generate a summary of all table relationships."""
        summary = "Database Relationship Summary:\n\n"
        
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
    """Main function to run database analysis."""
    print("DUI Database Analyzer")
    print("=" * 50)
    
    analyzer = DatabaseAnalyzer()
    
    if analyzer.analyze_all_tables():
        print("\n" + "=" * 50)
        print("RELATIONSHIP SUMMARY")
        print("=" * 50)
        print(analyzer.generate_relationship_summary())
        
        print("\n🎯 Next steps:")
        print("1. Review database_analysis.json for detailed information")
        print("2. Use the analysis to create comprehensive views")
        print("3. Generate view descriptions based on column analysis")
    else:
        print("❌ Database analysis failed")

if __name__ == "__main__":
    main() 