from engine.slimyengine import *


game = Game().init().target_fps(60).set_background_color(Colors.darkgrey)
game.set_debug(True)
game.load_image("player", "data/player.png")

main_menu = Scene()

world = game.get_world()
# world.enable_physics()
# world.get_physics_world().set_limits(vec3(-math.inf, -math.inf, 0.), vec3(math.inf, math.inf, 20.))

world.load_scene(main_menu)

play_btn        = Button(None, vec2(50, -100), vec2(200, 60), Colors.green, text="Jouer").register()
settings_btn    = Button(None, vec2(50, 0), vec2(200, 60), Colors.green, "Paramètres").register()
quit_btn        = Button(None, vec2(50, 100), vec2(200, 60), Colors.green, "Quitter").register().set_callback(lambda: game.quit())

game.update_size()
while game.is_alive():
    game.begin_frame()

    game.tick()

    game.end_frame()