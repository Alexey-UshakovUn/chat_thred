import socket


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 5000))
server_socket.listen()
print('[ Server is running ]')

while True:
    client_conn, addr = server_socket.accept()
    print('Connection from', addr)

    while True:
        request = client_conn.recv(1024)
        if not request:
             break
        else:
            print(request.decode())
            response = 'you request is done'
            client_conn.send(response.encode())
    print('end send')
    client_conn.close()

#
# if __name__ == '__main__':
#