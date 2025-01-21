import socket
import time

HOST = '127.0.0.1'
PORT = 9999


if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    while True:
        s.send(b"TEST")

        in_data = s.recv(1024)
        if len(in_data) == 0:  # connection closed
            s.close()
            print('server closed connection.')
            break
        print('recv: ' + in_data.decode())

        time.sleep(2)

