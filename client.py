import socket
import threading
import json

class clientPlayer:
    def __init__(self):
        self.HOST = "127.0.0.1"
        self.PORT = 5555
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.receive_messages()
            self.client.connect((self.HOST, self.PORT))
            print("Connection successful!")
        except ConnectionRefusedError:
            print("Connection failed: server is not available.")
        except Exception as e:
            print("Connection failed:", e)
    def receive_messages(self):
      while True:
        try:
            message =self.client.recv(1024).decode()
            print(message)
        except:
            break
        thread = threading.Thread(target=self.receive_messages)
        thread.start()
    def send_to_backend(self, data):
        try:
            if isinstance(data, dict):
                data = json.dumps(data).encode("utf-8")
            elif isinstance(data, str):
                data = data.encode("utf-8")
            self.client.sendall(data)

        except Exception as e:
            print(f"Error sending data: {e}")
if __name__ == "__main__":
    s = clientPlayer()
