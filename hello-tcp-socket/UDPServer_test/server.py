from socketserver import UDPServer, BaseRequestHandler


class MyHandler(BaseRequestHandler):
    def handle(self):
        data, socket = self.request  # self.request 是 (data, socket) 的組合
        print(f"Received: {data.decode('utf-8')} from {self.client_address}")
        socket.sendto(b"ACK", self.client_address)  # 回應客戶端


server = UDPServer(("127.0.0.1", 9999), MyHandler)
print("伺服器啟動中...")
server.serve_forever()
