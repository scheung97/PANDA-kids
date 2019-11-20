from threading import Thread

class RedisListener(Thread):
    def __init__(self, name, r, channels, handle_event_method):
        Thread.__init__(self)

        # Stored name for identifying the listener
        self.name = name

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
        print("Listener thread started: {}".format(self.name))
        for event in self.pubsub.listen():
            if event['type'] == 'pmessage':
                self.handle_event(self, event)
