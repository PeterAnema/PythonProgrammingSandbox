import socket
from threading import Thread

IP_ADDRESS = '0.0.0.0'   # all of localhost '127.0.0.1'
IP_PORT = 6669

connected_clients = []


class Session(Thread):

    def __init__(self, connection, addr, name = 'Anoniem'):
        super().__init__()
        self.__connection = connection
        self.__addr = ':'.join(map(str, addr))
        self.__name = name
        self.__state = {'name_known': False}
        print('Thread created for client at %s' % self.__addr)

    def __repr__(self):
        return '%s' % self.__addr

    def __str__(self):
        return '%s at %s' % (self.__name, self.__addr)

    def prompt_client_for_response(self, prompt = '? ', logging = False):
        if logging:
            print('%s - Sending: %s' % (self.__addr, prompt))

        self.__connection.send(prompt.encode('utf-8'))
        received = self.__connection.recv(1024).decode('utf-8')

        if logging:
            print('%s - Received: %s' % (self.__addr, received))

        return received

    def ask_client_name(self):
        prompt = 'What name do you want to use? : '
        return self.prompt_client_for_response(prompt)

    def run(self):
        try:
            if not self.__state['name_known']:
                self.__name = self.ask_client_name()

            response = ''
            while True:
                prompt = 'What can I do for you, %s? ' % self.__name
                received = self.prompt_client_for_response(response + '\n' + prompt, logging = True)
                if received.lower() == 'close':
                    break
                elif received.lower() == 'players':
                    response = '\nPlayers:\n  ' + '\n  '.join(map(str, connected_clients))
                else:
                    response = 'Unknown command "%s"' % received

        except:
            print('Client at %s closed connection.' % self.__addr)

        self.__connection.close()
        del connected_clients[connected_clients.index(self)]
        print('Connection with client %s closed.' % self.__addr)


def main():
    host = IP_ADDRESS
    port = IP_PORT

    s = socket.socket()
    try:
        s.bind((host, port))
    except OSError:
        print('Address already is use.')

    while True:
        s.listen()
        print('Server listening on %s on port %d' % (host, port))

        try:
            c, addr = s.accept()

        except KeyboardInterrupt:
            print('Shutting down the server')
            break

        print('Accepting connection from client ' + str(addr))

        th = Session(c, addr)
        connected_clients.append(th)
        th.start()


if __name__ == '__main__':
    main()