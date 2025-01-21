from microbit import *

class SerialPort:

    def __init__(self):
        uart.init(baudrate=115200)

    def serialize(self, message):
        uart.write(message)