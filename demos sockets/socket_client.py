import sys
import socket

IP_ADDRESS = '127.0.0.1'
IP_PORT = 6669

class ClientSession():

    def __init__(self, host = IP_ADDRESS, port = 6669):
        self._host = host
        self._port = port
        self._socket = None

    def connect(self):
        self._socket = socket.socket()
        try:
            self._socket.connect((self._host, self._port))
        except ConnectionRefusedError:
            print('Cannot connect to server %s:%d' % (self._host, self._port))
            sys.exit()

    def send(self, message):
        self._socket.send(message.encode('utf-8'))

    def receive(self):
        return self._socket.recv(1024).decode('utf-8')

    def disconnect(self):
        self._socket.close()

    def receive_prompt_send_command(self):
        while True:
            received = self.receive()
            message = input(received)
            if message == 'close':
                break
            self.send(message)

def main():
    session = ClientSession(host = '127.0.0.1', port = 6669)
    session.connect()
    session.receive_prompt_send_command()
    session.disconnect()


if __name__ == '__main__':
    main()