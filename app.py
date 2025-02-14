from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World! subdomain takeover by Vikas_upadhyay0"
