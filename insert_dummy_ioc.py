import sqlite3
from datetime import datetime

# Connect to database
conn = sqlite3.connect('threatintel.db')
c = conn.cursor()

# Dummy IOC data
ioc_type = "IP"
ioc_value = "192.168.1.101"  # dummy IP
description = "Dummy IOC for testing"
date_added = datetime.now().strftime("%Y-%m-%d")

# Insert into iocs table
c.execute("INSERT INTO iocs (type, value, description, date_added) VALUES (?, ?, ?, ?)",
          (ioc_type, ioc_value, description, date_added))

conn.commit()
conn.close()

print("Dummy IOC inserted successfully.")

