from microbit import *
from microbit_serial import *
from microbit_report import *

class Server:

    def __init__(self):
        self.report = Report()
        self.serial = SerialPort()

    def main_loop(self):
        while True:
            incoming = self.report.recieve_information()
            if incoming:
                self.serial.serialize("CO2: " + incoming[0] + " | Temperature: " + incoming[1] + " | Light: " + incoming[2] + "\n")