import socket
import threading

class server:

    def __init__(self, host='127.0.0.1', port=5555):
        self.PlayerNUM = {}
        self.HOST = host
        self.PORT = port
        self.clients = []

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.HOST, self.PORT))
        self.server.listen()

    def handle_client(self, conn):
        try:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                self.broadcast(data)
                print(data)
        except:
            pass
        finally:
            conn.close()

    def start(self):
        try:
            while True:
                conn, addr = self.server.accept()

                self.PlayerNUM[f"conn number {len(self.clients)}"] = conn
                print("1 person connected")
                print(self.PlayerNUM)

                t = threading.Thread(
                    target=self.handle_client,
                    args=(conn,),
                    daemon=True
                )
                t.start()

                self.clients.append(conn)
                print(len(self.clients))

                self.broadcast(
                    f"server: Player {len(self.clients)} has joined the game."
                    .encode()
                )

                if len(self.clients) > 3:
                    print("Maximum number of players reached.")
                    break

                self.game()

        except KeyboardInterrupt:
            print("\nShutting down server...")
            self.server.close()

    def broadcast(self, message):
        for client in self.clients:
            try:
                client.sendall(message)
            except:
                print("Error sending message to client.")

    def game(self):
        print("game started")

if __name__ == "__main__":
    s = server()
    s.start()
