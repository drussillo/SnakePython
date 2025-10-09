import Global as g
import Sound
import Apple
import Obstacle

initalized_state = g.Gamestate.VOID

def init_menu() -> None:
    global initalized_state
    if initalized_state != g.Gamestate.MENU:
        Sound.setBGM("./audio/MainSoundtrack1-trianglewave.wav")
        Sound.playBGM()
        initalized_state = g.Gamestate.MENU

def init_fail() -> None:
    global initalized_state
    if initalized_state != g.Gamestate.FAIL:
        g.clear_object_stack()
        Sound.stop()
        initalized_state = g.Gamestate.FAIL


def init_mode_basic() -> None:
    global initalized_state
    if initalized_state != g.Gamestate.MODE_BASIC:
        g.clear_object_stack()
        new_head_x, new_head_y = g.randomize_spawn_pos()
        g.direction = g.randomize_direction()
        g.snake_body = [(new_head_x, new_head_y, g.direction)]
        g.velocity = g.velocity_start
        Sound.setBGM("./audio/MainSoundtrack1.wav")
        Sound.playBGM()
        Apple.init_apples_basic()
        Obstacle.init_obstacles_basic()
        initalized_state = g.Gamestate.MODE_BASIC

