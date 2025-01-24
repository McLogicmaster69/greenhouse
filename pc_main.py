import serial
import time
from plotting import *
import datetime

print("Type port")
port = input(">>>")

port = serial.Serial(port, 115200)
plotter = Plotter()

def add_data(data):
    info = data.split("|")
    plotter.add_data([datetime.datetime.now(), int(info[0]), int(info[1]), int(info[2]), int(info[3]), int(info[4]), int(info[5])])

while True:
    if port.in_waiting > 0:
        message = port.readline().decode().strip()
        add_data(message)

    plotter.GUI_update()