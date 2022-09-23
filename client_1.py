import socket
import config


def client_config():
    socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_client.connect((config.HOST, config.PORT))
    user_name = str(input('Enter you name: '))
    socket_client.send(user_name.encode())
    return socket_client


def event_loop(socket_client):
    while True:
        msg = socket_client.recv(1024).decode('ascii')
        print(msg)
        client_msg = str(input('Say something: '))
        socket_client.send(client_msg.encode())


if __name__ == '__main__':
    socket_client = client_config()
    event_loop(socket_client)

