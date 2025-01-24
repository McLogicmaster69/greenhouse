from microbit import *
from microbit_report import *
from bme688 import *
import music

class Client:

    def __init__(self):
        self.report = Report()
        init_sensor()
        init_gas_sensor()

    def main_loop(self):

        while True:

            read_data_registers()
            temp = round(calc_temperature())
            humidity = calc_humidity()
            pressure = calc_pressure()
            light = display.read_light_level()
            iaqScore, iaqPercent, eCO2Value = calc_air_quality()
            self.report.report_information(self.format_data([str(temp), str(humidity), str(light), str(iaqScore), str(iaqPercent), str(eCO2Value)]))

            if temp < 20:
                music.play(["C5:1", "R:1"])

            sleep(1000)

    def format_data(self, data):
        if len(data) == 0:
            return ""
        
        output = ""
        for d in data:
            output += str(d)
            output += "|"

        return output[0:-1]