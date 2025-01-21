import serial

port = serial.Serial('COM3', 115200)

print("Started")

while True:
    message = port.readline().decode().strip()
    print(message)