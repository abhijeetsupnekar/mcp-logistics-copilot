# 🚚 Logistics MCP Orchestrator

> Enterprise AI Logistics Copilot built using **Model Context Protocol (MCP)**, **Microsoft Foundry**, **Azure App Service**, and **GitHub Actions**.

---

# Overview

The **Logistics MCP Orchestrator** is the central orchestration layer of the Enterprise Logistics Copilot platform.

It communicates with multiple independent MCP servers and combines their responses to provide intelligent logistics capabilities through a single interface.

Instead of embedding all business logic in one application, the platform follows an **MCP-first architecture**, where every business capability is implemented as an independent MCP server.

---

# Project Objectives

This project demonstrates how to build an enterprise AI application using:

* Model Context Protocol (MCP)
* Microsoft Foundry Agents
* Azure App Service
* GitHub Actions CI/CD
* FastMCP
* Python

---

# System Architecture

```text
                    Microsoft Foundry Agent
                              │
                              ▼
                Logistics MCP Orchestrator
                              │
        ┌──────────────┬──────┴──────┬──────────────┐
        ▼              ▼             ▼              ▼
 Database MCP     Maps MCP     Weather MCP   Notification MCP
```

---

# Responsibilities

The Logistics Orchestrator is responsible for:

* Coordinating all MCP servers
* Aggregating business responses
* Providing AI-ready business tools
* Exposing MCP tools
* Handling orchestration logic
* Managing service-to-service communication

---

# Connected MCP Servers

| MCP Server       | Responsibility                  |
| ---------------- | ------------------------------- |
| Database MCP     | Shipment & Tracking Information |
| Maps MCP         | Distance & ETA                  |
| Weather MCP      | Weather Conditions              |
| Notification MCP | Email Notifications             |

---

# Features

* Shipment Status
* Shipment Tracking
* Shipment ETA
* Weather-aware ETA
* Delayed Shipment Alerts
* Microsoft Foundry Integration
* Azure Deployment
* GitHub Actions CI/CD
* MCP Inspector Validation

---

# Technology Stack

## Backend

* Python 3.11
* FastMCP
* MCP SDK
* FastAPI
* HTTPX
* Uvicorn
* Gunicorn

## Cloud

* Azure App Service
* GitHub Actions

## AI Platform

* Microsoft Foundry
* Model Context Protocol (MCP)

---

# Project Structure

```text
Logistics-Orchestrator
│
├── src
│   ├── server.py
│   ├── mcp_client.py
│   │
│   ├── services
│   │     └── logistics_service.py
│   │
│   └── __init__.py
│
├── .github
│     └── workflows
│
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

# Environment Variables

Create a `.env` file.

```env
DATABASE_MCP_URL=
MAPS_MCP_URL=
WEATHER_MCP_URL=
NOTIFICATION_MCP_URL=
```

---

# Installation

Clone repository

```bash
git clone https://github.com/<your-account>/logistics-orchestrator.git
```

Move into project

```bash
cd logistics-orchestrator
```

Create virtual environment

```bash
python -m venv .venv
```

Activate

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

# Running Locally

```bash
python src/server.py
```

or

```bash
uvicorn src.server:app
```

---

# Available MCP Tools

## shipment_status_tool()

Returns

* Shipment Status
* Driver Details
* Vehicle Information
* Tracking History

---

## shipment_eta_tool()

Combines

* Database MCP
* Maps MCP
* Weather MCP

Returns

* Shipment Status
* Distance
* ETA
* Weather
* Temperature

---

## delayed_shipments_alert_tool()

Detects delayed shipments and triggers notifications through Notification MCP.

---

# Business Flow

Shipment ETA Request

```text
User

↓

Microsoft Foundry

↓

shipment_eta_tool()

↓

Database MCP

↓

Maps MCP

↓

Weather MCP

↓

Combine Results

↓

Return Response
```

---

# Deployment

The application is deployed on **Azure App Service**.

Deployment pipeline:

```text
Developer

↓

Git Push

↓

GitHub Actions

↓

Azure App Service

↓

Logistics Orchestrator
```

Deployment Features

* Automatic Build
* Automatic Deployment
* Environment Variables
* Secure Transport
* Production Configuration

---

# Microsoft Foundry Integration

The Logistics Orchestrator is connected to a Microsoft Foundry Agent.

Validated scenarios include:

* Shipment Status
* Shipment ETA
* Delayed Shipment Alerts

---

# Sample Prompts

```text
What is the status of shipment SHP001?
```

```text
Show ETA for shipment SHP003.
```

```text
Notify me about delayed shipments.
```

---

# Production Readiness

Completed

* Production Logging
* Exception Handling
* Azure Deployment
* GitHub Actions
* Environment Variables
* MCP Inspector Validation
* Microsoft Foundry Integration
* Clean Architecture
* Modular MCP Servers

---

# Future Enhancements

* Fleet Management
* Driver Management
* Warehouse Integration
* Route Optimization
* Traffic Intelligence
* Delivery Risk Prediction
* Azure Monitor
* Application Insights
* Docker Support
* Kubernetes Deployment
* Authentication & Authorization

---

# Version

Current Version

```
v1.0.0
```

---

# Author

Abhijeet Supnekar

Enterprise AI Engineering Learning Project

---

# License

This repository is intended for educational, research and enterprise learning purposes.
