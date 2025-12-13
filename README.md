# FastAPI Logging API

A simple FastAPI-based backend service for logging user actions with timestamps.
This project demonstrates basic API design, request validation, and in-memory data storage using FastAPI.

## Features

- Create log entries using a POST API
- Retrieve the latest log entries using a GET API
- Automatic timestamp generation
- In-memory storage (no database required)
- Interactive API testing using Swagger UI

## Tech Stack

- Python 3.10+
- FastAPI
- Uvicorn
- Pydantic

## Project Structure
```
logging_api/
├── main.py
├── requirements.txt
└── README.md
```

## Setup Instructions

### 1. Create and activate virtual environment
```bash
python -m venv venv
```

**Windows**
```bash
venv\Scripts\activate
```

**Mac/Linux**
```bash
source venv/bin/activate
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

## Running the Application

Start the FastAPI server using Uvicorn:

```bash
uvicorn main:app --reload
```

The API will be available at:

**http://127.0.0.1:8000**

## API Endpoints

### 1. POST /log

Create a new log entry.

**Request Body**
```json
{
  "user": "arun",
  "action": "uploaded invoice"
}
```

**Response (201 Created)**
```json
{
  "user": "arun",
  "action": "uploaded invoice",
  "timestamp": "2025-12-14T01:50:10.882517"
}
```

### 2. GET /logs

Retrieve the latest 10 log entries.

**Response**
```json
[
  {
    "user": "arun",
    "action": "uploaded invoice",
    "timestamp": "2025-12-14T01:50:10.882517"
  }
]
```

## Testing the API

The API can be tested using Swagger UI:

**http://127.0.0.1:8000/docs**

From Swagger UI, you can:
- Test the POST /log endpoint
- Verify stored logs using GET /logs

## Notes

- Logs are stored in memory, so all data is reset when the server restarts.
- This project is intentionally kept simple to focus on API fundamentals.

