import network
import machine
import time

class NetManager:
    def __init__(self, event, ssid, password):
        self.event = event
        self.ssid = ssid
        self.password = password
        self.connected = False
        self.reconnect_timer = machine.Timer(-1)
        self.reconnect_interval = 10  # seconds

    def connect_wifi(self):
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        wlan.connect(self.ssid, self.password)
        self.reconnect_timer.init(period=self.reconnect_interval * 1000, mode=machine.Timer.PERIODIC, callback=self._reconnect_callback)

    def _reconnect_callback(self, timer):
        wlan = network.WLAN(network.STA_IF)
        if wlan.isconnected():
            self.connected = True
            timer.deinit()
            self.event.connect()

    def check_connection(self):
        return self.connected
