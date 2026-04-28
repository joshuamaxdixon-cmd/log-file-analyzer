from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route("/")
def home():
    return "Log File Analyzer is running 🚀"

@app.route("/analyze", methods=["POST"])
def analyze():
    file = request.files["file"]
    file.save("uploaded.log")

    result = subprocess.run(
        ["python3", "log_analyzer.py", "uploaded.log"],
        capture_output=True,
        text=True
    )

    return jsonify({
        "output": result.stdout
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)
