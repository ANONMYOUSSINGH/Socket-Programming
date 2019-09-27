import os
from socket import *
host = "172.22.52.183"
port = 13000
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
while True:
    data = raw_input("Enter message to send or type 'exit': ")
    UDPSock.sendto(data, addr)
    if data == "exit":
        break
    if data == 2:
        host = ""
        addr = (host, port)
        UDPSock = socket(AF_INET, SOCK_DGRAM)
        UDPSock.bind(addr)
        print ("Waiting to receive messages...")
        while True:
            (data, addr) = UDPSock.recvfrom(buf)
            print ("Received message: "+data)
            if data == "exit":
                break
UDPSock.close()
os._exit(0)