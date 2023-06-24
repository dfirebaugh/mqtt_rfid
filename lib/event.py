import json
import utime

class EventManager:
    def __init__(self, config, acl, mqtt):
        self.config = config
        self.acl = acl
        self.mqtt = mqtt
        self.topic_prefix = self.config.get("MQTT_TOPIC_PREFIX")
        self.connect()

    def connect(self):
        self.mqtt.connect()
        self.mqtt.client.set_callback(self.on_message)
        self.set_subscriptions()
        self.publish_acl_hash()
        self.last_heartbeat = None

    def set_subscriptions(self):
        self.mqtt.subscribe(self.config.get("MQTT_TOPIC_PREFIX")+"/acl")
        self.mqtt.subscribe(self.config.get("MQTT_TOPIC_PREFIX")+"/adduser")
        self.mqtt.subscribe(self.config.get("MQTT_TOPIC_PREFIX")+"/removeuser")
        self.mqtt.subscribe(self.config.get("MQTT_TOPIC_PREFIX")+"/open")

        if self.config.get("DEBUG_ENABLED"):
            self.mqtt.subscribe(self.config.get("MQTT_TOPIC_PREFIX")+"/heartbeat")
            self.mqtt.subscribe(self.config.get("MQTT_TOPIC_PREFIX")+"/access_granted")
            self.mqtt.subscribe(self.config.get("MQTT_TOPIC_PREFIX")+"/access_denied")

    def on_message(self, topic, msg):
        print(topic, msg)
        if topic.decode('utf-8') == self.topic_prefix+'/adduser':
            self.acl.add(msg)
        if topic.decode('utf-8') == self.topic_prefix+'/removeuser':
            self.acl.remove(msg)
        if topic.decode('utf-8') == self.topic_prefix+'/open':
            self.door_control.on_grant('remote')
        if topic.decode('utf-8') == self.topic_prefix+'/acl':
            self.publish_acl_hash()

    def publish_acl_hash(self):
        self.mqtt.publish(self.topic_prefix+"/acl_response", json.dumps({'hash': self.acl.get_hash()}))
    def publish_heartbeat(self):
        self.mqtt.publish(self.topic_prefix+"/heartbeat", "OK")
    def publish_access_granted(self, uid):
        self.mqtt.publish(self.topic_prefix+"/access_granted", uid)
    def publish_access_denied(self, uid):
        self.mqtt.publish(self.topic_prefix+"/access_denied", uid)
    def heartbeat(self):
        if self.config.get("MQTT_HEARTBEAT_INTERVAL") == '':
            return
        if self.last_heartbeat is None:
            self.last_heartbeat = utime.time()
        if utime.time() - self.last_heartbeat > self.config.get("MQTT_HEARTBEAT_INTERVAL"):
            self.publish_heartbeat()
            self.last_heartbeat = utime.time()
    def run(self):
        try:
            self.heartbeat()
            self.mqtt.check_msg()
        except Exception as e:
            print("Failed to check messages:", e)
            self.connect()
