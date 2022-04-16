from flask import Flask
import os

l= Flask(__name__)
dir = os.scandir("./")
@l.route("/")
def index():
    return r
