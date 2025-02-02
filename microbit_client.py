from microbit import *
from microbit_report import *
from bme688 import *
import music
import random

class Client:
    """
    Microbit that acts as a sensor and sends data to the server
    """
    def __init__(self) -> None:
        """
        Initialises the client by intialising the sensors
        """
        self.report = Report()
        self.id = random.randint(0, 99999)
        init_sensor()
        init_gas_sensor()

    def main_loop(self) -> None:
        """
        The main loop of the client that reports the information of the sensors to the server
        """
        while True:
            read_data_registers()

            # Send temperature data to server and sound alarm if temperature is too low
            temp = round(calc_temperature())
            self.report.report_information(self.id, 0, temp)
            if temp < 20:
                self.alarm()
            sleep(500)

            # Send humidity data to server
            humidity = calc_humidity()
            self.report.report_information(self.id, 1, humidity)
            sleep(500)

            # Send pressure data to server
            pressure = calc_pressure()
            self.report.report_information(self.id, 2, pressure)
            sleep(500)

            # Send light data to server
            light = display.read_light_level()
            self.report.report_information(self.id, 3, light)
            sleep(500)

            # Send IAQ score data to server
            iaqScore, iaqPercent, eCO2Value = calc_air_quality()
            self.report.report_information(self.id, 4, iaqScore)
            sleep(500)

            # Send CO2 data to server
            iaqScore, iaqPercent, eCO2Value = calc_air_quality()
            self.report.report_information(self.id, 5, eCO2Value)
            sleep(500)
    
    def alarm(self) -> None:
        """
        Plays a note to act as an alarm
        """
        music.play(["C5:1", "R:1"])