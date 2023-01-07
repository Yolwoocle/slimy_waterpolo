from engine.slimyengine import *

game = Game().init().target_fps(60).set_background_color(Colors.darkgrey)

client = Client()
client.connect()


game.update_size()
try:
    while game.is_alive():
        game.begin_frame()

        game.tick()

        game.end_frame()
except KeyboardInterrupt:
    log("Caught KeyboardInterrupt, closing game...", logTypes.warning)
    game.quit()




"""
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
"""