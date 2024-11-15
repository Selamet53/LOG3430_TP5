from flask import Flask, jsonify, request
import time

app = Flask(__name__)

# Basic home endpoint
@app.route('/')
def home():
    return "Welcome to the test server!"

# Simulate a lightweight endpoint
@app.route('/fast')
def fast():
    return jsonify({"message": "This was quick!"})

# Simulate a medium processing endpoint
@app.route('/medium')
def medium():
    time.sleep(0.5)  # Simulate processing time
    return jsonify({"message": "This took a bit longer!"})

# Simulate a heavy processing endpoint
@app.route('/heavy')
def heavy():
    time.sleep(2)  # Simulate heavy processing time
    return jsonify({"message": "This took a while!"})

# Endpoint that takes a parameter and echoes it back
@app.route('/echo', methods=['POST'])
def echo():
    data = request.get_json()
    message = data.get("message", "No message sent")
    return jsonify({"echo": message})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
