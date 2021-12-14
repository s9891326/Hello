import socketserver
import sys
import threading
import time


class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        cur = threading.current_thread()
        print(f"{time.ctime()} Client connected from {self.request.getpeername()} and {cur.name}is handling with him.")
        while True:
            in_data = self.request.recv(1024).strip()
            if len(in_data) == 0:  # connection closed
                self.request.close()
                print("client closed connection.")
                break
            print(f"recv: {in_data.decode()}")

            out_data = f"echo {in_data.decode()}"
            self.request.sendall(out_data.encode())


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    daemon_threads = True
    allow_reuse_address = True


class MyTCPServer(socketserver.ThreadingTCPServer):
    daemon_threads = True
    allow_reuse_address = True


if __name__ == '__main__':
    HOST, PORT = "0.0.0.0", 7000
    # server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
    server = MyTCPServer((HOST, PORT), ThreadedTCPRequestHandler)

    print(f"server start at: {HOST}:{PORT}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        sys.exit()
