from flask import Flask

a = Flask(__name__)

@a.route("/")
def index():
    return "Hello World!"
