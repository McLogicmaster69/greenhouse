from microbit import *
from microbit_serial import *
from microbit_report import *

class Server:
    """
    Microbit that acts as a server to recieve data from clients
    """
    def __init__(self) -> None:
        """
        Initialises the server and USB port
        """
        self.report = Report()
        self.serial = SerialPort()

    def main_loop(self) -> None:
        """
        The main loop of the server that recieves data and sends it over the USB port
        """
        while True:
            incoming = self.report.recieve_information()
            if incoming:
                self.serial.serialize(incoming + "\n")