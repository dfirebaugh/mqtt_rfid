import machine

class Relay:
    def __init__(self, config):
        self.config = config
        self.led_pin = machine.Pin('LED', machine.Pin.OUT)
        self.relay_pin = machine.Pin(self.config.get('RELAY_PIN'), machine.Pin.OUT)
    def activate(self):
        self.relay_pin.on()
        self.led_pin.on()
    def deactivate(self):
        self.relay_pin.off()
        self.led_pin.off()
