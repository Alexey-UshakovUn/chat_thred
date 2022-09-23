import socket
import select

to_monitor = []

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 5000))
server_socket.listen()
print('[ Server is running ]')


def accept_connection(server_socket):
    client_conn, addr = server_socket.accept()
    print('Connection from', addr)

    to_monitor.append(client_conn)


def recive_connection(client_conn):
    request = client_conn.recv(1024)
    if request:
        print(request.decode())
        response = '-------'
        # client_conn.send(response.encode())
        client_conn.sendall(request)
    else:
        client_conn.close()


def event_loop():
    while True:
        conns, _, _ = select.select(to_monitor, [], [])
        for conn in conns:
            if conn == server_socket:
                accept_connection(conn)
            else:
                recive_connection(conn)


if __name__ == '__main__':
    to_monitor.append(server_socket)
    event_loop()
