from microbit import *
import radio
import machine

class Report:
    """
    Used to report data between microbits
    """
    def __init__(self) -> None:
        """
        Initialises the radio to be on channel 20 and group 15
        """
        radio.config(channel = 20, group = 15)
        radio.on()

    def report_information(self, id : int, index : int, value) -> None:
        """
        Sends information to the server
        """
        radio.send(self.format_information(id, index, value))

    def format_information(self, id : int, index : int, value) -> str:
        """
        Formats the information from the client to be sent to the server
        """
        return str(id) + "|" + str(index) + "|" + str(value)

    def recieve_information(self):
        """
        Checks if any information has been recieved from the client
        """
        return radio.receive()