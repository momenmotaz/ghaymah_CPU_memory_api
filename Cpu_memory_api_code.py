import psutil
from flask import Flask, jsonify, request
import datetime

app = Flask(__name__)

# تخزين اسم السيرفر كـ Global Variable
server_config = {"server_name": None}

@app.route('/configure', methods=['POST'])
def configure():
    data = request.json
    server_config["server_name"] = data.get("server_name")
    return {"message": "Server configured successfully"}, 200

@app.route('/system_usage', methods=['GET'])
def system_usage():
    # التحقق إذا كان السيرفر تم تكوينه مسبقًا
    if not server_config["server_name"]:
        return {"error": "Please configure server first"}, 400

    # الحصول على معلومات النظام
    cpu_usage_percent = psutil.cpu_percent()
    memory_info = psutil.virtual_memory()

    # تحويل الذاكرة من Bytes إلى GB
    total_memory_gb = round(memory_info.total / (1024**3), 2)
    used_memory_gb = round(memory_info.used / (1024**3), 2)

    # إنشاء الرد النهائي
    response = {
        "cpu_usage": f"{cpu_usage_percent}%",  # نسبة استخدام المعالج
        "memory_usage": {
            "total_memory": f"{total_memory_gb} GB",  # إجمالي الذاكرة
            "used_memory": f"{used_memory_gb} GB"    # الذاكرة المستخدمة
        },
        "server_name": server_config["server_name"],  # اسم السيرفر
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # الوقت الحالي
    }
    return jsonify(response), 200

@app.route('/configure', methods=['PUT'])
def update_server_name():
    data = request.json

    # التحقق إذا كان السيرفر موجودًا بالفعل
    if not server_config["server_name"]:
        return {"error": "Please configure server first before updating."}, 400

    # تحديث اسم السيرفر
    new_server_name = data.get("server_name")
    if not new_server_name:
        return {"error": "Server name is required for updating."}, 400

    server_config["server_name"] = new_server_name
    return {"message": "Server name updated successfully", "new_server_name": new_server_name}, 200

if __name__ == "__main__":
    app.run(debug=True)
