# 🗺️ Logistics Maps MCP

> Maps MCP Server for the Enterprise Logistics Copilot Platform.

The **Maps MCP** provides route planning, distance calculation, and Estimated Time of Arrival (ETA) services through the **Model Context Protocol (MCP)**.

It abstracts mapping and routing services behind a standardized MCP interface, allowing AI agents and orchestrators to consume logistics routing intelligence without direct integration with mapping providers.

---

# Overview

The Maps MCP is responsible for all location intelligence within the Logistics Copilot platform.

Instead of allowing every application to communicate directly with external mapping services, the Maps MCP provides a reusable, centralized service responsible for:

* Route Calculation
* Distance Estimation
* ETA Calculation
* Address Validation
* Logistics Route Intelligence

This architecture improves modularity, maintainability, and future extensibility.

---

# Responsibilities

The Maps MCP provides:

* Route Estimation
* Distance Calculation
* Travel Duration
* Estimated Arrival Time
* Address-to-Address Routing

---

# System Architecture

```text
                 Logistics Orchestrator
                         │
                         ▼
                   Maps MCP Server
                         │
                         ▼
                 Google Maps API
```

---

# Features

* Route by Address
* Distance Calculation
* ETA Calculation
* Logistics Route Planning
* MCP Tool Interface
* Azure Deployment
* GitHub Actions CI/CD

---

# Technology Stack

## Backend

* Python 3.11
* MCP SDK
* HTTPX
* Requests
* Uvicorn
* Gunicorn

## External Service

* Google Maps Distance Matrix API
* Google Maps Directions API

---

# Project Structure

```text
Maps-MCP/
│
├── src/
│   ├── server.py
│   ├── maps_service.py
│   ├── maps_client.py
│   ├── tools/
│   │     ├── estimate_eta_tool.py
│   │     └── route_tool.py
│   └── __init__.py
│
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

> Update the folder names if they differ in your repository.

---

# Environment Variables

Create a `.env` file.

```env
GOOGLE_MAPS_API_KEY=
```

---

# Installation

Clone the repository

```bash
git clone https://github.com/<your-account>/maps-mcp.git
```

Navigate to the project

```bash
cd maps-mcp
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate the environment

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

## estimate_eta_tool

### Input

```json
{
  "origin_address": "Pune",
  "destination_address": "Mumbai"
}
```

### Returns

* Distance (km)
* Estimated Duration
* Estimated Arrival Time

---

## route_by_address_tool

### Input

```json
{
  "origin_address": "Pune",
  "destination_address": "Mumbai"
}
```

### Returns

* Origin
* Destination
* Route Information
* Distance
* Duration

---

# Request Flow

```text
Logistics Orchestrator

        │

        ▼

estimate_eta_tool()

        │

        ▼

Google Maps API

        │

        ▼

Distance Matrix

        │

        ▼

ETA Response
```

---

# Sample Response

```json
{
  "distance_km": 152,
  "duration_minutes": 180,
  "estimated_arrival": "2026-06-26T16:45:00"
}
```

---

# Deployment

The Maps MCP is deployed on **Azure App Service**.

Deployment pipeline:

Developer

↓

Git Push

↓

GitHub Actions

↓

Azure App Service

↓

Maps MCP

---

# Security

* Google API Key stored in Azure App Settings
* No API keys committed to source control
* Environment variable configuration
* Secure MCP endpoint

---

# Production Readiness

Completed

* Azure Deployment
* GitHub Actions CI/CD
* Environment Variables
* Exception Handling
* Production Logging
* MCP Inspector Validation
* Secure API Configuration

---

# Future Enhancements

* Traffic-aware ETA
* Multi-stop Route Optimization
* Toll Estimation
* Fuel Consumption Estimation
* Reverse Geocoding
* Route Alternatives
* Delivery Zone Calculation
* Geofencing
* Vehicle Routing Optimization

---

# Integration

The Maps MCP is consumed by:

* Logistics Orchestrator MCP
* Microsoft Foundry Agent
* AI Logistics Copilot

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
