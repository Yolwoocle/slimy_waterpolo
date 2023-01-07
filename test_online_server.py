from engine.slimyengine import *

game = Game().init().target_fps(60).set_background_color(Colors.darkgrey)

server = Server()
server.open()


game.update_size()
try:
    while game.is_alive():
        game.begin_frame()

        game.tick()

        game.end_frame()
except KeyboardInterrupt:
    log("Caught KeyboardInterrupt, closing game...", logTypes.warning)
    game.quit()