from socket import *

server_ip = "172.21.115.230"
 
s = socket(AF_INET , SOCK_DGRAM)
s.bind((server_ip , 9999))
data , addr = s.recvfrom(1024)
print(data.decode('ascii'))
b = "Soon you will be connected  , be thankful to Mr. Kadyan"
s.sendto(b.encode('ascii'),addr)
