#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Example program to receive packets from the radio
#
# João Paulo Barraca <jpbarraca@gmail.com>
#

from NRF24L01.nrf24 import NRF24
import time


def makechar(data):
    text = ''.join(chr(i) for i in data)
    return text

def makeunicode(data):
    uncode = []
    i = 0
    for char in data:
        uncode.insert(i, ord(char))
        i += 1
    return uncode
    
pipes = [[0xe7, 0xe7, 0xe7, 0xe7, 0xe7], [0xc2, 0xc2, 0xc2, 0xc2, 0xc2]]

radio = NRF24()
radio.begin(1, 0, "P9_23", "P9_24")

radio.setRetries(15,15)

radio.setPayloadSize(8)
radio.setChannel(0x60)

radio.setDataRate(NRF24.BR_250KBPS)
radio.setPALevel(NRF24.PA_MAX)
radio.setAutoAck(1)

radio.openReadingPipe(1, pipes[1])

radio.startListening()
radio.stopListening()

radio.printDetails()

radio.startListening()

while True:
    pipe = [0]
    while not radio.available(pipe, True):
        time.sleep(1000/1000000.0)

    recv_buffer = []
    radio.read(recv_buffer)

    print (recv_buffer)
