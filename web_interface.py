#!/usr/bin/env python3
"""
DUI Multi-Agent Web Interface
=============================

FastAPI web interface for the DUI Multi-Agent SQL System.
Provides a simple chat interface for natural language to SQL conversion.
"""

import json
import os
import sys
from typing import Dict, Any, List, Optional
from datetime import datetime
from pathlib import Path

# Add current directory to path for imports
sys.path.append(str(Path(__file__).parent))

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import uvicorn

# Import the multi-agent system
from dui_multi_agent_system import get_multi_agent_system

# Initialize FastAPI app
app = FastAPI(
    title="DUI Multi-Agent SQL System",
    description="Web interface for natural language to SQL conversion",
    version="1.0.0"
)

# Initialize multi-agent system
try:
    multi_agent_system = get_multi_agent_system()
    system_ready = True
except Exception as e:
    print(f"❌ Failed to initialize multi-agent system: {e}")
    system_ready = False
    multi_agent_system = None

# Create templates directory
templates_dir = Path("templates")
templates_dir.mkdir(exist_ok=True)

# Create static directory
static_dir = Path("static")
static_dir.mkdir(exist_ok=True)

# Setup templates
templates = Jinja2Templates(directory="templates")

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Pydantic models
class QueryRequest(BaseModel):
    query: str
    execute: bool = False

class QueryResponse(BaseModel):
    success: bool
    query: str
    sql: str
    explanation: str
    validation: Dict[str, Any]
    context_usage: Dict[str, Any]
    execution_result: Optional[Dict[str, Any]] = None
    timestamp: str

class SystemStatus(BaseModel):
    status: str
    agents_loaded: int
    total_views: int
    cache_hit_ratio: str
    context_reduction: str

