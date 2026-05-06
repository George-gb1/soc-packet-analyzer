# SOC Analyzer v5
# Features:
# - Packet detection
# - Logging
# - Time-based analysis
# - Brute force detection
# - Multi-IP attack detection

import json
from datetime import datetime, timedelta

print("[*] Advanced SOC Analyzer - Multi-IP Detection Running...")

events = []

TIME_WINDOW = 10
IP_THRESHOLD = 3

# Load alert events
for line in open("soc_alerts.json", "r"):
    event = json.loads(line)

    if event["status"] != "ALERT":
        continue

    event_time = datetime.strptime(event["time"], "%Y-%m-%d %H:%M:%S")

    events.append({
        "ip": event["src_ip"],
        "time": event_time
    })

# Sort by time
events.sort(key=lambda x: x["time"])

print("\n[!] Multi-IP Attack Detection:\n")

for i in range(len(events)):
    unique_ips = set()
    base_time = events[i]["time"]

    for j in range(i, len(events)):
        if events[j]["time"] - base_time <= timedelta(seconds=TIME_WINDOW):
            unique_ips.add(events[j]["ip"])
        else:
            break

    if len(unique_ips) >= IP_THRESHOLD:
        print(f"[CRITICAL] Distributed attack detected → {len(unique_ips)} IPs within {TIME_WINDOW}s")
        print(f"IPs involved: {', '.join(unique_ips)}\n")
        break
