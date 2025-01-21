from microbit import *
import radio

def init_information():
    radio.config(channel = 20, group = 15)

def report_information(co2, temp, light):
    radio.send(f"{co2}|{temp}|{light}")

def recieve_information():
    incoming = radio.receive()
    if incoming:
        return incoming.split("|")