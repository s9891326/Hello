import socket

# 建立socket：s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)，並指定 socket.AF_INET (TCP) 的通訊協定
# 綁定socket到本地IP與port：s.bind()
# 開始監聽：s.listen()
# 等待與接受客戶端的請求連線：s.accept()
# 接收客戶端傳來的資料：s.recv()
# 傳送給對方發送資料：s.send()、s.sendall()
# 傳輸完畢後，關閉socket：s.close()

HOST = '0.0.0.0'
PORT = 7000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(5)

print('server start at: %s:%s' % (HOST, PORT))
print('wait for connection...')

while True:
    conn, addr = s.accept()
    print(f"connected by {addr}")
    while True:
        in_data = conn.recv(1024)
        if len(in_data) == 0:  # connection closed
            conn.close()
            print("client closed connection.")
            break

        print(f"recv: {in_data.decode()}")

        out_data = f'echo {in_data.decode()}'
        conn.send(out_data.encode())

