"""
FastAPI Logging API
A simple API for logging user actions with timestamps.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from datetime import datetime
from typing import List


app = FastAPI(
    title="Logging API",
    description="API for logging user actions with timestamps",
    version="1.0.0"
)



logs: List[dict] = []


class LogEntry(BaseModel):
    """
    Pydantic model for log entry validation.
    Ensures user and action fields are provided as strings.
    """
    user: str = Field(..., description="Username or user identifier")
    action: str = Field(..., description="Action performed by the user")


class LogResponse(BaseModel):
    """
    Pydantic model for log response.
    Includes the log entry with its timestamp.
    """
    user: str
    action: str
    timestamp: str


@app.post("/log", response_model=LogResponse, status_code=201)
async def create_log(log_entry: LogEntry):
    """
    POST endpoint to create a new log entry.
    
    Args:
        log_entry: JSON object containing "user" and "action" fields
        
    Returns:
        LogResponse: The created log entry with timestamp
        
    Example:
        POST /log
        {
            "user": "john_doe",
            "action": "login"
        }
    """
    # Get current timestamp in ISO format
    timestamp = datetime.now().isoformat()
    
    # Create log entry dictionary
    log_data = {
        "user": log_entry.user,
        "action": log_entry.action,
        "timestamp": timestamp
    }
    
    # Append to global logs list
    logs.append(log_data)
    
    # Return the created log entry
    return log_data


@app.get("/logs", response_model=List[LogResponse])
async def get_logs():
    """
    GET endpoint to retrieve the latest 10 log entries.
    
    Returns:
        List[LogResponse]: List of the latest 10 log entries, 
                          ordered from newest to oldest
                          
    Example:
        GET /logs
        Returns up to 10 most recent log entries
    """
    # Get the latest 10 logs (most recent first)
    # Reverse the list to show newest first, then take last 10
    latest_logs = logs[-10:][::-1] if len(logs) > 0 else []
    
    return latest_logs


@app.get("/")
async def root():
    """
    Root endpoint providing API information.
    
    Returns:
        dict: API information and available endpoints
    """
    return {
        "message": "Logging API",
        "version": "1.0.0",
        "endpoints": {
            "POST /log": "Create a new log entry",
            "GET /logs": "Get latest 10 log entries"
        }
    }

