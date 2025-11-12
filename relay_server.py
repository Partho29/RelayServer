import os
import socket, threading

HOST = '0.0.0.0'
PORT = int(os.environ.get("PORT", 5050))
clients = []

def handle_client(conn, addr):
    print(f"[+] {addr} connected")
    clients.append(conn)
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            # Forward data to other clients
            for c in clients:
                if c != conn:
                    c.sendall(data)
    except:
        pass
    finally:
        clients.remove(conn)
        conn.close()
        print(f"[-] {addr} disconnected")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(2)
print(f"Relay server listening on port {PORT}...")

while True:
    conn, addr = server.accept()
    threading.Thread(target=handle_client, args=(conn, addr)).start()
