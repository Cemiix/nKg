from pyrogram import Client
from flask import Flask

web = Flask(__name__)
@web.route("/")
def home():
	return "Hello world"

app = Client("app")

with app:
	web.run("0.0.0.0")
app.run()
