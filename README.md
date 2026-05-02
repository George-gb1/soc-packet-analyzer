# SOC Packet Analyzer

## Overview
A lightweight Python-based SOC tool that captures network traffic, analyzes IP behavior, and generates alerts for suspicious activity.

## eatures
- Real-time packet capture using Scapy
- IP-based traffic monitoring
- Threshold-based alert detection
- JSON logging for analysis
- Lightweight SOC-style architecture

## How it works
1. Captures live network packets
2. Extracts source IP addresses
3. Counts traffic per IP
4. Triggers alert if threshold is exceeded
5. Logs events into JSON file

## How to run
```bash
sudo python3 analyzer.py
