from microbit import *
import radio

class Report:

    def __init__(self):
        radio.config(channel = 20, group = 15)
        radio.on()

    def report_information(self, index, value):
        radio.send(format(index, value))

    def format_information(self, index, value):
        return machine.unique_id() + "|" + str(index) + "|" + str(value)

    def recieve_information(self):
        incoming = radio.receive()
        if incoming:
            return incoming
        return None