import socket
import time

server = "127.0.0.1"
port = 5555

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.settimeout(0.5)
    s.connect((server, port))
    s.sendall(str.encode(str(0)))
    for i in range(1000):
        try:
            data = int(s.recv(2048).decode())
            print(data)
            s.sendall(str.encode(str(data+1)))
        except socket.timeout:
            pass
        except KeyboardInterrupt:
            s.close()
            break
