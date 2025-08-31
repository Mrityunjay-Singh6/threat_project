# Threat Intelligence Feed Processor & Anomaly Detector

## Overview
Python tool that fetches open-source threat intelligence, stores IOCs, compares against logs, and alerts suspicious activity.

## Features
- Fetches IOCs from AbuseIPDB & AlienVault OTX
- Stores IOCs in SQLite
- Processes simulated logs
- Detects anomalies & logs alerts
- REST API to view IOCs & last alerts
- Can be scheduled via cron

## Requirements
- Python 3.x
- Flask
- sqlite3
- requests

