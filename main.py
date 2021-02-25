from flask import Flask

web = Flask(__name__)

@web.route("/")
def index():
	return "hello"

web.run("0.0.0.0")