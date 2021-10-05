import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("192.168.1.110", 1234))

while True:
    client.send(input().encode("utf-8"))