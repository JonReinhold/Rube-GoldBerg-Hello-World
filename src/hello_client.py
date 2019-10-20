import socket

ip = socket.gethostbyname('localhost.localdomain') 
port = 10000
buffer_size = 1024

with open("payload.c", "r") as file:
    message_list = file.read()

message =  str.encode(message_list)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, port))
s.send(message)
data = s.recv(buffer_size)
s.close()

data = str(data)
print(data[2:-1])
