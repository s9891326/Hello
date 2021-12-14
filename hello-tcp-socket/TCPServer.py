import socketserver


class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print(f"connect by: {str(self.client_address)}")
        while True:
            in_data = self.request.recv(1024).strip()
            if len(in_data) == 0:  # connection closed
                self.request.close()
                print("client closed connection.")
                break
            print(f"recv: {in_data.decode()}")

            out_data = f"echo {in_data.decode()}"
            self.request.sendall(out_data.encode())


if __name__ == '__main__':
    HOST, PORT = "0.0.0.0", 7000

    # Create the server, binding to localhost on port 7000
    socketserver.TCPServer.allow_reuse_address = True
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)

    print(f"server start at: {HOST}:{PORT}")
    try:
        server.serve_forever()
    except:
        print("closing the server.")
        server.server_close()
        # raise
