import json

from flask import Flask, render_template
from flask_socketio import send, SocketIO
from redislite import Redis
from channel_logic import RedisListener

app = Flask(__name__)
app.config['SECRET_KEY'] = 'MYSECRETCODE'
socketio = SocketIO(app)

@app.route('/')
def selection():
    # set up selection to go to hospital, home, or education
    return render_template('base.html', title='selection')

@app.route('/<page_type>/')
def pages(page_type='hospital'):
    # page_type = hospital, home, or education
    return render_template('base.html', title=page_type)

@app.route('/facial_recognition/')
def facial_recognition_ui():
    return render_template('base.html', title='What\'s your emotion?')

@app.route('/settings/')
def settings():
    return 'SETTINGS'

def handle_ui_change(self, event):
    if event['data']:
        with app.app_context():
            send(json.dumps({'data': 'data'}), room='ui', namespace='/')

if __name__ == '__main__':
    r = Redis()
    client = RedisListener(r, ['ui'], handle_ui_change)
    client.start()

    socketio.run(app)
