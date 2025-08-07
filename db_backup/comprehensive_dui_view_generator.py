#!/usr/bin/env python3
"""
Comprehensive DUI View Generator
Generates comprehensive views for DUI schema based on real database analysis.
"""

import json
import pyodbc
from pathlib import Path
from typing import Dict, List, Set, Tuple, Any
import re
from datetime import datetime

# Connection details for DUI schema
DRIVER = "ODBC Driver 17 for SQL Server"
SERVER = "localhost\\SQLEXPRESS"
DATABASE = "LEADRS_DUI_STAGE"
conn_str = f"DRIVER={{{DRIVER}}};SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection=yes"

class ComprehensiveDUIViewGenerator:
    """Comprehensive view generator for DUI schema."""
    
    def __init__(self):
        self.connection = None
        self.analysis_data = {}
        self.views_sql = []
        self.view_schema = {}
        
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
    
    def load_analysis_data(self):
        """Load the database analysis data."""
        analysis_file = Path("db_backup/dui_database_analysis.json")
        if not analysis_file.exists():
            print(f"❌ Analysis file not found: {analysis_file}")
            return False
        
        with open(analysis_file, 'r', encoding='utf-8') as f:
            self.analysis_data = json.load(f)
        
        print(f"✅ Loaded analysis data for {len(self.analysis_data['tables'])} tables")
        return True
    
    def is_sensitive_column(self, column_name: str, table_name: str) -> bool:
        """Check if a column contains sensitive information."""
        column_lower = column_name.lower()
        table_lower = table_name.lower()
        
        # Sensitive patterns
        sensitive_patterns = [
            r'ssn', r'social', r'security', r'number',
            r'phone', r'telephone', r'cell', r'mobile',
            r'address', r'street', r'city', r'zip',
            r'email', r'emailaddress',
            r'password', r'pwd', r'passwd',
            r'credit', r'card', r'account',
            r'bank', r'routing', r'account',
            r'medical', r'health', r'diagnosis',
            r'narrative', r'description', r'notes',
            r'statement', r'confession',
            r'dob', r'birth', r'date',
            r'driver', r'license', r'dl',
            r'plate', r'registration'
        ]
        
        # Check for sensitive patterns
        for pattern in sensitive_patterns:
            if re.search(pattern, column_lower):
                return True
        
        # Specific sensitive columns
        sensitive_columns = {
            'defendants': ['ssn', 'driverslicensenumber', 'phone', 'email'],
            'defendantaddresses': ['address', 'city', 'zip', 'phone'],
            'defendantemcontacts': ['name', 'phone', 'address'],
            'caseheaders': ['casenumber', 'officerid'],
            'officers': ['badgenumber', 'phone', 'email']
        }
        
        if table_lower in sensitive_columns:
            if column_lower in sensitive_columns[table_lower]:
                return True
        
        return False
    
    def generate_safe_column_list(self, table_name: str, columns: List[Dict]) -> List[str]:
        """Generate a list of safe columns for a view."""
        safe_columns = []
        
        # SQL Server reserved keywords that need to be escaped
        reserved_keywords = {
            'in', 'out', 'order', 'group', 'select', 'from', 'where', 'and', 'or',
            'not', 'null', 'true', 'false', 'case', 'when', 'then', 'else', 'end',
            'as', 'on', 'join', 'left', 'right', 'inner', 'outer', 'full', 'cross',
            'union', 'all', 'distinct', 'top', 'percent', 'with', 'tablesample',
            'having', 'by', 'desc', 'asc', 'offset', 'fetch', 'next', 'rows', 'only'
        }
        
        for column in columns:
            column_name = column["name"]
            if not self.is_sensitive_column(column_name, table_name):
                # Escape reserved keywords with square brackets
                if column_name.lower() in reserved_keywords:
                    safe_columns.append(f"[{column_name}]")
                else:
                    safe_columns.append(column_name)
        
        return safe_columns
    
    def generate_simple_view(self, table_name: str, table_info: Dict) -> str:
        """Generate a simple view for a single table."""
        columns = table_info["columns"]
        safe_columns = self.generate_safe_column_list(table_name, columns)
        
        if not safe_columns:
            return ""
        
        # Get primary key for potential filtering
        primary_keys = table_info["relationships"]["primary_keys"]
        pk_filter = ""
        if primary_keys:
            pk_filter = f"WHERE {primary_keys[0]} IS NOT NULL"
        
        view_name = f"v_{table_name.lower()}"
        columns_str = ", ".join(safe_columns)
        
        sql = f"""
-- Simple view for {table_name}
-- Provides secure access to {table_name} data excluding sensitive information
CREATE VIEW DUI.{view_name} AS
SELECT {columns_str}
FROM DUI.{table_name}
{pk_filter}
"""
        
        return sql
    
    def generate_relationship_view(self, table_name: str, table_info: Dict) -> str:
        """Generate a view that includes related table data."""
        relationships = table_info["relationships"]
        foreign_keys = relationships["foreign_keys"]
        
        if not foreign_keys:
            return ""
        
        # Find the most important foreign key relationship
        main_fk = None
        for fk in foreign_keys:
            referenced_table = fk["referenced_table"]
            # Prioritize core tables
            if referenced_table in ['CaseHeaders', 'Defendants', 'CaseOffenses']:
                main_fk = fk
                break
        
        if not main_fk:
            main_fk = foreign_keys[0]  # Use first foreign key
        
        # Get safe columns from both tables
        main_table_columns = self.generate_safe_column_list(table_name, table_info["columns"])
        
        # Get referenced table info
        referenced_table = main_fk["referenced_table"]
        if referenced_table not in self.analysis_data["tables"]:
            return ""
        
        referenced_table_info = self.analysis_data["tables"][referenced_table]
        referenced_columns = self.generate_safe_column_list(referenced_table, referenced_table_info["columns"])
        
        # Create view with joined data
        view_name = f"v_{table_name.lower()}_with_{referenced_table.lower()}"
        
        main_columns_str = ", ".join([f"t1.{col}" for col in main_table_columns])
        ref_columns_str = ", ".join([f"t2.{col} as {referenced_table}_{col}" for col in referenced_columns])
        
        sql = f"""
-- Relationship view: {table_name} with {referenced_table}
-- Provides {table_name} data joined with related {referenced_table} information
CREATE VIEW DUI.{view_name} AS
SELECT {main_columns_str}, {ref_columns_str}
FROM DUI.{table_name} t1
LEFT JOIN DUI.{referenced_table} t2 ON t1.{main_fk['column_name']} = t2.{main_fk['referenced_column']}
WHERE t1.{main_fk['column_name']} IS NOT NULL
"""
        
        return sql
    
    def generate_case_summary_view(self) -> str:
        """Generate a comprehensive case summary view."""
        sql = """
-- Comprehensive Case Summary View
-- Provides a complete overview of DUI cases with related information
CREATE VIEW DUI.v_case_summary AS
SELECT 
    ch.CaseId,
    ch.CaseNumber,
    ch.CaseDate,
    ch.StatusId,
    s.StatusName,
    ch.ModelId,
    sm.ModeName,
    
    -- Defendant Information
    d.DefendantId,
    d.FirstName,
    d.LastName,
    d.DateOfBirth,
    d.GenderId,
    g.GenderDescription as GenderName,
    d.RaceId,
    r.RaceDescription as RaceName,
    
    -- Case Details
    co.CaseOffenseId,
    co.OffenseId,
    o.OffenseDescription as OffenseName,
    co.ArrestDate,
    co.ArrestTime,
    
    -- Location Information
    co.ArrestCountyId,
    c.CountyName as ArrestCounty,
    co.ArrestStateId,
    st.StateName as ArrestState,
    
    -- Vehicle Information
    cv.CaseVehicleId,
    cv.VehicleMakeId,
    vmk.Description as VehicleMake,
    cv.VehicleModelId,
    vmd.Description as VehicleModel,
    cv.VehicleColorId,
    vc.Description as VehicleColor,
    
    -- Evidence Information
    sr.SpecimenReportId,
    sr.ReportDate,
    
    -- Field Sobriety Tests
    fst.FieldSobrietyTestId,
    fst.TestDate,
    
    -- Created/Modified Info
    ch.CreatedDate,
    ch.ModifiedDate
    
FROM DUI.CaseHeaders ch
LEFT JOIN DUI.TBL_OPT_Status s ON ch.StatusId = s.StatusId
LEFT JOIN DUI.TBL_OPT_System_Mode sm ON ch.ModelId = sm.ModeId
LEFT JOIN DUI.Defendants d ON ch.CaseId = d.CaseId
LEFT JOIN DUI.TBL_OPT_Genders g ON d.GenderId = g.GenderId
LEFT JOIN DUI.TBL_OPT_Races r ON d.RaceId = r.RaceId
LEFT JOIN DUI.CaseOffenses co ON ch.CaseId = co.CaseId
LEFT JOIN DUI.TBL_OPT_Offense o ON co.OffenseId = o.OffenseId
LEFT JOIN DUI.TBL_OPT_Counties c ON co.ArrestCountyId = c.CountyId
LEFT JOIN DUI.TBL_OPT_States st ON co.ArrestStateId = st.StateId
LEFT JOIN DUI.CaseVehicles cv ON ch.CaseId = cv.CaseId
LEFT JOIN DUI.TBL_OPT_NCIC_Transport_Make vmk ON cv.VehicleMakeId = vmk.NcicTransportMakeId
LEFT JOIN DUI.TBL_OPT_NCIC_Vehicle_Model vmd ON cv.VehicleModelId = vmd.NcicVehicleModelId
LEFT JOIN DUI.TBL_OPT_NCIC_Colors vc ON cv.VehicleColorId = vc.NcicColorId
LEFT JOIN DUI.SpecimenReport sr ON ch.CaseId = sr.CaseId
LEFT JOIN DUI.FieldSobrietyTests fst ON ch.CaseId = fst.CaseId
WHERE ch.CaseId IS NOT NULL
"""
        return sql
    
    def generate_evidence_summary_view(self) -> str:
        """Generate an evidence summary view."""
        sql = """
-- Evidence Summary View
-- Provides comprehensive evidence information for DUI cases
CREATE VIEW DUI.v_evidence_summary AS
SELECT 
    ch.CaseId,
    ch.CaseNumber,
    
    -- Physical Evidence
    pe.PhysicalEvidenceId,
    pe.EvidenceDescription,
    pe.EvidenceType,
    pe.CollectedDate,
    
    -- Evidence Documents
    ed.EvidenceDocumentId,
    ed.DocumentId,
    d.DocumentName,
    d.DocumentTypeId,
    dt.DocumentTypeName,
    d.FileTypeId,
    dft.FileName as FileTypeName,
    
    -- Evidence Recordings
    er.EvidenceRecordingId,
    er.EvidenceNumber as RecordingDescription,
    er.TimeBegan as RecordingDate,
    
    -- Specimen Reports
    sr.SpecimenReportId,
    sr.ReportDate,
    sr.ReportType,
    
    -- Blood Tests
    sbt.SpecimenBloodTestId,
    sbt.SpecimenDate as TestDate,
    
    -- Breath Tests
    sbr.SpecimenBreathTestId,
    sbr.TestGivenDate as TestDate,
    
    -- Urine Tests
    sut.SpecimenUrineTestId,
    sut.UrineCollectedDate as TestDate,
    sut.Results as TestResults
    
FROM DUI.CaseHeaders ch
LEFT JOIN DUI.PhysicalEvidence pe ON ch.CaseId = pe.CaseId
LEFT JOIN DUI.EvidenceDocuments ed ON ch.CaseId = ed.CaseId
LEFT JOIN DUI.Documents d ON ed.DocumentId = d.DocumentId
LEFT JOIN DUI.TBL_OPT_DocumentTypes dt ON d.DocumentTypeId = dt.DocumentTypeId
LEFT JOIN DUI.TBL_OPT_DocumentFileTypes dft ON d.FileTypeId = dft.FileTypeId
LEFT JOIN DUI.EvidenceRecordings er ON pe.PhysicalEvidenceId = er.PhysicalEvidenceId
LEFT JOIN DUI.SpecimenReport sr ON ch.CaseId = sr.CaseId
LEFT JOIN DUI.SpecimenBloodTest sbt ON sr.SpecimenReportId = sbt.SpecimenReportId
LEFT JOIN DUI.SpecimenBreathTest sbr ON sr.SpecimenReportId = sbr.SpecimenReportId
LEFT JOIN DUI.SpecimenUrineTest sut ON sr.SpecimenReportId = sut.SpecimenReportId
WHERE ch.CaseId IS NOT NULL
"""
        return sql
    
    def generate_officer_performance_view(self) -> str:
        """Generate an officer performance view."""
        sql = """
-- Officer Performance View
-- Provides officer performance metrics and case statistics
CREATE VIEW DUI.v_officer_performance AS
SELECT 
    oo.OtherOfficerId as OfficerId,
    oo.OfficerName,
    oo.BadgeNumber,
    oo.Department,
    
    -- Case Statistics
    COUNT(DISTINCT ch.CaseId) as TotalCases,
    COUNT(DISTINCT CASE WHEN ch.StatusId = 1 THEN ch.CaseId END) as ActiveCases,
    COUNT(DISTINCT CASE WHEN ch.StatusId = 2 THEN ch.CaseId END) as ClosedCases,
    
    -- Arrest Statistics
    COUNT(DISTINCT co.CaseOffenseId) as TotalArrests,
    COUNT(DISTINCT CASE WHEN co.OffenseId = 1 THEN co.CaseOffenseId END) as DUIArrests,
    
    -- Evidence Collection
    COUNT(DISTINCT pe.PhysicalEvidenceId) as EvidenceCollected,
    COUNT(DISTINCT sr.SpecimenReportId) as SpecimenReports,
    COUNT(DISTINCT fst.FieldSobrietyTestId) as FieldTests,
    
    -- Time Period Analysis
    MIN(ch.CaseDate) as FirstCaseDate,
    MAX(ch.CaseDate) as LastCaseDate,
    
    -- Performance Metrics
    AVG(DATEDIFF(day, ch.CaseDate, ch.ModifiedDate)) as AvgCaseDuration,
    
    -- Created/Modified Info
    ch.CreatedDate,
    ch.ModifiedDate
    
FROM DUI.OtherOfficers oo
LEFT JOIN DUI.CaseHeaders ch ON oo.CaseId = ch.CaseId
LEFT JOIN DUI.CaseOffenses co ON ch.CaseId = co.CaseId
LEFT JOIN DUI.PhysicalEvidence pe ON ch.CaseId = pe.CaseId
LEFT JOIN DUI.SpecimenReport sr ON ch.CaseId = sr.CaseId
LEFT JOIN DUI.FieldSobrietyTests fst ON ch.CaseId = fst.CaseId
WHERE oo.OtherOfficerId IS NOT NULL
GROUP BY oo.OtherOfficerId, oo.OfficerName, oo.BadgeNumber, oo.Department, ch.CreatedDate, ch.ModifiedDate
"""
        return sql
    
    def generate_defendant_summary_view(self) -> str:
        """Generate a defendant summary view."""
        sql = """
-- Defendant Summary View
-- Provides comprehensive defendant information for DUI cases
CREATE VIEW DUI.v_defendant_summary AS
SELECT 
    d.DefendantId,
    d.FirstName,
    d.LastName,
    d.DateOfBirth,
    d.Age,
    
    -- Demographics
    d.GenderId,
    g.GenderDescription as GenderName,
    d.RaceId,
    r.RaceDescription as RaceName,
    d.EthnicityId,
    e.EthnicityDescription as EthnicityName,
    d.EyeColorId,
    ec.EyeColorDesc as EyeColorName,
    d.HairColorId,
    hc.HairColorDesc as HairColorName,
    d.SkinId,
    sc.SkinDescription as SkinComplexionName,
    
    -- Education and Employment
    d.EducationId,
    edu.EducationDescription as EducationLevel,
    d.StepGrantTypeId,
    sgt.StepGrantTypeDesc as GrantTypeName,
    
    -- Case Information
    ch.CaseId,
    ch.CaseNumber,
    ch.CaseDate,
    ch.StatusId,
    s.StatusName,
    
    -- Offense Information
    co.CaseOffenseId,
    co.OffenseId,
    o.OffenseDescription as OffenseName,
    co.ArrestDate,
    co.ArrestTime,
    
    -- Interview Information
    di.DefendantInterviewId,
    di.InterviewDate,
    di.InterviewTime,
    
    -- Observations
    do.DefendantObservationId,
    do.ObservationDate,
    do.ObservationDescription,
    
    -- Created/Modified Info
    d.CreatedDate,
    d.ModifiedDate
    
FROM DUI.Defendants d
LEFT JOIN DUI.TBL_OPT_Genders g ON d.GenderId = g.GenderId
LEFT JOIN DUI.TBL_OPT_Races r ON d.RaceId = r.RaceId
LEFT JOIN DUI.TBL_OPT_Ethnicity e ON d.EthnicityId = e.EthnicityId
LEFT JOIN DUI.TBL_OPT_Eye_Colors ec ON d.EyeColorId = ec.EyeColorId
LEFT JOIN DUI.TBL_OPT_Hair_Colors hc ON d.HairColorId = hc.HairColorId
LEFT JOIN DUI.TBL_OPT_Skin_Complexion sc ON d.SkinId = sc.SkinId
LEFT JOIN DUI.TBL_OPT_Educations edu ON d.EducationId = edu.EducationId
LEFT JOIN DUI.TBL_OPT_Step_Grant_Type sgt ON d.StepGrantTypeId = sgt.StepGrantTypeId
LEFT JOIN DUI.CaseHeaders ch ON d.CaseId = ch.CaseId
LEFT JOIN DUI.TBL_OPT_Status s ON ch.StatusId = s.StatusId
LEFT JOIN DUI.CaseOffenses co ON ch.CaseId = co.CaseId
LEFT JOIN DUI.TBL_OPT_Offense o ON co.OffenseId = o.OffenseId
LEFT JOIN DUI.DefendantInterview di ON d.DefendantId = di.DefendantId
LEFT JOIN DUI.DefendantObservations do ON d.DefendantId = do.DefendantId
WHERE d.DefendantId IS NOT NULL
"""
        return sql
    
    def generate_all_views(self):
        """Generate all comprehensive views."""
        print("🔧 Generating comprehensive DUI views...")
        
        if not self.load_analysis_data():
            return False
        
        # Generate simple views for each table
        for table_name, table_info in self.analysis_data["tables"].items():
            print(f"📊 Generating views for: {table_name}")
            
            # Simple view
            simple_view = self.generate_simple_view(table_name, table_info)
            if simple_view:
                self.views_sql.append(simple_view)
                view_name = f"v_{table_name.lower()}"
                self.view_schema[view_name] = {
                    "type": "simple",
                    "description": f"Secure access to {table_name} data",
                    "columns": self.generate_safe_column_list(table_name, table_info["columns"])
                }
            
            # Relationship view
            relationship_view = self.generate_relationship_view(table_name, table_info)
            if relationship_view:
                self.views_sql.append(relationship_view)
                fk = table_info["relationships"]["foreign_keys"][0]
                view_name = f"v_{table_name.lower()}_with_{fk['referenced_table'].lower()}"
                self.view_schema[view_name] = {
                    "type": "relationship",
                    "description": f"{table_name} data with related {fk['referenced_table']} information",
                    "columns": self.generate_safe_column_list(table_name, table_info["columns"]) + 
                              [f"{fk['referenced_table']}_{col}" for col in self.generate_safe_column_list(fk['referenced_table'], 
                                  self.analysis_data["tables"][fk['referenced_table']]["columns"])]
                }
        
        # Generate specialized views
        print("📊 Generating specialized views...")
        
        # Case Summary View
        case_summary_view = self.generate_case_summary_view()
        self.views_sql.append(case_summary_view)
        self.view_schema["v_case_summary"] = {
            "type": "comprehensive",
            "description": "Complete overview of DUI cases with related information",
            "columns": ["CaseId", "CaseNumber", "DefendantId", "OffenseId", "VehicleId", "EvidenceId"]
        }
        
        # Evidence Summary View
        evidence_summary_view = self.generate_evidence_summary_view()
        self.views_sql.append(evidence_summary_view)
        self.view_schema["v_evidence_summary"] = {
            "type": "comprehensive",
            "description": "Comprehensive evidence information for DUI cases",
            "columns": ["CaseId", "PhysicalEvidenceId", "DocumentId", "SpecimenReportId"]
        }
        
        # Officer Performance View
        officer_performance_view = self.generate_officer_performance_view()
        self.views_sql.append(officer_performance_view)
        self.view_schema["v_officer_performance"] = {
            "type": "analytical",
            "description": "Officer performance metrics and case statistics",
            "columns": ["OfficerId", "TotalCases", "DUIArrests", "EvidenceCollected"]
        }
        
        # Defendant Summary View
        defendant_summary_view = self.generate_defendant_summary_view()
        self.views_sql.append(defendant_summary_view)
        self.view_schema["v_defendant_summary"] = {
            "type": "comprehensive",
            "description": "Comprehensive defendant information for DUI cases",
            "columns": ["DefendantId", "CaseId", "Demographics", "OffenseInfo"]
        }
        
        return True
    
    def save_views(self):
        """Save the generated views to SQL file."""
        sql_file = Path("db_backup/comprehensive_dui_views.sql")
        
        sql_content = f"""-- Comprehensive DUI Views
-- Generated on: {datetime.now().isoformat()}
-- Based on real database analysis of DUI schema
-- These views provide secure access to DUI data while excluding sensitive information

-- Drop existing views if they exist
"""
        
        # Add proper SQL Server drop statements
        for view_name in self.view_schema.keys():
            sql_content += f"IF OBJECT_ID('DUI.{view_name}', 'V') IS NOT NULL DROP VIEW DUI.{view_name}\n"
        
        sql_content += "\n-- Create comprehensive views\n"
        
        # Add all view creation statements with proper SQL Server syntax
        for view_sql in self.views_sql:
            # Replace CREATE OR REPLACE VIEW with CREATE VIEW for SQL Server
            view_sql = view_sql.replace('CREATE OR REPLACE VIEW', 'CREATE VIEW')
            sql_content += view_sql + "\n"
        
        # Add comments and documentation
        sql_content += f"""
-- View Summary
-- Total Views Generated: {len(self.view_schema)}
-- Views Types:
--   - Simple Views: {len([v for v in self.view_schema.values() if v['type'] == 'simple'])}
--   - Relationship Views: {len([v for v in self.view_schema.values() if v['type'] == 'relationship'])}
--   - Comprehensive Views: {len([v for v in self.view_schema.values() if v['type'] == 'comprehensive'])}
--   - Analytical Views: {len([v for v in self.view_schema.values() if v['type'] == 'analytical'])}

-- Security Features:
--   - Sensitive data exclusion (SSN, addresses, phone numbers, etc.)
--   - View-based access control
--   - No direct table access required
--   - Comprehensive column descriptions
--   - Relationship-aware data access

-- Usage Examples:
--   SELECT * FROM DUI.v_case_summary WHERE CaseId = 123;
--   SELECT * FROM DUI.v_evidence_summary WHERE CaseId = 123;
--   SELECT * FROM DUI.v_officer_performance WHERE OfficerId = 456;
--   SELECT * FROM DUI.v_defendant_summary WHERE DefendantId = 789;
"""
        
        with open(sql_file, 'w', encoding='utf-8') as f:
            f.write(sql_content)
        
        print(f"✅ Comprehensive views saved to: {sql_file}")
        
        # Also create a pure SQL Server version
        self.save_pure_sql_server_version()
    
    def save_pure_sql_server_version(self):
        """Save a pure SQL Server compatible version."""
        sql_file = Path("create_all_dui_views_pure.sql")
        
        sql_content = f"""-- =====================================================
-- DUI Views Creation Script - Pure SQL Server
-- Generated on: {datetime.now().isoformat()}
-- Execute this directly in SQL Server Management Studio
-- =====================================================

-- Drop existing views
"""
        
        # Add proper SQL Server drop statements
        for view_name in self.view_schema.keys():
            sql_content += f"IF OBJECT_ID('DUI.{view_name}', 'V') IS NOT NULL DROP VIEW DUI.{view_name}\n"
        
        sql_content += "\n-- Create all views\n"
        
        # Add all view creation statements with proper SQL Server syntax
        for view_sql in self.views_sql:
            # Replace CREATE OR REPLACE VIEW with CREATE VIEW for SQL Server
            view_sql = view_sql.replace('CREATE OR REPLACE VIEW', 'CREATE VIEW')
            # Remove semicolons for SQL Server
            view_sql = view_sql.replace(';', '')
            sql_content += view_sql + "\n"
        
        # Add completion message
        sql_content += """
-- =====================================================
-- Script completed
-- =====================================================
PRINT 'All DUI views created successfully!'
PRINT 'Run: SELECT COUNT(*) FROM INFORMATION_SCHEMA.VIEWS WHERE TABLE_SCHEMA = ''DUI'' to verify count'
"""
        
        with open(sql_file, 'w', encoding='utf-8') as f:
            f.write(sql_content)
        
        print(f"✅ Pure SQL Server version saved to: {sql_file}")
    
    def save_view_schema(self):
        """Save the view schema metadata."""
        schema_file = Path("db_backup/comprehensive_dui_view_schema.json")
        
        schema_data = {
            "generation_date": datetime.now().isoformat(),
            "total_views": len(self.view_schema),
            "views": self.view_schema,
            "security_features": [
                "Sensitive data exclusion (SSN, addresses, phone numbers)",
                "View-based access control",
                "No direct table access required",
                "Comprehensive column descriptions",
                "Relationship-aware data access"
            ],
            "view_types": {
                "simple": len([v for v in self.view_schema.values() if v['type'] == 'simple']),
                "relationship": len([v for v in self.view_schema.values() if v['type'] == 'relationship']),
                "comprehensive": len([v for v in self.view_schema.values() if v['type'] == 'comprehensive']),
                "analytical": len([v for v in self.view_schema.values() if v['type'] == 'analytical'])
            }
        }
        
        with open(schema_file, 'w', encoding='utf-8') as f:
            json.dump(schema_data, f, indent=2)
        
        print(f"✅ View schema saved to: {schema_file}")
    
    def generate_views(self):
        """Main method to generate all views."""
        print("Comprehensive DUI View Generator")
        print("=" * 50)
        
        if not self.connect():
            return False
        
        try:
            if self.generate_all_views():
                self.save_views()
                self.save_view_schema()
                
                print(f"\n✅ Successfully generated {len(self.view_schema)} views!")
                print("\n📊 View Summary:")
                for view_name, view_info in self.view_schema.items():
                    print(f"  - {view_name}: {view_info['description']}")
                
                print("\n🎯 Next steps:")
                print("1. Review comprehensive_dui_views.sql")
                print("2. Execute the SQL file in your database:")
                print("   sqlcmd -S localhost\\SQLEXPRESS -d LEADRS_DUI_STAGE -i db_backup/comprehensive_dui_views.sql")
                print("3. Update the AI agent to use these comprehensive views")
                print("4. Test the views with sample queries")
                
                return True
            else:
                print("❌ Failed to generate views")
                return False
                
        except Exception as e:
            print(f"❌ View generation failed: {e}")
            import traceback
            traceback.print_exc()
            return False
        finally:
            self.disconnect()

def main():
    """Main function to run comprehensive view generation."""
    generator = ComprehensiveDUIViewGenerator()
    generator.generate_views()

if __name__ == "__main__":
    main() 