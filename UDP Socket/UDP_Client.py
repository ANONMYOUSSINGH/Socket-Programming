from socket import *
host = ('172.21.115.230',9999)
s = socket(AF_INET , SOCK_DGRAM)
a = "You are connected"
s.sendto(a.encode('ascii'),host)

data,server = s.recvfrom(1024)
print(data.decode('ascii'))

