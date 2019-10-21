# Echo client program
import socket

HOST = ''    # The remote host
PORT = 50007              # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    while True:
        data = str.encode(input('> '))
        if not data: break
        s.sendall(data)
        print('Sent: ', data)
        data = s.recv(1024)
        print('Received', repr(data))