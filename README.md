# SOC Packet Analyzer 🔍

## 🚨 Overview

A lightweight SOC-style network monitoring tool built using Python.
This project captures live network traffic, analyzes IP behavior, detects suspicious activity, and logs events in real time.

---

## ⚙️ Features

* Real-time packet capture (Scapy)
* IP traffic monitoring
* Threshold-based alert detection
* JSON logging (SIEM-style)
* Detection of suspicious behavior

---

## 🧠 Skills Demonstrated

* Network Traffic Analysis
* Intrusion Detection Basics
* SOC Monitoring Concepts
* Log Analysis & SIEM Basics
* Python for Cybersecurity

---

## 🚀 How to Run

```bash
sudo python3 analyzer.py
```

---

## 📊 Example Output

```
[NORMAL] 192.168.1.10 → 3 packets  
[ALERT] 192.168.1.10 → 12 packets  
```

---

## 📁 Project Structure

```
soc-packet-analyzer/
│
├── analyzer.py
├── soc_alerts.json
├── README.md
└── requirements.txt
```

---

## 🎯 Project Purpose

This project simulates how a basic Security Operations Center (SOC) monitors network traffic and detects suspicious activity.

---

## 👨‍💻 Author

George Biswas
Aspiring SOC Analyst | Cybersecurity Enthusiast
