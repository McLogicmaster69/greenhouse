import serial
import time
from plotting import *
import datetime

# User inputs which port 
print("Type port")
port_name = input(">>> ")
port = serial.Serial(port_name, 115200)

plotter = Plotter()

def add_data(data) -> None:
    """
    Parse data and add it to the graphs
    """
    info = data.split("|")
    plotter.add_data(info[0], int(info[1]), datetime.datetime.now(), int(info[2]))

while True:
    if port.in_waiting > 0: # If data is in port, read it and add it to the graph
        message = port.readline().decode().strip()
        if message != "":
            add_data(message)
    plotter.GUI_update()