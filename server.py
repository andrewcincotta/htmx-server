# server.py
from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def index():
    return open("index.html").read()

@app.route("/clicked", methods=["POST"])
def clicked():
    return "<p>Thanks for clicking!</p>"

if __name__ == "__main__":
    app.run(debug=True)
