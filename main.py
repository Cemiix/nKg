from pyrogram import Client
from flask import Flask

web = Flask(__name__)
@web.route("/")
def home():
	return "Hello world"

app = Client("app")

app.run()
