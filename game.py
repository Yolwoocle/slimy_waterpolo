from engine.slimyengine import *

class Player(Pawn):
    def __init__(self, pos:vec3|None=...):
        Pawn.__init__(self, world, pos, "player")
        scene.register_component(self._root)

game = Game().init().target_fps(60).set_background_color(Colors.darkgreen)
game.set_debug(True)
game.load_image("player", "data/player.png")

scene = Scene()
camera = scene.active_camera

world = PhysicsWorld().set_limits(vec3(-math.inf, -math.inf, 0.), vec3(math.inf, math.inf, 20.))
Globals.world = world

player = Player(vec3(1, 1, 0))

game.update_size()
player.root.set_local_position(player.root.get_local_position())

while game.is_alive():
    game.begin_frame()
    world.tick()
    scene.update()
    scene.draw()
    scene.light_pass()
    game.end_frame()