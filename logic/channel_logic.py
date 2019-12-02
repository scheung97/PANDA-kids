from redislite import Redis
from threading import Thread
from redis_listener import RedisListener
import TTS.tts as tts
from constants import *
import time

# globals
states = {
    'emotion': '',
    'speech': '',
    'ui': '',
    'tts': '',
    'leds': ''
}

# Channel Data Handlers
def emotion_data_handler(r, data):
    emotion = data
    if states['emotion'] != emotion:
        r.publish('ui', emotion)
        r.publish('leds', emotion)

def speech_data_handler(r, data):
    data

def ui_data_handler(r, data):
    pass
    #print("UI data handler received: {}".format(data), flush=True)

def tts_data_handler(r, data):
    if not isinstance(data, int):
        print("TTS call for: {}".format(data.decode('utf-8')))
        tts.Speech(data.decode("utf-8"))

def leds_data_handler(r, data):
    data

handlers = {
    EMOTION_CHANNEL: emotion_data_handler,
    SPEECH_CHANNEL: speech_data_handler,
    UI_CHANNEL: ui_data_handler,
    TTS_CHANNEL: tts_data_handler,
    LEDS_CHANNEL: leds_data_handler
}
channels = list(handlers.keys())

# Main Listener Event Handler
def main_event_handler(self, event):
    #print("Logic main event handler called")
    handlers[event['channel']](self.redis, event['data'])

if __name__ == '__main__':
    print("Channel logic started")
    redis_object = Redis(REDIS_DB_FILE)
    listener = RedisListener('Logic Listener', redis_object, channels, main_event_handler)
    listener.start()
    while True:
        pass

    # emotions & speech to text need pubsub objects
    # ui & text to speech & leds need to subscribe & publish
    # each subscription gets their own thread to be async
    # publish when we want to change the state
