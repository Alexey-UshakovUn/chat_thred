import socket
import config
from typing import NamedTuple


class AddrClient(NamedTuple):
    host: str
    port: int


clients = {}

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((config.HOST, config.PORT))
server_socket.listen()
print('[ Server started ]')

def server_accept_connection(server_socket):
    client_socket, addr = server_socket.accept()
    if addr not in clients:
        tmp = {addr: client_socket.recv(1024)}
        clients.update(tmp)
    print(clients)
    print('Connection from', addr)
    print(type(addr))
    print(type(addr[0]))
    response = 'Hello, {}'.format(clients[addr])
    client_socket.send(response.encode())
    return client_socket, addr

def server_register_new_client(addr: AddrClient) -> None:
    pass

def server_greetings_new_client(addr: AddrClient) -> str:
    pass

while True:
    client_socket, addr = server_accept_connection(server_socket)  # Принимаем подключение клиента

    while True:
        print('we wait recv')
        request = client_socket.recv(1024)  # Получаем сообщение от клиента
        print(request.decode())

        if not request:
            break
        else:
            response = ('Hello, your addr :' + addr[0] + '\n').encode()
            print(response)
            client_socket.send(response)



