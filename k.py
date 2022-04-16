from flask import Flask
import os
import time
l= Flask(__name__)
dir = [f.name for f in os.scandir(".")]
b = [os.path.getsize(f) for f in [dir[f] for f in range(len(dir))]]
z = ";".join([x + " " + y for x,y in zip(dir,b)])
@l.route("/")
def index():
    return z
