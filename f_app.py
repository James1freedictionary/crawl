from flask import Flask
import os
import time
import subprocess
print("hi")
app = Flask(__name__)
dir = [f.name for f in os.scandir(".")]
b = [os.path.getsize(f) for f in [dir[f] for f in range(len(dir))]]
z = ";".join([x + " " + str(y) for x,y in zip(dir,b)])
@app.route("/")
def index():
    #subprocess.run(["python", "crawl.py"], shell=True)
    return z
