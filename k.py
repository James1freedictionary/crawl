from flask import Flask
import os
import time
l= Flask(__name__)
dir = [f for f in os.scandir(".")]
@l.route("/")
def index():
    return dir
