import json

class AccessControlSystem:
    def __init__(self, config, acl, reader, door_control):
        self.config = config
        self.acl = acl
        self.reader = reader
        self.door_control = door_control
        self.PreviousCard = [0]
    def handle_rfid_swipe(self, uid):
        uid_hex = ''.join(['{:02X}'.format(byte) for byte in uid])
        payload = json.dumps({'uid': uid_hex})

        if self.acl.has_user(uid_hex):
            self.door_control.on_grant(uid_hex)
            return

        self.door_control.on_deny(uid_hex)

    def run(self):
        self.reader.init()
        (stat, tag_type) = self.reader.request(self.reader.REQIDL)
        if stat == self.reader.OK:
            (stat, uid) = self.reader.SelectTagSN()

            if uid == self.PreviousCard:
                return

            if stat == self.reader.OK:
                self.handle_rfid_swipe(uid)
                self.PreviousCard = uid
        else:
            self.PreviousCard = [0]
