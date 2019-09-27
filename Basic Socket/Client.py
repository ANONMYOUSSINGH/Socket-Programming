import os
from socket import *
host = ""
port = 13000
buf = 1024
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
UDPSock.bind(addr)
print ("Waiting to receive messages...")
while True:
    (data, addr) = UDPSock.recvfrom(buf)
    print ("Received message: "+data)
    if data == "exit":
        break
    """ if data == 2:
        ip=input("Enter the ip address of the reciever")
        addr = (ip, port)
        UDPSock = socket(AF_INET, SOCK_DGRAM)
        UDPSock.bind(addr)
        data = raw_input("Enter message to send or type 'exit': ")
        UDPSock.sendto(data, addr)
        if data == "exit":
            break """
UDPSock.close()
os._exit(0)



