import socket
import time

# 建立socket：s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 連線至遠端地址：s.connect()
# 傳送資料：s.send()、s.sendall()
# 接收資料：s.recv()
# 傳輸完畢後，關閉socket：s.close()

HOST = '127.0.0.1'
PORT = 7000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    # outdata = input('please input message: ')
    out_data = "heartbeat"
    print('send: ' + out_data)
    s.send(out_data.encode())

    in_data = s.recv(1024)
    if len(in_data) == 0:  # connection closed
        s.close()
        print('server closed connection.')
        break
    print('recv: ' + in_data.decode())

    time.sleep(1)
