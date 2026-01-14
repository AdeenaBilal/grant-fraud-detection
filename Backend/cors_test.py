from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/test", methods=["GET"])
def test():
    return jsonify({"status": "CORS WORKS"})

if __name__ == "__main__":
    app.run(port=5000, debug=True)
