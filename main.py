# from flask import Flask

# web = Flask(__name__)

# @web.route("/")
# def index():
# 	return "hello"

# web.run("0.0.0.0")

import os

print(os.system("npm install -g heroku"))
print(os.system("heroku --version"))