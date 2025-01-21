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
            ### IMPLEMENT SENSOR CODE HERE
            read_data_registers()
            self.report.report_information("REPLACE WITH CO2", "REPLACE WITH TEMP", "REPLACE WITH LIGHT")
            sleep(500)