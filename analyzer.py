from scapy.all import *
import json
import time

print("[*] SOC Analyzer v4 Running...")

ip_count = {}
THRESHOLD = 10

def log_event(data):
    with open("soc_alerts.json", "a") as f:
        f.write(json.dumps(data) + "\n")

def analyze(packet):
    if packet.haslayer(IP):
        src = packet[IP].src

        if src in ip_count:
            ip_count[src] += 1
        else:
            ip_count[src] = 1

        count = ip_count[src]

        event = {
            "time": time.strftime("%Y-%m-%d %H:%M:%S"),
            "src_ip": src,
            "count": count
        }

        if count > THRESHOLD:
            event["status"] = "ALERT"
            print(f"[ALERT] {src} → {count}")
        else:
            event["status"] = "NORMAL"
            print(f"[NORMAL] {src} → {count}")

        log_event(event)

sniff(iface="eth0", prn=analyze, store=False)
