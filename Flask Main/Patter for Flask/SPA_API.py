from flask import Flask, jsonify


app = Flask(__name__, static_folder='app', static_url_path="/app")


@app.route("/heartbeat")
def heartbeat():
    return jsonify({"status": "healthy"})


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return app.send_static_file("index.html")