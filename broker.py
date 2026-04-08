import socket
import threading

clients = []
subscriptions = {}

def handle_client(conn, addr):
    print(f"Client connected: {addr}")
    clients.append(conn)

    try:
        while True:
            data = conn.recv(1024).decode()
            if not data:
                break

            parts = data.split(" ", 2)

            if parts[0] == "SUB":
                topic = parts[1]
                subscriptions.setdefault(topic, []).append(conn)
                print(f"{addr} subscribed to {topic}")

            elif parts[0] == "PUB":
                topic = parts[1]
                message = parts[2]

                print(f"Message on {topic}: {message}")

                for sub in subscriptions.get(topic, []):
                    sub.send(f"{topic}: {message}".encode())

    except:
        pass
    finally:
        conn.close()
        clients.remove(conn)
        print(f"Client disconnected: {addr}")

def start_broker(host="0.0.0.0", port=1883):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()

    print(f"Broker running on {host}:{port} ")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
    start_broker()