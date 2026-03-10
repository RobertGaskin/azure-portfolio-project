from flask import Flask, render_template
import socket
import os

app = Flask(__name__)

@app.route("/")
def home():
    hostname = socket.gethostname()
    return render_template(
        "index.html",
        hostname=hostname,
        environment=os.environ.get("APP_ENV", "Production")
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)