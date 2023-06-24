from lib.config import ConfigManager

config = ConfigManager('cnf')
config.load_config()
config.save_config(config={
    "MAIN_SLEEP_INTERVAL": 50,
    "MQTT_HEARTBEAT_INTERVAL": 1*60, # every minute
    "MQTT_BROKER": "",
    "MQTT_PORT": 1883,
    "MQTT_USER": "",
    "MQTT_PASSWORD": "",
    "MQTT_RECONNECT_INTERVAL": 60000,
    "MQTT_TOPIC_PREFIX": "frontdoor",
    "MQTT_CLIENT_ID": "door_testing_random_mqtt_client_1029381029487124",
    "WIFI_SSID": "",
    "WIFI_PASSWORD": ""
})
