import sys
import socket

IP_ADDRESS = '0.0.0.0'   # all of localhost '127.0.0.1'
IP_PORT = 6669

def proces_message(message):
    # return message.upper()
    return str((len(message) * 7) % 11)

def main():
    host = IP_ADDRESS
    port = IP_PORT

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Socket created')

    try:
        s.bind((host, port))
    except socket.error as err:
        print('Error')
        # print('Bind failed. Error Code: %s Message %s' % (err[0], err[1]))
        sys.exit()
    except Exception as err:
        print(err)

    print('Socket bind complete')

    s.listen()
    print('Listening on %s on port %d' % (host, port))

    conn, addr = s.accept()
    print('Connection from : ' + str(addr))

    try:
        response = ''
        while True:
            prompt = response + '\n> '
            conn.send(prompt.encode('utf-8'))
            received = conn.recv(1024).decode('utf-8')
            print('Received from connected user : ' + received)
            response = proces_message(received)
            print('Sending back : ' + str(response))

    except:
        print('Client closed connection.')

    conn.close()
    print('Done. Connection closed.')

if __name__ == '__main__':
    main()