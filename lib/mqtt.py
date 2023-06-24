from umqtt.simple import MQTTClient
import time

class MQTTWrapper:
    def __init__(self, server, user, password, client_id):
        self.client_id = client_id
        self.server = server
        self.user = user
        self.password = password

    def connect(self):
        try:
            self.client = MQTTClient(self.client_id, self.server, user=self.user, password=self.password)
            self.client.connect()
        except Exception as e:
            print("Failed to connect to MQTT server:", e)
            time.sleep(5)  # Wait for 5 seconds before attempting reconnection

    def disconnect(self):
        try:
            self.client.disconnect()
        except Exception as e:
            print("Failed to disconnect from MQTT server:", e)

    def publish(self, topic, msg):
        try:
            self.client.publish(topic, msg)
        except Exception as e:
            print("Failed to publish message:", e)

    def subscribe(self, topic):
        try:
            self.client.subscribe(topic)
        except Exception as e:
            print("Failed to subscribe to topic:", e)

    def check_msg(self):
        self.client.check_msg()
