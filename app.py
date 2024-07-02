from flask import Flask, request, jsonify
import time

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    input_text = data.get("inputText")
    time.sleep(400)  # Wait for 90 seconds
    return jsonify({"output": "some test output text"})

if __name__ == '__main__':
    app.run(debug=True)
