from lib.access_control import AccessControlSystem
from lib.rfid_readers.mfrc522 import MFRC522
from lib.acl import AccessControlList
from lib.config import ConfigManager
from lib.door import DoorControl
from lib.event import EventManager
from lib.mqtt import MQTTWrapper
from lib.wifi import NetManager

import utime

reader = MFRC522(spi_id=0, sck=2, miso=4, mosi=3, cs=1, rst=0)
config = ConfigManager('cnf')

mqtt = MQTTWrapper(server=config.get("MQTT_BROKER"), user=config.get("MQTT_USER"), password=config.get("MQTT_PASSWORD"), client_id=config.get("MQTT_CLIENT_ID"))
acl = AccessControlList('acl')
event = EventManager(config, acl, mqtt)
door = AccessControlSystem(config, acl, reader, DoorControl(event))

wifi = NetManager(event, config.get("WIFI_SSID"), config.get("WIFI_PASSWORD"))

try:
    wifi.connect_wifi()
    event.publish_heartbeat()
    while True:
        wifi.check_connection()
        door.run()
        event.run()
        utime.sleep_ms(config.get("MAIN_SLEEP_INTERVAL"))

except KeyboardInterrupt:
    print("Bye")
    mqtt.disconnect()
