import socket
import io_common
from threading import Thread


PORT_NUMBER = 2222
MESSAGE_LENGTH = 1024


class ClientThread(Thread):

    def __init__(self, _client_socket, _client_address):
        Thread.__init__(self)
        self.client_socket = _client_socket
        self.client_address = _client_address
        print('Connection established for', _client_address)

    def run(self):
        while True:
            try:
                data = io_common.receive(self.client_socket, MESSAGE_LENGTH)
                if data.decode('utf-8') == 'close':
                    break
                io_common.send(self.client_socket, data)
            except RuntimeError as err:
                print('ERROR', err)
                break
        self.client_socket.close()
        print('Connection closed for', self.client_address)


if '__main__' == __name__:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((socket.gethostname(), PORT_NUMBER))
    server_socket.listen(10)

    while True:
        (client_socket, client_address) = server_socket.accept()
        client_thread = ClientThread(client_socket, client_address)
        client_thread.start()