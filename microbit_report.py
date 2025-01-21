from microbit import *
import radio

class Report:

    def __init__(self):
        radio.config(channel = 20, group = 15)
        radio.on()

    def report_information(self, co2, temp, light):
        radio.send(co2 + "|" + temp + "|" + light)

    def recieve_information(self):
        incoming = radio.receive()
        if incoming:
            return incoming.split("|")
        return None