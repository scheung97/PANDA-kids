from gevent import monkey

monkey.patch_all()

import json
import os

from flask import Flask, render_template
from flask_socketio import SocketIO
from redislite import Redis
from logic.redis_listener import RedisListener
from constants import *

listener_thread = None

app = Flask(__name__)
app.config['SECRET_KEY'] = 'MYSECRETCODE'
socketio = SocketIO(app)
r = Redis(REDIS_DB_FILE)

def handle_ui_change(self, event):
    print(event)
    if event['data']:
        print('Received socket data:')
        print(event['data'])
        socketio.emit('ui', {'data': event['data'].decode('utf-8')}, namespace='/ui')

@app.route('/')
def selection():
    print("Entered selection")
    global listener_thread
    if listener_thread == None:
        listener_thread = RedisListener('UI Listener', r, [UI_CHANNEL], handle_ui_change)
        listener_thread.start()
        print("Started listener thread")
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

@socketio.on('connect')
def client_connected():
    print('Client has connected')

if __name__ == '__main__':
    socketio.run(app)