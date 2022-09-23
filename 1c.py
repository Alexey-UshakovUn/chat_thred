import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 5000))
user_name = str(input('Enter you name: '))
client_socket.send(user_name.encode())