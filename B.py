from flask import Flask
from threading import Thread

app = Flask('Discord Bot')

@app.route('/')
def main():
    return 'SERVER ONLINE'

def run():
    app.run(host='0.0.0.0', port=8080)

def b():
    server = Thread(target=run)
    server.start()