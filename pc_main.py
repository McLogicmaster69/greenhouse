import serial
import time
from plotting import *
import datetime

port = serial.Serial('COM4', 115200)
plotter = Plotter()

def add_data(data):
    info = data.split("|")
    plotter.add_data([datetime.datetime.now(), info[0], info[1], info[2], info[3], info[4], info[5]])

while True:
    if port.in_waiting > 0:
        message = port.readline().decode().strip()
        add_data(message)

    plotter.GUI_update()