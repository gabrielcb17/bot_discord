from flask import Flask
from flask import render_template
from threading import Thread

app = Flask('Discord Bot')

@app.route('/')
def main():
    return 'SERVER ONLINE'

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

def run():
    app.run(host='0.0.0.0', port=8080)

def b():
    server = Thread(target=run)
    server.start()

if __name__ == '__main__':
    b()