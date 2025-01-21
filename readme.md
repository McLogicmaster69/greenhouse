Code to send data from one microbit to another, and then for that microbit to report it to the computer that it is connected to

# Client

For the sensor microbits that will be sending the data, the following code is required in their main.py

'''
from microbit import *
from microbit_client import *

client = Client()
client.main_loop()
'''

Within the microbit_client, in the commeneted while loop, you can add code there to be able to send sensor information

# Server

For the microbit that acts as the central server, the following code is required in their main.py

'''
from microbit import *
from microbit_server import *

server = Server()
server.main_loop()
'''

# Computer

Run pc_main.py and that will recieve and display the data from the microbit