import socket
import config
from typing import NamedTuple
import threading
from select import select


class AddrClient(NamedTuple):
    host: str
    port: int


clients = {}


def server_setting():
    """Config and Run server"""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((config.HOST, config.PORT))
    server_socket.listen()
    print('[ Server started ]')
    return server_socket


def server_accept_connection(server_socket):
    while True:
        client_socket, addr = server_socket.accept()
        
    return client_socket, addr


def server_register_new_client(addr: AddrClient, name: str) -> None:
    tmp = {addr: client_socket.recv(1024)}
    clients.update(tmp)


def server_greetings_new_client(addr: AddrClient) -> str:
    ...


def server_receive(client_socket):
    while True:
        request = client_socket.recv(1024)
        print(request.decode())
        if not request:
            break
        else:
            response = ('--\n').encode()
            client_socket.send(response)


def evant_loop(server_socket):
    reads, [], [] = select(server_socket.accept(), [], [])
    server_receive(client_socket)


if __name__ == '__main__':
    server_socket = server_setting()
    client_socket, addr = server_accept_connection(server_socket)
    rT = threading.Thread(target=server_accept_connection, args=(server_socket,))
    rT.start()
    server_receive(client_socket)


    # rT.join()
    # server_socket.close()
