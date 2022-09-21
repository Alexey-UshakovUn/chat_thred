import socket
import config


socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_client.connect((config.HOST, config.PORT))
user_name = str(input('Enter you name: '))
socket_client.send(user_name.encode())

while True:
    msg = socket_client.recv(1024).decode('ascii')
    print(msg)
    client_msg = str(input('Say something: '))

    socket_client.send(client_msg.encode())
    print('msg fly')

