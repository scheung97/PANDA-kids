from flask import Flask, render_template
from flask_socketio import SocketIO
from redislite import Redis
from threading import Thread

app = Flask(__name__)
app.config['SECRET_KEY'] = 'MYSECRETCODE'
socketio = SocketIO(app)


class RedisListener(Thread):
    def __init__(self, r, channels, flask_app):
        Thread.__init__(self)

        # Thread is killed on process end
        self.daemon = True

        # Store redis info in thread
        self.redis = r
        self.pubsub = self.redis.pubsub()

        # Subscribe to selected channels
        self.pubsub.psubscribe(channels)

        # Store flask app info in thread
        self.app = flask_app

    def handle_event(event):
        # Handle the events here!
        # figures out what event is what
        pass

    def run(self):
        for event in self.pubsub.listen():
            self.handle_event(event)

@app.route('/')
def selection():
    # set up selection to go to hospital, home, or education
    return render_template('base.html', title='selection')


@app.route('/<page_type>/')
def pages(page_type='hospital'):
    # page_type = hospital, home, or education
    return render_template('base.html', title=page_type)


@app.route('/settings/')
def settings():
    return 'SETTINGS'


if __name__ == '__main__':
    r = redis.Redis()
    client = Listener(r, ['channels'], app)
    client.start()

    socketio.run(app)
