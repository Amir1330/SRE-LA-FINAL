from flask import Flask, jsonify, Response
from flask_cors import CORS
import time
import random
import os
import prometheus_client
from prometheus_client import Counter, Histogram, start_http_server

app = Flask(__name__)
CORS(app)

# Prometheus metrics
REQUEST_COUNT = Counter('app_request_count', 'Total app HTTP request count', ['method', 'endpoint', 'http_status'])
REQUEST_LATENCY = Histogram('app_request_latency_seconds', 'Request latency in seconds', ['method', 'endpoint'])

# Start prometheus metrics server on port 8000
start_http_server(8000)

@app.route('/')
def home():
    return "SRE Demo API is running!"

@app.route('/metrics')
def metrics():
    return Response(prometheus_client.generate_latest(), mimetype='text/plain')

@app.route('/api/health', methods=['GET'])
def health_check():
    start_time = time.time()
    status_code = 200
    
    # Simulate occasional slowness for monitoring demo
    if random.random() < 0.1:
        time.sleep(0.5)
    
    response = {"status": "healthy", "timestamp": time.time()}
    
    # Record metrics
    REQUEST_COUNT.labels('GET', '/api/health', status_code).inc()
    REQUEST_LATENCY.labels('GET', '/api/health').observe(time.time() - start_time)
    
    return jsonify(response), status_code

@app.route('/api/data', methods=['GET'])
def get_data():
    start_time = time.time()
    status_code = 200
    
    # Simulate occasional errors for alerting demo
    if random.random() < 0.05:
        status_code = 500
        response = {"error": "Internal server error", "timestamp": time.time()}
    else:
        response = {
            "data": [
                {"id": 1, "name": "Item 1", "value": random.randint(1, 100)},
                {"id": 2, "name": "Item 2", "value": random.randint(1, 100)},
                {"id": 3, "name": "Item 3", "value": random.randint(1, 100)}
            ],
            "timestamp": time.time()
        }
    
    # Record metrics
    REQUEST_COUNT.labels('GET', '/api/data', status_code).inc()
    REQUEST_LATENCY.labels('GET', '/api/data').observe(time.time() - start_time)
    
    return jsonify(response), status_code

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port) 