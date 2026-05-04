# SOC Packet Analyzer

A lightweight network traffic analyzer for SOC environments that detects suspicious activity including port scans and traffic anomalies.

## Features
- Real-time packet capture (Scapy)
- IP traffic volume monitoring
- **Port scan detection** (identifies hosts scanning >10 ports)
- JSON logging for SIEM integration
- Configurable alert thresholds

## How It Works
1. Captures live IP packets
2. Tracks packet count per source IP
3. Monitors TCP port access patterns
4. Triggers alerts for:
   - Traffic spikes (>100 packets in window)
   - Potential port scans (>10 unique ports from single IP)

## Quick Start

```bash
git clone https://github.com/George-gb1/soc-packet-analyzer
cd soc-packet-analyzer
pip install -r requirements.txt
sudo python3 analyzer.py
