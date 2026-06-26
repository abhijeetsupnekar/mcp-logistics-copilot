# 🚚 Logistics MCP Orchestrator

## Overview

The **Logistics MCP Orchestrator** is the central orchestration service for the Logistics Copilot platform.

It integrates multiple specialized MCP (Model Context Protocol) servers into a single intelligent interface that can be consumed by Microsoft Foundry Agents, AI applications, or other MCP-compatible clients.

The orchestrator coordinates information from multiple backend services to provide real-time shipment intelligence.

---

## Architecture

```text
                    Microsoft Foundry Agent
                              │
                              ▼
                 Logistics MCP Orchestrator
                              │
      ┌──────────────┬─────────┼──────────────┬──────────────┐
      ▼              ▼         ▼              ▼
 Database MCP    Maps MCP   Weather MCP   Notification MCP
```

### MCP Services

| Service          | Purpose                                            |
| ---------------- | -------------------------------------------------- |
| Database MCP     | Shipment, Driver, Vehicle and Tracking Information |
| Maps MCP         | Distance, Route and ETA Estimation                 |
| Weather MCP      | Current Weather and Forecast                       |
| Notification MCP | Email Notifications                                |

---

## Features

* Shipment Status
* Shipment Tracking
* Shipment ETA
* Route Estimation
* Weather Lookup
* Delayed Shipment Alerts
* Microsoft Foundry Integration
* Azure App Service Deployment
* MCP Inspector Validation
* GitHub Actions CI/CD

---

## Technology Stack

* Python 3.11+
* Model Context Protocol (MCP)
* FastMCP
* FastAPI
* Uvicorn
* Gunicorn
* HTTPX
* Microsoft Foundry
* Azure App Service
* GitHub Actions

---

## Project Structure

```
Logistics-Orchestrator/
│
├── src/
│   ├── server.py
│   ├── mcp_client.py
│   ├── services/
│   │     └── logistics_service.py
│   └── __init__.py
│
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

## Environment Variables

Create a `.env` file.

```
DATABASE_MCP_URL=
MAPS_MCP_URL=
WEATHER_MCP_URL=
NOTIFICATION_MCP_URL=
```

---

## Installation

Clone the repository.

```bash
git clone <repository-url>
cd Logistics-Orchestrator
```

Create a virtual environment.

```bash
python -m venv .venv
```

Activate the environment.

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

---

## Running the Application

```bash
python src/server.py
```

or

```bash
uvicorn src.server:app
```

---

## Available MCP Tools

### shipment_status_tool

Returns

* Shipment Status
* Driver Information
* Vehicle Information
* Tracking Details

---

### shipment_eta_tool

Combines

* Database MCP
* Maps MCP
* Weather MCP

Returns

* Origin
* Destination
* ETA
* Distance
* Weather
* Temperature

---

### delayed_shipments_alert_tool

Checks delayed shipments and sends notification emails.

---

## Deployment

The application is deployed on **Azure App Service** using **GitHub Actions**.

Deployment includes:

* Automatic CI/CD
* Environment Variables
* Secure Transport Settings
* Streamable HTTP Transport

---

## Microsoft Foundry Integration

The Logistics MCP Orchestrator is connected to a Microsoft Foundry Agent.

Validated Scenarios:

* Shipment Status
* Shipment ETA
* Delayed Shipment Notification

---

## Sample Prompt

```
What is the status of shipment SHP001?
```

```
Give me the ETA for shipment SHP003.
```

```
Notify me about delayed shipments.
```

---

## Future Enhancements

* Fleet Management
* Warehouse Integration
* Route Optimization
* Traffic Intelligence
* Delivery Risk Prediction
* Authentication & Authorization
* Azure Monitor Integration
* Distributed Tracing
* Docker Support
* Kubernetes Deployment

---

## Production Readiness

* Production Logging
* Exception Handling
* Environment Variable Management
* GitHub Actions CI/CD
* Azure Deployment
* MCP Inspector Validation
* Microsoft Foundry Integration

---

## License

This project is intended for educational, research, and enterprise learning purposes.
