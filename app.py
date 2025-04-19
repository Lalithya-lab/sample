import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("sample.html")

if __name__ == "__main__":
    host = os.environ.get("FLASK_RUN_HOST", "0.0.0.0")
    port = int(os.environ.get("FLASK_RUN_PORT", 5000))
    app.run(host=host, port=port, debug=True)