# API Routes
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Serve the main chat interface."""
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/api/status", response_model=SystemStatus)
async def get_status():
    """Get system status."""
    if not system_ready:
        raise HTTPException(status_code=503, detail="System not ready")
    
    try:
        status = multi_agent_system.get_system_status()
        return SystemStatus(
            status=status["system_status"],
            agents_loaded=status["agents_loaded"],
            total_views=status["data_manager"]["total_views"],
            cache_hit_ratio=status["data_manager"]["cache_hit_ratio"],
            context_reduction=status["context_optimization"]["reduction_percentage"]
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to get status: {str(e)}")

@app.post("/api/query", response_model=QueryResponse)
async def process_query(request: QueryRequest):
    """Process a natural language query."""
    if not system_ready:
        raise HTTPException(status_code=503, detail="System not ready")
    
    try:
        # Process the query
        result = multi_agent_system.process_query(request.query)
        
        # Extract SQL from JSON if needed
        final_sql = result.get('final_sql', '')
        if final_sql:
            try:
                # Handle markdown code blocks
                if final_sql.strip().startswith('```'):
                    import re
                    # Remove markdown code blocks
                    final_sql = re.sub(r'^```\w*\s*', '', final_sql)
                    final_sql = re.sub(r'\s*```$', '', final_sql)
                
                # Handle JSON wrapper
                if final_sql.strip().startswith('{') and final_sql.strip().endswith('}'):
                    sql_data = json.loads(final_sql)
                    if isinstance(sql_data, dict) and 'sql_query' in sql_data:
                        final_sql = sql_data['sql_query']
            except (json.JSONDecodeError, KeyError):
                pass
        
        # Execute query if requested
        execution_result = None
        if request.execute and result.get('success', False) and result.get('is_valid', False):
            try:
                execution_result = multi_agent_system.execute_query(request.query)
            except Exception as e:
                execution_result = {
                    "executed": False,
                    "reason": f"Execution failed: {str(e)}"
                }
        
        return QueryResponse(
            success=result.get('success', False),
            query=request.query,
            sql=final_sql.strip(),
            explanation=result.get('sql_generation', {}).get('explanation', ''),
            validation=result.get('validation', {}),
            context_usage=result.get('context_usage', {}),
            execution_result=execution_result,
            timestamp=datetime.now().isoformat()
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Query processing failed: {str(e)}")

@app.get("/api/health")
async def health_check():
    """Health check endpoint."""
    return {
        "status": "healthy" if system_ready else "unhealthy",
        "system_ready": system_ready,
        "timestamp": datetime.now().isoformat()
    }

# Create HTML template
def create_html_template():
    """Create the HTML template for the chat interface."""
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DUI Multi-Agent SQL System</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 15px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
            overflow: hidden;
        }
        
        .header {
            background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%);
            color: white;
            padding: 30px;
            text-align: center;
        }
        
        .header h1 {
            font-size: 2.5em;
            margin-bottom: 10px;
        }
        
        .header p {
            font-size: 1.1em;
            opacity: 0.9;
        }
        
        .status-bar {
            background: #f8f9fa;
            padding: 15px 30px;
            border-bottom: 1px solid #e9ecef;
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 10px;
        }
        
        .status-item {
            display: flex;
            align-items: center;
            gap: 5px;
            font-size: 0.9em;
            color: #6c757d;
        }
        
        .status-indicator {
            width: 10px;
            height: 10px;
            border-radius: 50%;
            background: #28a745;
        }
        
        .status-indicator.error {
            background: #dc3545;
        }
        
        .main-content {
            display: flex;
            min-height: 600px;
        }
        
        .chat-section {
            flex: 1;
            padding: 30px;
            border-right: 1px solid #e9ecef;
        }
        
        .results-section {
            flex: 1;
            padding: 30px;
            background: #f8f9fa;
        }
        
        .input-group {
            margin-bottom: 20px;
        }
        
        .input-group label {
            display: block;
            margin-bottom: 8px;
            font-weight: 600;
            color: #495057;
        }
        
        .query-input {
            width: 100%;
            padding: 15px;
            border: 2px solid #e9ecef;
            border-radius: 10px;
            font-size: 16px;
            resize: vertical;
            min-height: 100px;
            font-family: inherit;
        }
        
        .query-input:focus {
            outline: none;
            border-color: #667eea;
            box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
        }
        
        .button-group {
            display: flex;
            gap: 10px;
            margin-bottom: 20px;
        }
        
        .btn {
            padding: 12px 24px;
            border: none;
            border-radius: 8px;
            font-size: 16px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            flex: 1;
        }
        
        .btn-primary {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
        }
        
        .btn-primary:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
        }
        
        .btn-secondary {
            background: #6c757d;
            color: white;
        }
        
        .btn-secondary:hover {
            background: #5a6268;
        }
        
        .btn:disabled {
            opacity: 0.6;
            cursor: not-allowed;
            transform: none;
        }
        
        .loading {
            display: none;
            text-align: center;
            padding: 20px;
            color: #6c757d;
        }
        
        .spinner {
            border: 3px solid #f3f3f3;
            border-top: 3px solid #667eea;
            border-radius: 50%;
            width: 30px;
            height: 30px;
            animation: spin 1s linear infinite;
            margin: 0 auto 10px;
        }
        
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        
        .result-card {
            background: white;
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        
        .result-card h3 {
            margin-bottom: 15px;
            color: #495057;
            display: flex;
            align-items: center;
            gap: 10px;
        }
        
        .success-icon {
            color: #28a745;
            font-size: 1.2em;
        }
        
        .error-icon {
            color: #dc3545;
            font-size: 1.2em;
        }
        
                 .sql-code {
             background: #1e1e1e;
             border: 1px solid #333;
             border-radius: 8px;
             padding: 20px;
             font-family: 'Consolas', 'Monaco', 'Courier New', monospace;
             font-size: 13px;
             line-height: 1.5;
             white-space: pre-wrap;
             overflow-x: auto;
             margin: 10px 0;
             color: #d4d4d4;
             box-shadow: 0 2px 8px rgba(0,0,0,0.1);
         }
        
        .validation-summary {
            display: flex;
            gap: 15px;
            margin: 15px 0;
            flex-wrap: wrap;
        }
        
        .validation-item {
            background: #e9ecef;
            padding: 8px 12px;
            border-radius: 20px;
            font-size: 0.9em;
            color: #495057;
        }
        
        .validation-item.valid {
            background: #d4edda;
            color: #155724;
        }
        
        .validation-item.error {
            background: #f8d7da;
            color: #721c24;
        }
        
        .context-usage {
            background: #e3f2fd;
            padding: 15px;
            border-radius: 8px;
            margin: 15px 0;
        }
        
        .context-usage h4 {
            margin-bottom: 10px;
            color: #1976d2;
        }
        
        .usage-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
            gap: 10px;
        }
        
        .usage-item {
            text-align: center;
            padding: 10px;
            background: white;
            border-radius: 6px;
        }
        
        .usage-value {
            font-size: 1.2em;
            font-weight: bold;
            color: #1976d2;
        }
        
        .usage-label {
            font-size: 0.8em;
            color: #666;
            margin-top: 5px;
        }
        
        .execution-result {
            background: #fff3cd;
            border: 1px solid #ffeaa7;
            border-radius: 8px;
            padding: 15px;
            margin: 15px 0;
        }
        
        .execution-result h4 {
            color: #856404;
            margin-bottom: 10px;
        }
        
        .example-queries {
            background: #f8f9fa;
            padding: 20px;
            border-radius: 10px;
            margin-top: 20px;
        }
        
        .example-queries h4 {
            margin-bottom: 15px;
            color: #495057;
        }
        
        .example-list {
            list-style: none;
        }
        
        .example-list li {
            padding: 8px 0;
            border-bottom: 1px solid #e9ecef;
            cursor: pointer;
            transition: color 0.3s ease;
        }
        
        .example-list li:hover {
            color: #667eea;
        }
        
        .example-list li:last-child {
            border-bottom: none;
        }
        
        @media (max-width: 768px) {
            .main-content {
                flex-direction: column;
            }
            
            .chat-section,
            .results-section {
                border-right: none;
                border-bottom: 1px solid #e9ecef;
            }
            
            .button-group {
                flex-direction: column;
            }
            
            .status-bar {
                flex-direction: column;
                align-items: flex-start;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🚀 DUI Multi-Agent SQL System</h1>
            <p>Natural Language to SQL Conversion with Optimized Context Usage</p>
        </div>
        
        <div class="status-bar">
            <div class="status-item">
                <div class="status-indicator" id="systemStatus"></div>
                <span id="statusText">Loading...</span>
            </div>
            <div class="status-item">
                <span>Agents: <span id="agentCount">-</span></span>
            </div>
            <div class="status-item">
                <span>Views: <span id="viewCount">-</span></span>
            </div>
            <div class="status-item">
                <span>Cache: <span id="cacheRatio">-</span></span>
            </div>
            <div class="status-item">
                <span>Context Reduction: <span id="contextReduction">-</span></span>
            </div>
        </div>
        
        <div class="main-content">
            <div class="chat-section">
                <div class="input-group">
                    <label for="queryInput">Enter your query:</label>
                    <textarea 
                        id="queryInput" 
                        class="query-input" 
                        placeholder="Example: Show me recent DUI cases from the last 30 days"
                    ></textarea>
                </div>
                
                <div class="button-group">
                    <button class="btn btn-primary" onclick="processQuery(false)">Generate SQL</button>
                    <button class="btn btn-secondary" onclick="processQuery(true)">Generate & Execute</button>
                    <button class="btn btn-secondary" onclick="clearResults()">Clear</button>
                </div>
                
                <div class="loading" id="loading">
                    <div class="spinner"></div>
                    <p>Processing your query...</p>
                </div>
                
                <div class="example-queries">
                    <h4>💡 Example Queries:</h4>
                    <ul class="example-list">
                        <li onclick="setQuery('Show me recent DUI cases from the last 30 days')">Show me recent DUI cases from the last 30 days</li>
                        <li onclick="setQuery('Count how many defendants had BAC above 0.08')">Count how many defendants had BAC above 0.08</li>
                        <li onclick="setQuery('List officers with the most DUI arrests')">List officers with the most DUI arrests</li>
                        <li onclick="setQuery('Find cases with field sobriety test failures')">Find cases with field sobriety test failures</li>
                        <li onclick="setQuery('Show me cases with high BAC levels and failed field tests')">Show me cases with high BAC levels and failed field tests</li>
                    </ul>
                </div>
            </div>
            
            <div class="results-section">
                <h2>Results</h2>
                <div id="results"></div>
            </div>
        </div>
    </div>

    <script>
        // Global variables
        let systemStatus = 'loading';
        
        // Initialize the application
        document.addEventListener('DOMContentLoaded', function() {
            loadSystemStatus();
            
            // Add enter key support for query input
            document.getElementById('queryInput').addEventListener('keydown', function(e) {
                if (e.key === 'Enter' && e.ctrlKey) {
                    processQuery(false);
                }
            });
        });
        
        // Load system status
        async function loadSystemStatus() {
            try {
                const response = await fetch('/api/status');
                const status = await response.json();
                
                updateStatusDisplay(status);
                systemStatus = 'ready';
            } catch (error) {
                console.error('Failed to load system status:', error);
                updateStatusDisplay({
                    status: 'error',
                    agents_loaded: 0,
                    total_views: 0,
                    cache_hit_ratio: 'N/A',
                    context_reduction: 'N/A'
                });
                systemStatus = 'error';
            }
        }
        
        // Update status display
        function updateStatusDisplay(status) {
            const statusIndicator = document.getElementById('systemStatus');
            const statusText = document.getElementById('statusText');
            
            if (status.status === 'operational') {
                statusIndicator.className = 'status-indicator';
                statusText.textContent = 'System Ready';
            } else {
                statusIndicator.className = 'status-indicator error';
                statusText.textContent = 'System Error';
            }
            
            document.getElementById('agentCount').textContent = status.agents_loaded;
            document.getElementById('viewCount').textContent = status.total_views;
            document.getElementById('cacheRatio').textContent = status.cache_hit_ratio;
            document.getElementById('contextReduction').textContent = status.context_reduction;
        }
        
        // Set query from example
        function setQuery(query) {
            document.getElementById('queryInput').value = query;
        }
        
        // Process query
        async function processQuery(execute) {
            const query = document.getElementById('queryInput').value.trim();
            if (!query) {
                alert('Please enter a query');
                return;
            }
            
            if (systemStatus !== 'ready') {
                alert('System is not ready. Please wait...');
                return;
            }
            
            showLoading(true);
            
            try {
                const response = await fetch('/api/query', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        query: query,
                        execute: execute
                    })
                });
                
                const result = await response.json();
                
                if (response.ok) {
                    displayResults(result);
                } else {
                    displayError(result.detail || 'An error occurred');
                }
            } catch (error) {
                console.error('Query processing failed:', error);
                displayError('Failed to process query. Please try again.');
            } finally {
                showLoading(false);
            }
        }
        
        // Display results
        function displayResults(result) {
            const resultsDiv = document.getElementById('results');
            
            const resultHtml = `
                <div class="result-card">
                    <h3>
                        <span class="${result.success ? 'success-icon' : 'error-icon'}">
                            ${result.success ? '✅' : '❌'}
                        </span>
                        Query Result
                    </h3>
                    
                    <div><strong>Query:</strong> ${escapeHtml(result.query)}</div>
                    
                                         ${result.sql ? `
                         <div style="margin-top: 15px;">
                             <strong>Generated SQL:</strong>
                             <div class="sql-code">${formatSQL(escapeHtml(result.sql))}</div>
                         </div>
                     ` : ''}
                    
                    ${result.explanation ? `
                        <div style="margin-top: 15px;">
                            <strong>Explanation:</strong>
                            <div style="background: #f8f9fa; padding: 10px; border-radius: 5px; margin-top: 5px;">
                                ${escapeHtml(result.explanation)}
                            </div>
                        </div>
                    ` : ''}
                    
                    ${result.validation ? `
                        <div style="margin-top: 15px;">
                            <strong>Validation:</strong>
                            <div class="validation-summary">
                                <div class="validation-item ${result.validation.is_valid ? 'valid' : 'error'}">
                                    ${result.validation.is_valid ? '✅ Valid' : '❌ Invalid'}
                                </div>
                                <div class="validation-item">
                                    Errors: ${result.validation.errors ? result.validation.errors.length : 0}
                                </div>
                                <div class="validation-item">
                                    Warnings: ${result.validation.warnings ? result.validation.warnings.length : 0}
                                </div>
                            </div>
                            ${result.validation.summary ? `
                                <div style="margin-top: 10px; font-style: italic; color: #6c757d;">
                                    ${escapeHtml(result.validation.summary)}
                                </div>
                            ` : ''}
                        </div>
                    ` : ''}
                    
                    ${result.context_usage ? `
                        <div class="context-usage">
                            <h4>Context Usage</h4>
                            <div class="usage-grid">
                                <div class="usage-item">
                                    <div class="usage-value">${result.context_usage.total_estimated || 'N/A'}</div>
                                    <div class="usage-label">Total Context</div>
                                </div>
                                <div class="usage-item">
                                    <div class="usage-value">${result.context_usage.views_used || 0}</div>
                                    <div class="usage-label">Views Used</div>
                                </div>
                                <div class="usage-item">
                                    <div class="usage-value">${result.context_usage.context_reduction || 'N/A'}</div>
                                    <div class="usage-label">Reduction</div>
                                </div>
                            </div>
                        </div>
                    ` : ''}
                    
                    ${result.execution_result ? `
                        <div class="execution-result">
                            <h4>Execution Result</h4>
                            <div><strong>Executed:</strong> ${result.execution_result.executed ? '✅ Yes' : '❌ No'}</div>
                            ${result.execution_result.executed ? `
                                <div><strong>Rows Returned:</strong> ${result.execution_result.rows_returned || 0}</div>
                                ${result.execution_result.columns ? `
                                    <div><strong>Columns:</strong> ${result.execution_result.columns.join(', ')}</div>
                                ` : ''}
                            ` : `
                                <div><strong>Reason:</strong> ${escapeHtml(result.execution_result.reason || 'Unknown')}</div>
                            `}
                        </div>
                    ` : ''}
                    
                    <div style="margin-top: 15px; font-size: 0.9em; color: #6c757d;">
                        <strong>Timestamp:</strong> ${new Date(result.timestamp).toLocaleString()}
                    </div>
                </div>
            `;
            
            resultsDiv.innerHTML = resultHtml;
        }
        
        // Display error
        function displayError(message) {
            const resultsDiv = document.getElementById('results');
            resultsDiv.innerHTML = `
                <div class="result-card">
                    <h3>
                        <span class="error-icon">❌</span>
                        Error
                    </h3>
                    <div style="color: #dc3545;">${escapeHtml(message)}</div>
                </div>
            `;
        }
        
        // Show/hide loading
        function showLoading(show) {
            const loading = document.getElementById('loading');
            const buttons = document.querySelectorAll('.btn');
            
            if (show) {
                loading.style.display = 'block';
                buttons.forEach(btn => btn.disabled = true);
            } else {
                loading.style.display = 'none';
                buttons.forEach(btn => btn.disabled = false);
            }
        }
        
        // Clear results
        function clearResults() {
            document.getElementById('results').innerHTML = '';
            document.getElementById('queryInput').value = '';
        }
        
                 // Escape HTML
         function escapeHtml(text) {
             const div = document.createElement('div');
             div.textContent = text;
             return div.innerHTML;
         }
         
         // Format SQL for better display
         function formatSQL(sql) {
             // Remove any remaining JSON wrapper
             if (sql.trim().startsWith('{') && sql.trim().endsWith('}')) {
                 try {
                     const sqlData = JSON.parse(sql);
                     if (sqlData.sql_query) {
                         sql = sqlData.sql_query;
                     }
                 } catch (e) {
                     // If JSON parsing fails, use as-is
                 }
             }
             
             // Remove markdown code blocks if present
             sql = sql.replace(/^```\w*\s*/, '').replace(/\s*```$/, '');
             
             // Basic SQL formatting
             sql = sql
                 .replace(/\bSELECT\b/gi, '<span style="color: #0066cc; font-weight: bold;">SELECT</span>')
                 .replace(/\bFROM\b/gi, '<span style="color: #0066cc; font-weight: bold;">FROM</span>')
                 .replace(/\bWHERE\b/gi, '<span style="color: #0066cc; font-weight: bold;">WHERE</span>')
                 .replace(/\bAND\b/gi, '<span style="color: #0066cc; font-weight: bold;">AND</span>')
                 .replace(/\bOR\b/gi, '<span style="color: #0066cc; font-weight: bold;">OR</span>')
                 .replace(/\bIN\b/gi, '<span style="color: #0066cc; font-weight: bold;">IN</span>')
                 .replace(/\bJOIN\b/gi, '<span style="color: #0066cc; font-weight: bold;">JOIN</span>')
                 .replace(/\bLEFT\b/gi, '<span style="color: #0066cc; font-weight: bold;">LEFT</span>')
                 .replace(/\bRIGHT\b/gi, '<span style="color: #0066cc; font-weight: bold;">RIGHT</span>')
                 .replace(/\bINNER\b/gi, '<span style="color: #0066cc; font-weight: bold;">INNER</span>')
                 .replace(/\bOUTER\b/gi, '<span style="color: #0066cc; font-weight: bold;">OUTER</span>')
                 .replace(/\bON\b/gi, '<span style="color: #0066cc; font-weight: bold;">ON</span>')
                 .replace(/\bORDER BY\b/gi, '<span style="color: #0066cc; font-weight: bold;">ORDER BY</span>')
                 .replace(/\bGROUP BY\b/gi, '<span style="color: #0066cc; font-weight: bold;">GROUP BY</span>')
                 .replace(/\bHAVING\b/gi, '<span style="color: #0066cc; font-weight: bold;">HAVING</span>')
                 .replace(/\bCOUNT\b/gi, '<span style="color: #cc6600; font-weight: bold;">COUNT</span>')
                 .replace(/\bSUM\b/gi, '<span style="color: #cc6600; font-weight: bold;">SUM</span>')
                 .replace(/\bAVG\b/gi, '<span style="color: #cc6600; font-weight: bold;">AVG</span>')
                 .replace(/\bMAX\b/gi, '<span style="color: #cc6600; font-weight: bold;">MAX</span>')
                 .replace(/\bMIN\b/gi, '<span style="color: #cc6600; font-weight: bold;">MIN</span>')
                 .replace(/\bAS\b/gi, '<span style="color: #0066cc; font-weight: bold;">AS</span>')
                 .replace(/\bDISTINCT\b/gi, '<span style="color: #0066cc; font-weight: bold;">DISTINCT</span>')
                 .replace(/\bTOP\b/gi, '<span style="color: #0066cc; font-weight: bold;">TOP</span>')
                 .replace(/\bDATEADD\b/gi, '<span style="color: #cc6600; font-weight: bold;">DATEADD</span>')
                 .replace(/\bGETDATE\b/gi, '<span style="color: #cc6600; font-weight: bold;">GETDATE</span>')
                 .replace(/\bDUI\./g, '<span style="color: #009900; font-weight: bold;">DUI.</span>')
                 .replace(/\b(\w+\.\w+)/g, '<span style="color: #666666;">$1</span>');
             
             return sql;
         }
    </script>
</body>
</html>"""
    
    with open(templates_dir / "index.html", "w", encoding="utf-8") as f:
        f.write(html_content)

# Create the HTML template when the module is imported
create_html_template()

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="DUI Multi-Agent Web Interface")
    parser.add_argument("--host", default="127.0.0.1", help="Host to bind to")
    parser.add_argument("--port", type=int, default=8000, help="Port to bind to")
    parser.add_argument("--reload", action="store_true", help="Enable auto-reload")
    
    args = parser.parse_args()
    
    print("🚀 Starting DUI Multi-Agent Web Interface...")
    print(f"📊 System Status: {'Ready' if system_ready else 'Not Ready'}")
    print(f"🌐 Web Interface: http://{args.host}:{args.port}")
    print(f"📚 API Documentation: http://{args.host}:{args.port}/docs")
    
    uvicorn.run(
        "web_interface:app",
        host=args.host,
        port=args.port,
        reload=args.reload,
        log_level="info"
    )
