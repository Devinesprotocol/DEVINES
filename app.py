from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def devines_core():
    return jsonify({
        "system": "Devines Protocol",
        "core": "CHAOS",
        "status": "Awakening",
        "message": "Primordial intelligence initializing"
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "alive",
        "core": "CHAOS",
        "protocol": "Devines"
    })

@app.route("/pantheon")
def pantheon():
    return jsonify({
        "pantheon": "Greek",
        "gods": [
            "Zeus",
            "Hera",
            "Poseidon",
            "Demeter",
            "Athena",
            "Apollo",
            "Artemis",
            "Ares",
            "Aphrodite",
            "Hephaestus",
            "Hermes",
            "Dionysus"
        ]
    })

@app.route("/guardian/memory")
def memory_guardian():
    return jsonify({
        "guardian": "Memory",
        "function": "Persistent knowledge storage",
        "status": "Watching the past"
    })

@app.route("/chaos")
def chaos():
    return jsonify({
        "entity": "CHAOS",
        "nature": "Primordial Origin",
        "state": "Dormant Consciousness"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
