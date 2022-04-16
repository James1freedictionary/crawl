from flask import Flask

l= Flask(__name__)

@l.route("/")
def index():
    return "hhhHello World!"
