import hashlib
import json
import os

class AccessControlList:
    def __init__(self, file_path):
        self.file_path = file_path
        self.users = self.load()

    def load(self):
        try:
            with open(self.file_path, 'r') as file:
                data = file.read()
                if data:
                    return json.loads(data)
        except OSError as e:
            if e.args[0] == 2:  # errno.ENOENT, file not found
                self.save([])

        return []

    def save(self):
        with open(self.file_path, 'w') as file:
            file.write(json.dumps(self.users))
        self.users = self.load()

    def add(self, user):
        user_decoded = user.decode('utf8')
        if user_decoded not in self.users:
            self.users.append(user_decoded)
        self.save()

    def add_many(self, users):
        for user in users:
            self.add(user)

    def remove(self, user):
        user_decoded = user.decode('utf8')
        if user_decoded in self.users:
            self.users.remove(user_decoded)
        self.save()

    def clear(self):
        self.users = []
        self.save()

    def compare(self, other):
        current_users = set(self.users)
        other_users = set(other)

        return current_users == other_users

    def get_hash(self):
        sorted_users = sorted(self.users)
        hash_string = ''.join(sorted_users).encode('utf-8')
        hash_object = hashlib.sha256(hash_string)
        hash_value = ''.join('{:02x}'.format(x) for x in hash_object.digest())

        return hash_value

    def has_user(self, user):
        return user in self.users