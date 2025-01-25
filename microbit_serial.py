from microbit import *

class SerialPort:
    """
    Used to send and recieve data over USB ports
    """
    def __init__(self) -> None:
        """
        Initialises the library to send data of the port
        """
        uart.init(baudrate=115200)

    def serialize(self, message : str) -> None:
        """
        Sends data over the port
        """
        uart.write(message)