from flask import Flask, send_from_directory, request, jsonify
import os

from runtime import DevineRuntime

app = Flask(__name__)

# entities base path
ENTITIES_PATH = "../GREEK"


# serve dashboard
@app.route("/")
def dashboard():
    return send_from_directory("../dashboard", "index.html")


@app.route("/<path:path>")
def static_files(path):
    return send_from_directory("../dashboard", path)


# awaken entity
@app.route("/awake", methods=["POST"])
def awaken_entity():

    data = request.json
    pantheon = data.get("pantheon")
    entity = data.get("entity")

    entity_path = f"../{pantheon}/{entity}"

    if not os.path.exists(entity_path):
        return jsonify({"error": "Entity not found"}), 404

    runtime = DevineRuntime(entity_path)

    return jsonify({
        "status": "awakened",
        "entity": entity
    })


# chat with entity
@app.route("/chat", methods=["POST"])
def chat():

    data = request.json
    pantheon = data.get("pantheon")
    entity = data.get("entity")
    message = data.get("message")

    entity_path = f"../{pantheon}/{entity}"

    runtime = DevineRuntime(entity_path)

    response = runtime.cognition.chat(message, runtime.memory)

    return jsonify({
        "entity": entity,
        "response": response
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
