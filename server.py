import socket
import select
import json
from exeption import CantAppendClient, CantGetSocket

clients_connect = {}
to_monitor = clients_connect.values()
help_text = ['exit', ]


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 5001))
server_socket.listen()
print('[ Server is running ]')


def accept_connection(server_socket):
    """accept connection and return client socket, and client addr"""
    client_socket, addr = server_socket.accept()
    print('Connection from', addr)
    return client_socket, addr


def recive_connection(client_socket):
    """send request to client and close connection if not request"""
    request = client_socket.recv(1024).decode()
    if request in help_text:
        print('control')
        control(request, client_socket)
    elif request:
        print(request)
        request = request.encode()
        for conn in to_monitor:
            if conn != server_socket and conn != client_socket:
                conn.send(request)
    else:
        client_socket.close()


def append_clients(addr, client_socket):
    """append client in db"""
    if addr not in clients_connect:
        clients_connect[addr] = client_socket
    else:
        raise CantAppendClient


def control(request, client_socket):
    """Сейчас работает только с экситом, должна возвращать функции которые есть в хелп тексте"""
    print(request)
    chat_exit(client_socket)


def chat_exit(client_socket):
    """ Функция выхода из чата реализована и на сервере у клиента. Реализована не верно так как если клиент отвалился
    или не отправляет сообщений сервер просто проверяет есть ли сокет клиента и должен был его просто убрать"""
    feedback = 'disconnection from {}'.format(client_socket.getpeername())
    clients_connect.pop(client_socket.getpeername())
    client_socket.sendall(feedback.encode())
    client_socket.close()


def event_loop():
    """Ну тут все понятно обычный эвент луп"""
    while True:
        try:
            conns, _, _ = select.select(to_monitor, [], [])
        except ValueError:
            raise CantGetSocket
        for conn in conns:
            if conn == server_socket:
                client_conn, addr = accept_connection(conn)
                append_clients(addr, client_conn)
            else:
                recive_connection(conn)


# def run():
#     clients_connect[('localhost', 5001)] = server_socket
#     event_loop()


if __name__ == '__main__':
    def run():
        clients_connect[('localhost', 5000)] = server_socket
        event_loop()

    run()
