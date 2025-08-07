#!/usr/bin/env python3
"""
Convert to Pure SQL Script
Converts comprehensive_dui_views.sql to pure SQL Server syntax
"""

def convert_sql_file():
    """Convert the SQL file to pure SQL Server syntax."""
    
    input_file = "db_backup/comprehensive_dui_views.sql"
    output_file = "create_all_dui_views_pure.sql"
    
    print(f"Converting {input_file} to {output_file}...")
    
    try:
        # Read the input file
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace CREATE OR REPLACE VIEW with CREATE VIEW
        content = content.replace('CREATE OR REPLACE VIEW', 'CREATE VIEW')
        
        # Remove GO statements
        content = content.replace('GO', '')
        
        # Remove DROP VIEW IF EXISTS statements (SQL Server doesn't support this)
        lines = content.split('\n')
        filtered_lines = []
        
        for line in lines:
            # Skip DROP VIEW IF EXISTS lines
            if line.strip().startswith('DROP VIEW IF EXISTS'):
                continue
            # Skip empty lines after removing GO
            if line.strip() == '':
                continue
            filtered_lines.append(line)
        
        # Add proper DROP VIEW statements at the beginning
        drop_statements = []
        for line in filtered_lines:
            if line.strip().startswith('CREATE VIEW DUI.'):
                view_name = line.strip().split('CREATE VIEW ')[1].split(' AS')[0]
                drop_statements.append(f"IF OBJECT_ID('{view_name}', 'V') IS NOT NULL DROP VIEW {view_name}")
        
        # Create the final content
        final_content = """-- =====================================================
-- DUI Views Creation Script - Pure SQL Server
-- Converted from comprehensive_dui_views.sql
-- Execute this directly in SQL Server Management Studio
-- =====================================================

"""
        
        # Add drop statements
        if drop_statements:
            final_content += "-- Drop existing views\n"
            for drop_stmt in drop_statements:
                final_content += drop_stmt + "\n"
            final_content += "\n"
        
        # Add the converted CREATE VIEW statements
        final_content += "-- Create all views\n"
        for line in filtered_lines:
            if line.strip().startswith('CREATE VIEW'):
                final_content += line + "\n"
        
        # Add completion message
        final_content += """
-- =====================================================
-- Script completed
-- =====================================================
PRINT 'All DUI views created successfully!'
PRINT 'Run: SELECT COUNT(*) FROM INFORMATION_SCHEMA.VIEWS WHERE TABLE_SCHEMA = ''DUI'' to verify count'
"""
        
        # Write the output file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(final_content)
        
        print(f"✅ Conversion completed! Output saved to: {output_file}")
        print(f"📄 You can now run this file directly in SQL Server Management Studio")
        
        # Count the views
        view_count = len([line for line in filtered_lines if line.strip().startswith('CREATE VIEW')])
        print(f"📊 Total views: {view_count}")
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    convert_sql_file() 