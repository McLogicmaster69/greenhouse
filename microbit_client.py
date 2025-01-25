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
            self.report.report_information(0, temp)
            if temp < 20:
                self.alarm()
            sleep(100)

            humidity = calc_humidity()
            self.report.report_information(1, humidity)
            sleep(100)

            pressure = calc_pressure()
            self.report.report_information(2, pressure)
            sleep(100)

            light = display.read_light_level()
            self.report.report_information(3, light)
            sleep(100)

            iaqScore, iaqPercent, eCO2Value = calc_air_quality()
            self.report.report_information(4, iaqScore)
            sleep(100)

            iaqScore, iaqPercent, eCO2Value = calc_air_quality()
            self.report.report_information(5, eCO2Value)
            sleep(100)

    def format_data(self, data):
        if len(data) == 0:
            return ""
        
        output = ""
        for d in data:
            output += str(d)
            output += "|"

        return output[0:-1]
    
    def alarm(self):
        music.play(["C5:1", "R:1"])