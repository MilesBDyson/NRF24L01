from NRF24L01.nrf24 import NRF24
import time

pipes = [[0x4e, 0x15, 0x2F, 0x63, 0x91], [0x30, 0x55, 0x3E, 0x10, 0x58]]
radio = NRF24()
radio.begin(1, 0, "P9_23", "P9_24")
radio.setPayloadSize(32)
radio.setChannel(0x71)
#radio.setDataRate(NRF24.BR_250KBPS)
radio.setDataRate(NRF24.BR_1MBPS)
#radio.setDataRate(NRF24.BR_2MBPS)
radio.setPALevel(NRF24.PA_MAX)
radio.setAutoAck(1)
radio.enableDynamicPayloads()
radio.enableAckPayload()

def sendData(message):
	radio.startListening()
	radio.stopListening()
	time.sleep(0.25)
	radio.write(message)
	radio.startListening()

def receiveData():
	radio.startListening()
	while not radio.available(pipes, True):
		time.sleep(1/100)
	receivedMessage = []
	radio.read(receivedMessage,radio.getDynamicPayloadSize())
	message = ""
	for n in receivedMessage:
		if (n >= 32 and n <= 126):
			message += chr(n)
	print("Message: {}".format(message))
	radio.stopListening()