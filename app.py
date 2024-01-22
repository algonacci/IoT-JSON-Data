import os
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def index():
    return jsonify({
        "status": {
            "message": "Success fetching the API",
            "code": 200,
        }
    }), 200


@app.route("/post_data", methods=["POST"])
def post_data():
    if request.method == "POST":
        input_data = request.get_json()
        return jsonify(input_data), 200


if __name__ == "__main__":
    app.run(debug=True,
            host="0.0.0.0",
            port=int(os.environ.get("PORT", 8080)))
