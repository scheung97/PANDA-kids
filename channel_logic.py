from redislite import Redis
from threading import Thread

# globals
states = {
    'emotion': '',
    'speech': '',
    'ui': '',
    'tts': '',
    'leds': ''
}
channels = list(states.keys())

# classes
class RedisListener(Thread):
    def __init__(self, r, channels, handle_event_method):
        Thread.__init__(self)

        # Thread is killed on process end
        self.daemon = True

        # Store redis info in thread
        self.redis = r
        self.pubsub = self.redis.pubsub()

        # Subscribe to selected channels
        self.pubsub.psubscribe(channels)

        # Store flask app info in thread
        # self.app = flask_app

        self.handle_event = handle_event_method

    def run(self):
        for event in self.pubsub.listen():
            self.handle_event(event)

# Channel Data Handlers
def emotion_data_handler(r, data):
    emotion = data['smth']
    if states['emotion'] != emotion:
        r.publish('ui', emotion)
        r.publish('leds', emotion)

def speech_data_handler(r, data):
    data

def ui_data_handler(r, data):
    data

def tts_data_handler(r, data):
    data

def leds_data_handler(r, data):
    data

handlers = {
    'emotions': emotion_data_handler,
    'speech': speech_data_handler,
    'ui': ui_data_handler,
    'tts': tts_data_handler,
    'leds': leds_data_handler
}

# Main Listener Event Handler
def main_event_handler(self, event):
    handlers[event['channel']](self.redis, event['data'])

if __name__ == '__main__':
    listener = RedisListener(Redis(), [channels], main_event_handler)

    # emotions & speech to text need pubsub objects
    # ui & text to speech & leds need to subscribe & publish
    # each subscription gets their own thread to be async
    # publish when we want to change the state
