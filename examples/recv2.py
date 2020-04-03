from NRF24L01.nrf24 import NRF24
import time
from radio_config import *

radio.openWritingPipe(pipes[0])
radio.openReadingPipe(1, pipes[1])
#radio.printDetails()

receiveData()
#time.sleep(1)
message = "received"
sendData(message)

    

    


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
