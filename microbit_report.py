from microbit import *
import radio

class Report:

    def __init__(self):
        radio.config(channel = 20, group = 15)
        radio.on()

    def report_information(self, information):
        radio.send(information)

    def recieve_information(self):
        incoming = radio.receive()
        if incoming:
            return incoming
        return None