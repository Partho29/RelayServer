from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# simple in-memory store
state = {"move": ""}

@app.route("/set", methods=["POST"])
def set_move():
    data = request.get_json(silent=True) or {}
    mv = data.get("move", "")
    state["move"] = mv
    return jsonify({"ok": True, "move": state["move"]})

@app.route("/get", methods=["GET"])
def get_move():
    return jsonify({"move": state["move"]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(__import__("os").environ.get("PORT", 5000)))
