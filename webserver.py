from flask import Flask, render_template, redirect
from threading import Thread

app = Flask('')

@app.route('/')
def index():
	return 'Bot is online!'

def run():
	app.run(host="0.0.0.0", port=8080)

def webserver():
	server = Thread(target=run)
	server.start()

webserver()