import os
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome on super safe app ;)"

@app.route("/ping")
def ping():
    ip = request.args.get("ip", "127.0.0.1")

    # Faille
    os.system("ping" + ip)
    return "Ping terminé"

if __name__ == "__name__":
    app.run()

