import sqlite3
from datetime import datetime

# Database file
DB_FILE = "threatintel.db"
LOG_FILE = "access.log"

# Dummy API fetch functions (existing code intact)
def fetch_abuseipdb():
    try:
        print("Fetching AbuseIPDB blacklist...")
        # original API fetch code here
    except Exception as e:
        print(f"Error fetching AbuseIPDB data: {e}")

def fetch_otx():
    try:
        print("Fetching AlienVault OTX indicators...")
        # original API fetch code here
    except Exception as e:
        print(f"OTX: {e}")

# Log scanning and alerting
def check_logs(log_file):
    print(f"\nScanning log file: {log_file}...")
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    alerts = []
    try:
        with open(log_file, "r") as f:
            for line in f:
                ip = line.strip()
                # Use correct column 'value' for IOC check
                cursor.execute("SELECT value, description FROM iocs WHERE value = ?", (ip,))
                result = cursor.fetchone()
                if result:
                    alert_msg = f"[!] ALERT: IOC match found! {result[0]} ({result[1]})"
                    print(alert_msg)
                    alerts.append(alert_msg)

        if alerts:
            with open("alerts.log", "a") as logf:
                for a in alerts:
                    logf.write(a + "\n")
            print(f"Total alerts: {len(alerts)} (also saved in alerts.log)")
        else:
            print("No alerts found in this log file.")

    except FileNotFoundError:
        print(f"Error: Log file '{log_file}' not found.")
    finally:
        conn.close()

# Sample log generator for testing
def write_sample_log():
    with open(LOG_FILE, "w") as f:
        f.write("192.168.1.101\n")  # matches dummy IOC
        f.write("10.0.0.5\n")       # benign IP
    print(f"Sample log written to {LOG_FILE}.")

if __name__ == "__main__":
    fetch_abuseipdb()
    fetch_otx()
    write_sample_log()
    check_logs(LOG_FILE)

