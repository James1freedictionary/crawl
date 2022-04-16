from flask import Flask
import os
import time
l= Flask(__name__)
dir = os.scandir("./")
@l.route("/")
def index():
    return dir
