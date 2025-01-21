from socketserver import TCPServer, BaseRequestHandler, ThreadingTCPServer


class MyHandler(BaseRequestHandler):

    def handle(self):
        while True:
            data = self.request.recv(1024).strip()
            print(f"Received: {data}")
            self.request.sendall(b"Hello client!")


# server = TCPServer(("127.0.0.1", 9999), MyHandler)
# server.serve_forever()

server = ThreadingTCPServer(("127.0.0.1", 9999), MyHandler)
server.serve_forever()
