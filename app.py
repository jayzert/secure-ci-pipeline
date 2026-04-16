from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/hello", methods=["GET"])
def hello():
    return jsonify(message="Hello, CI Pipeline"), 200


@app.route("/health", methods=["GET"])
def health():
    return jsonify(status="OK"), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
