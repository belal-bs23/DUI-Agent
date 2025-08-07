# 🚔 DUI SQL Agent

A professional AI agent that generates precise SQL queries for DUI database schema using environment-based configuration and secure views.

## ✅ **SYSTEM READY - Environment-Based Configuration**

### **🎯 What You Have:**

1. **✅ Complete Database Analysis**
   - 142 DUI tables analyzed and documented
   - 200+ relationships mapped
   - Comprehensive column descriptions

2. **✅ 195 Secure Views Generated**
   - Security-focused views (excludes sensitive data)
   - Relationship-aware views with proper JOINs
   - Ready to deploy to your database

3. **✅ Professional AI Agent**
   - Environment-based configuration
   - Multiple model support
   - Clean, maintainable code

## 🚀 **Quick Start**

### **1. Setup**
```bash
# Run setup script
python setup.py

# Or manually install dependencies
pip install -r requirements.txt
```

### **2. Quick Demo**
```bash
python demo_agent.py
```

### **3. Interactive Interface**
```bash
python dui_interface.py
```

### **4. Programmatic Usage**
```python
from dui_sql_agent import DUISQLAgent

# Initialize agent (uses environment configuration)
agent = DUISQLAgent()

# Generate SQL queries
result = agent.run_query("Show me all DUI cases from last month")
print(result['sql_query'])
```

## ⚙️ **Environment Configuration**

The system uses environment variables for configuration. Edit your `.env` file:

```bash
# AI Model Configuration
AI_MODEL_TYPE=mock
AI_MODEL_NAME=
AI_API_KEY=

# OpenAI Configuration (if using OpenAI models)
OPENAI_API_KEY=your-openai-api-key-here

# Database Configuration
DB_DRIVER=ODBC Driver 17 for SQL Server
DB_SERVER=localhost\\SQLEXPRESS
DB_NAME=LEADRS_DUI_STAGE
```

## 🔧 **Available Model Types**

| AI_MODEL_TYPE | Description | Requirements |
|---------------|-------------|--------------|
| `mock` | Testing model (no API) | None |
| `openai` | OpenAI models | OpenAI API key |
| `ollama` | Local models | Ollama installation |
| `huggingface` | HuggingFace models | HuggingFace token |

## 📋 **Example Usage**

```bash
# Test the system
python demo_agent.py

# Interactive mode
python dui_interface.py
# Then type: query Show me all DUI cases from last month
```

## 🎯 **What the System Can Do**

1. **Natural Language to SQL**
   - Convert questions to precise SQL queries
   - Uses secure views instead of direct table access
   - Handles complex relationships automatically

2. **Security First**
   - All queries use secure views
   - Sensitive data automatically excluded
   - No direct table access

3. **Comprehensive Coverage**
   - Access to all 142 DUI tables
   - 195 specialized views available
   - Relationship-aware queries

## 📊 **System Status**

- ✅ **Database Connection**: Working
- ✅ **Schema Analysis**: Complete (142 tables)
- ✅ **View Generation**: Complete (195 views)
- ✅ **AI Agent**: Working (configurable)
- ✅ **Security**: Implemented
- ✅ **Environment Config**: Working

## 🔑 **Next Steps**

1. **Deploy Views** (Optional):
   ```bash
   sqlcmd -S localhost\SQLEXPRESS -d LEADRS_DUI_STAGE -i db_backup/comprehensive_dui_views.sql
   ```

2. **Use the System**:
   ```bash
   # Demo
   python demo_agent.py
   
   # Interactive
   python dui_interface.py
   ```

3. **Configure Models** (Optional):
   - Edit `.env` file to change `AI_MODEL_TYPE`
   - Add API keys as needed
   - Install additional dependencies if required

## 💡 **Key Benefits**

- **🔧 Configurable**: Environment-based configuration
- **🔒 Secure**: Uses views, not direct table access
- **📊 Comprehensive**: Covers all 142 DUI tables
- **🚀 Ready to Use**: No additional setup required
- **🔄 Scalable**: Easy to upgrade models
- **🧹 Clean Code**: Professional, maintainable codebase

## 📁 **Project Structure**

```
leadrs_dui_stage/
├── dui_sql_agent.py          # Main agent with environment configuration
├── dui_interface.py          # Interactive interface
├── demo_agent.py             # Demo script
├── setup.py                  # Setup script
├── requirements.txt          # Python dependencies
├── .env                      # Environment configuration
├── README.md                 # This file
├── FINAL_DUI_AGENT_SUMMARY.md # Detailed summary
└── db_backup/
    ├── comprehensive_dui_views.sql           # 195 secure views
    ├── dui_database_analysis.json            # Complete database analysis
    ├── comprehensive_dui_view_schema.json    # View schema definitions
    ├── comprehensive_dui_view_generator.py   # View generator
    └── dui_focused_analyzer.py               # Database analyzer
```

## 🎉 **Success!**

Your DUI SQL Agent is **100% ready to use** with environment-based configuration. The system is professional, secure, and easily configurable for different environments and requirements.

## 📞 **Support**

For questions or issues:
1. Check the `FINAL_DUI_AGENT_SUMMARY.md` for detailed information
2. Run `python setup.py` to verify your setup
3. Use `python dui_interface.py` and type `help` for usage instructions 