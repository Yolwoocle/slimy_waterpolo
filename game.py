from engine.slimyengine import *

# Creating global game variable (registers itself in Globals static class)
game = Game().init().target_fps(60).set_background_color(Colors.darkgreen)
game.set_debug(True)

scene = Scene()

camera = scene.active_camera


world = PhysicsWorld().set_limits(vec3(-math.inf, -math.inf, 0.), vec3(math.inf, math.inf, 20.))
Globals.world = world

# Main gameloop
while game.is_alive():
    # Must be called before everything else
    game.begin_frame()
    # Update physics => apply forces from the last frame, this needs a rework in order to react instantly to user inputs
    world.tick()

    # Update parent/ child transforms, quite effective for now but may require a rewrite later
    scene.update()

    scene.draw()

    scene.light_pass()
    # Performs all debug draws, update delta time and wait idle until frame time is reached
    game.end_frame()