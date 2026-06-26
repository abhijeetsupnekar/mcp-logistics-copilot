# 🌦️ Logistics Weather MCP

> Weather MCP Server for the Enterprise Logistics Copilot Platform.

The **Weather MCP** provides real-time weather information and weather forecasts through the **Model Context Protocol (MCP)**.

It enables AI agents and orchestration services to incorporate weather conditions into logistics planning, shipment monitoring, and ETA calculations without directly integrating with weather service providers.

---

# Overview

The Weather MCP is responsible for delivering weather intelligence to the Logistics Copilot platform.

Instead of allowing each application to communicate directly with external weather APIs, the Weather MCP provides a centralized service that exposes weather capabilities through standardized MCP tools.

This modular design makes weather services reusable across multiple AI applications while keeping business logic independent from external providers.

---

# Responsibilities

The Weather MCP provides:

* Current Weather
* Weather Forecast
* Temperature Information
* Weather Conditions
* Weather Intelligence for Logistics

---

# System Architecture

```text
                 Logistics Orchestrator
                         │
                         ▼
                 Weather MCP Server
                         │
                         ▼
                  Weather API Provider
```

---

# Features

* Current Weather Lookup
* Multi-day Weather Forecast
* Temperature Information
* Weather Conditions
* MCP Tool Interface
* Azure Deployment
* GitHub Actions CI/CD

---

# Technology Stack

## Backend

* Python 3.11
* MCP SDK
* Requests
* Uvicorn
* Gunicorn

## External Service

* Weather API

---

# Project Structure

```text
Weather-MCP/
│
├── src/
│
├── server.py
├── weather_service.py
├── weather_client.py
│
├── tools/
│   ├── current_weather_tool.py
│   └── forecast_weather_tool.py
│
├── __init__.py
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
WEATHER_API_KEY=
```

---

# Installation

Clone the repository

```bash
git clone https://github.com/<your-account>/weather-mcp.git
```

Navigate to the project

```bash
cd weather-mcp
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate the environment

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

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

## current_weather_tool

### Input

```json
{
  "city": "Mumbai"
}
```

### Returns

* City
* Temperature
* Weather Condition
* Humidity
* Wind Speed

---

## forecast_weather_tool

### Input

```json
{
  "city": "Mumbai"
}
```

### Returns

* Forecast
* High Temperature
* Low Temperature
* Weather Conditions
* Rain Probability (if available)

---

# Request Flow

```text
Logistics Orchestrator

        │

        ▼

current_weather_tool()

        │

        ▼

Weather MCP

        │

        ▼

Weather API

        │

        ▼

Weather Response

        │

        ▼

Logistics Orchestrator
```

---

# Sample Response

```json
{
  "city": "Mumbai",
  "temperature_c": 31,
  "condition": "Partly Cloudy",
  "humidity": 72,
  "wind_kph": 18
}
```

---

# Integration with Logistics Copilot

The Weather MCP is used by the Logistics Orchestrator to enrich shipment information.

Example workflow:

```text
Shipment ETA Request

        │

        ▼

Retrieve Shipment

        │

        ▼

Retrieve Route ETA

        │

        ▼

Retrieve Weather

        │

        ▼

Combine Results

        │

        ▼

Return AI Response
```

Weather information helps logistics operators understand conditions that may impact delivery schedules.

---

# Deployment

The Weather MCP is deployed on **Azure App Service**.

Deployment pipeline

```text
Developer

↓

Git Push

↓

GitHub Actions

↓

Azure App Service

↓

Weather MCP
```

Deployment features

* Automatic Build
* Automatic Deployment
* Environment Variables
* Production Configuration
* Secure MCP Endpoint

---

# Security

* Weather API Key stored in Azure App Settings
* Environment-based configuration
* No secrets committed to source control
* Secure MCP endpoint

---

# Production Readiness

Completed

* Azure Deployment
* GitHub Actions CI/CD
* Environment Variables
* Production Logging
* Exception Handling
* MCP Inspector Validation
* Modular Architecture

---

# Future Enhancements

* Severe Weather Alerts
* Weather Risk Score
* Storm Detection
* Weather-based ETA Prediction
* Route Weather Analysis
* Historical Weather Data
* Multiple Weather Providers
* Weather Caching
* Automatic Retry Logic

---

# Integration

The Weather MCP is consumed by:

* Logistics Orchestrator MCP
* Microsoft Foundry Agent
* Enterprise Logistics Copilot

---

# Version

```text
v1.0.0
```

---

# Author

**Abhijeet Supnekar**

Enterprise AI Engineering Learning Project

---

# License

This repository is intended for educational, research, and enterprise learning purposes.
