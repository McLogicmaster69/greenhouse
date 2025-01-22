import serial
from plotting import *

port = serial.Serial('COM4', 115200)
plotter = Plotter()

while True:
    message = port.readline().decode().strip()
    print(message)