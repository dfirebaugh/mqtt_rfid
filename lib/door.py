import machine
import utime

class DoorControl:
    def __init__(self, event, config, relay):
        self.event = event
        self.config = config
        self.relay = relay
        self.relay.deactivate()

    def on_grant(self, uid):
        self.event.publish_access_granted(uid)
        print('granted', uid)
        self.relay.activate()
        utime.sleep(self.config.get('RELAY_DURATION'))
        self.relay.deactivate()

    def on_deny(self, uid):
        self.event.publish_access_denied(uid)
        print('denied', uid)
