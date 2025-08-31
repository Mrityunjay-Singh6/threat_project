from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

DB_FILE = 'iocs.sqlite'  # your local IOC DB
ALERT_LOG = 'alerts.log'  # your alert log file

# Endpoint to get last 10 alerts
@app.route('/alerts', methods=['GET'])
def get_alerts():
    try:
        with open(ALERT_LOG, 'r') as f:
            lines = f.readlines()
            last_10 = lines[-10:] if len(lines) >= 10 else lines
        return jsonify({'last_alerts': last_10})
    except Exception as e:
        return jsonify({'error': str(e)})

# Endpoint to get all IOCs
@app.route('/iocs', methods=['GET'])
def get_iocs():
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM iocs LIMIT 50")
        rows = cursor.fetchall()
        conn.close()
        return jsonify({'iocs': rows})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

