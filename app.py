import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return {
        "system": "Devines Protocol",
        "core": "CHAOS",
        "status": "online"
    }

@app.route("/health")
def health():
    return {"status": "alive"}

@app.route("/pantheon")
def pantheon():
    return {
        "pantheon": "Greek",
        "gods": [
            "Zeus","Hera","Poseidon","Demeter",
            "Athena","Apollo","Artemis","Ares",
            "Aphrodite","Hephaestus","Hermes","Dionysus"
        ]
    }

@app.route("/chaos")
def chaos():
    return {
        "entity": "CHAOS",
        "state": "Primordial Origin"
    }


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
