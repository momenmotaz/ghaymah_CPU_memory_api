from flask import Flask, request, jsonify
import psutil
from datetime import datetime

app = Flask(__name__)

# Memory to store server configuration
server_config = {}

# POST /configure
@app.route('/configure', methods=['POST'])
def configure_server():
    data = request.get_json()
    server_name = data.get("server_name")
    region = data.get("region")
    
    if not server_name or not region:
        return jsonify({"error": "server_name and region are required"}), 400
    
    server_config['server_name'] = server_name
    server_config['region'] = region
    return jsonify({"message": "Configuration successful"}), 200

# GET /system_usage
@app.route('/system_usage', methods=['GET'])
def system_usage():
    if 'server_name' not in server_config:
        return jsonify({"error": "Please configure server"}), 400
    
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    memory_usage = {
        "total": memory_info.total,
        "used": memory_info.used,
        "percentage": memory_info.percent
    }
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    response = {
        "server_name": server_config['server_name'],
        "cpu_usage_percent": cpu_usage,
        "memory_usage": memory_usage,
        "timestamp": current_time
    }
    return jsonify(response), 200

# UPDATE /configure
@app.route('/configure', methods=['PUT'])
def update_server():
    data = request.get_json()
    new_server_name = data.get("server_name")
    
    if not new_server_name:
        return jsonify({"error": "server_name is required"}), 400
    
    server_config['server_name'] = new_server_name
    return jsonify({"message": "Server name updated successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)
