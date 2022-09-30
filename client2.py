import socket
import threading

help_text = ['exit', ]


def client_config():
    socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_client.connect(('localhost', 5001))
    user_name = str(input('Enter you name: '))
    socket_client.send(user_name.encode())
    return socket_client, user_name


def event_loop(socket_client, user_name):
    while True:

        msg = receive_message(socket_client)
        print(msg)

        input_message_from_user(user_name)

        msg = '{}:{}'.format(user_name, client_msg)
        socket_client.sendall(msg.encode())
        if client_msg in help_text:
            socket_client.close()
            break


def receive_message(socket_client):
    """return receive message"""
    while True:
        yield ('read', socket_client)
        msg = socket_client.recv(1024).decode('utf-8')
        return msg



def print_message():
    """print message in window"""
    pass


def input_message_from_user():
    """return message from user"""
    while True:
        yield ('write', )
        client_msg = str(input('{}: '.format(user_name)))



def connect_to_server():
    """return ip server, port and username"""
    pass


if __name__ == '__main__':
    socket_client, user_name = client_config()
    event_loop(socket_client, user_name)
