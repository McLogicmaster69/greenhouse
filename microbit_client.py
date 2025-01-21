from microbit import *
from microbit_serial import *
from microbit_report import *
from OLED import *
from bme688 import *

class Client:

    def __init__(self):
        self.report = Report()
        init_sensor()
        init_gas_sensor()
        init_display()

    def main_loop(self):
        while True:
            read_data_registers()
            self.report.report_information("5", str(calc_temperature()), "90")
            sleep(500)