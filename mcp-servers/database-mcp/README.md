# 🗄️ Logistics Database MCP

> Database MCP Server for the Enterprise Logistics Copilot Platform.

The Database MCP exposes logistics data through the **Model Context Protocol (MCP)**, allowing AI agents and orchestrators to retrieve shipment, driver, vehicle, and tracking information without direct database access.

---

# Overview

The **Database MCP** acts as the data access layer for the Logistics Copilot platform.

Instead of allowing AI agents to query SQL Server directly, the Database MCP exposes a controlled set of MCP tools that retrieve logistics information securely.

This design keeps database access centralized, reusable, and independent from AI orchestration logic.

---

# Responsibilities

The Database MCP is responsible for:

* Shipment Information
* Shipment Summary
* Driver Information
* Vehicle Information
* Tracking Information
* Delayed Shipment Detection

---

# Architecture

```text
                 Logistics Orchestrator
                         │
                         ▼
                 Database MCP Server
                         │
                         ▼
                 SQL Server Database
```

---

# Features

* Shipment Lookup
* Shipment Summary
* Shipment Tracking
* Driver Details
* Vehicle Details
* Delayed Shipment Detection
* Secure Database Access
* MCP Tool Interface

---

# Technology Stack

## Backend

* Python 3.11
* MCP SDK
* SQLAlchemy
* PyODBC
* Uvicorn
* Gunicorn

## Database

* Microsoft SQL Server

---

# Project Structure

```text
Database-MCP/
│
├── src/
│   ├── server.py
│   ├── database.py
│   ├── models.py
│   ├── tools/
│   │   ├── shipment_tool.py
│   │   ├── tracking_tool.py
│   │   └── delayed_shipments_tool.py
│   └── __init__.py
│
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

> Adjust the folder names above if your implementation differs.

---

# Environment Variables

Create a `.env` file.

```env
DATABASE_CONNECTION_STRING=
```

Example

```text
Driver={ODBC Driver 18 for SQL Server};
Server=<server-name>;
Database=LogisticsDB;
UID=<username>;
PWD=<password>;
Encrypt=yes;
TrustServerCertificate=no;
```

---

# Installation

Clone repository

```bash
git clone https://github.com/<your-account>/database-mcp.git
```

Navigate to project

```bash
cd database-mcp
```

Create virtual environment

```bash
python -m venv .venv
```

Activate environment

Windows

```bash
.venv\Scripts\activate
```

Linux/macOS

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Running the MCP Server

```bash
python src/server.py
```

or

```bash
uvicorn src.server:app
```

---

# Available MCP Tools

## get_shipment_tool

Input

```json
{
  "shipment_code": "SHP001"
}
```

Returns

* Shipment Code
* Origin
* Destination
* Status

---

## get_tracking_tool

Returns

* Current Location
* Timestamp
* Tracking History

---

## get_shipment_summary_tool

Returns

* Shipment Information
* Driver Details
* Vehicle Details

---

## get_delayed_shipments_tool

Returns

* Delayed Shipment
* Delay Status
* Reason (if available)

---

# Database Design

The MCP interacts with the following entities:

* Shipment
* Driver
* Vehicle
* Tracking

Example relationship

```text
Shipment
   │
   ├── Driver
   ├── Vehicle
   └── Tracking
```

---

# Request Flow

```text
Logistics Orchestrator
          │
          ▼
 get_shipment_summary_tool
          │
          ▼
 SQLAlchemy
          │
          ▼
 SQL Server
          │
          ▼
 JSON Response
```

---

# Sample Response

```json
{
  "shipment": {
    "ShipmentCode": "SHP001",
    "Origin": "Pune",
    "Destination": "Mumbai",
    "Status": "In Transit"
  },
  "driver": {
    "DriverName": "John Smith"
  },
  "vehicle": {
    "VehicleNumber": "MH12AB1234"
  }
}
```

---

# Deployment

The Database MCP is deployed to **Azure App Service**.

Deployment includes:

* GitHub Actions CI/CD
* Environment Variables
* Production Configuration
* Secure MCP Endpoint

---

# Security

* No direct database access from AI agents
* Environment-based configuration
* Parameterized SQL through SQLAlchemy
* Secrets excluded from source control

---

# Production Readiness

Completed

* Azure Deployment
* GitHub Actions
* Environment Variables
* Exception Handling
* Production Logging
* SQLAlchemy Integration
* MCP Inspector Validation

---

# Future Enhancements

* Pagination
* Shipment Search
* Driver Search
* Vehicle Search
* Historical Tracking
* Bulk Shipment Queries
* Audit Logging
* Read-only Database Role
* Connection Pool Monitoring

---

# Version

```text
v1.0.0
```

---

# Author

Abhijeet Supnekar

Enterprise AI Engineering Learning Project

---

# License

This repository is intended for educational, research, and enterprise learning purposes.
