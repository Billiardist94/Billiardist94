from socket import socket, getaddrinfo, SHUT_WR
from shared import send_data, recv_data


family, type, proto, name, addr = getaddrinfo('127.0.0.1', 1234)[0]
s = socket(family, type, proto)
s.bind(addr)
s.listen(1)
client, addr = s.accept()

while True:
    grid = recv_data(client)
    if grid is None:
        break

client.shutdown(SHUT_WR)
client.close()
