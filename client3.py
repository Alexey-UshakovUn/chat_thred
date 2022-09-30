import socket
import threading
import time
import json

from exeption import MassageIsNone


shutdown = False
join = False

server = ('localhost', 5001)
socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_client.connect(('localhost', 5001))
name = input('Name: ')


def receving(sock):
    """ await receive data"""
    while not shutdown:
        try:
            while True:
                data, addr = sock.recvfrom(1024)
                data = data.decode('utf-8')
                pretty_print(data)
                time.sleep(0.2)
        except:
            pass


def join_chat():
    """return greetings for chat"""
    message = "join chat"
    data_to_json(message)


def data_to_json(message):
    """return data in json object"""
    if message != "":
        data = {'name': name,
                'message': message
                }
    else:
        raise MassageIsNone
    return data


def pretty_print(data):
    """print data in terminal"""
    data = json.loads(data)
    print('\n{}:: {}'.format(data.get('name', 'server'), data['message']))


def event_loop(shutdown, join):
    """event loop"""
    while not shutdown:
        if not join:
            join_chat()
            join = True
        else:
            try:
                message = input("\nYou :: ")
                time.sleep(0.2)
                data = data_to_json(message)
                data = json.dumps(data).encode("utf-8")
                socket_client.sendto(data, server)
            except:
                socket_client.sendto(('[' + name + '] :: ' + message).encode('utf-8'), server)
                shutdown = True


if __name__ == '__main__':
    rT = threading.Thread(target=receving, args=(socket_client, ))
    rT.start()
    event_loop(shutdown=False, join=False)
    rT.join()
    socket_client.close()
