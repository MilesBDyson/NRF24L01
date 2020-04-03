from NRF24L01.nrf24 import NRF24
import time
from radio_config import *

radio.openReadingPipe(1, pipes[0])
radio.openWritingPipe(pipes[1])
#radio.printDetails()

message = "dikzmgkgtyyiureybshxcbudtmdmhmxp"
sendData(message)

receiveData()


