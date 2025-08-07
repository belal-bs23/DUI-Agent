# DUI SQL Agent

AI agent that generates SQL queries for DUI database schema using LangGraph workflow.

## Quick Start

```bash
# Setup
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt

# Run demo
python dui_sql_agent_langgraph.py

# Interactive mode
python dui_interface_langgraph.py
```

## Configuration

```bash
# Setup configuration
python setup_config.py
```

Or edit `.env` manually:
```bash
AI_MODEL_TYPE=mock          # mock, openai, gemini, ollama, huggingface
AI_MODEL_NAME=gpt-4
OPENAI_API_KEY=your-key-here
```

## Usage

### Programmatic
```python
from dui_sql_agent_langgraph import DUISQLAgentLangGraph

agent = DUISQLAgentLangGraph()
result = agent.run_query("Show me all DUI cases from last month")
print(result['sql_query'])
```

### Interactive
```bash
python dui_interface_langgraph.py
# Type: query Show me all DUI cases from last month
```

## Features

- **LangGraph Workflow**: 5-step organized process
- **Rate Limit Handling**: Automatic fallback to mock model
- **Secure Views**: Uses 195 secure database views
- **Multiple Models**: Support for OpenAI, Gemini, Ollama, HuggingFace
- **Mock Mode**: No API required for testing

## Model Types

| Type | Description | Requirements |
|------|-------------|--------------|
| `mock` | Testing model | None |
| `openai` | OpenAI models | API key |
| `gemini` | Google Gemini | API key |
| `ollama` | Local models | Ollama install |
| `huggingface` | HuggingFace | API token |

## Project Structure

```
├── dui_sql_agent_langgraph.py      # Main agent
├── dui_interface_langgraph.py      # Interactive interface
├── setup_config.py                 # Config setup
├── requirements.txt                # Dependencies
├── .env                            # Configuration
└── db_backup/
    ├── comprehensive_dui_views.sql           # 195 views
    ├── dui_database_analysis.json            # DB analysis
    └── comprehensive_dui_view_schema.json    # View schema
```

## Database Views

Deploy views to your database (optional):
```bash
sqlcmd -S localhost\SQLEXPRESS -d LEADRS_DUI_STAGE -i db_backup/comprehensive_dui_views.sql
```

## Support

- Run `python setup_config.py` for configuration help
- Use `python dui_interface_langgraph.py` and type `help`
- Check logs for workflow details 