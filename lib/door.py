
class DoorControl:
    def __init__(self, event):
        self.event = event
    def on_grant(self, uid):
        self.event.publish_access_granted(uid)
        print('granted', uid)
        # TODO: activate relay
    def on_deny(self, uid):
        self.event.publish_access_denied(uid)
        print('denied', uid)
