import random

import Global as g
import Sound
import Apple
import Obstacle

initalized_state = g.Gamestate.VOID

def init_menu() -> None:
    global initalized_state
    if initalized_state != g.Gamestate.MENU:
        Sound.setBGM(g.resource_path("audio/MainSoundtrack1-trianglewave.wav"))
        Sound.playBGM()
        initalized_state = g.Gamestate.MENU

def init_fail() -> None:
    global initalized_state
    if initalized_state != g.Gamestate.FAIL:
        g.clear_object_stack()
        Sound.stop()
        initalized_state = g.Gamestate.FAIL

def init_settings() -> None:
    global initalized_state
    if initalized_state != g.Gamestate.SETTINGS:
        # reset temp settings
        g.screen_w_temp = g.screen_w
        g.screen_h_temp = g.screen_h
        g.fullscreen_temp = g.fullscreen
        g.velocity_temp = g.velocity
        g.max_fps_temp = g.max_fps
        g.d_size_temp = g.d_size
        g.d_dist_temp = g.d_dist
        g.sfx_temp = g.sfx
        g.music_temp = g.music
        initalized_state = g.Gamestate.SETTINGS


def init_mode_basic() -> None:
    global initalized_state
    if initalized_state != g.Gamestate.MODE_BASIC:
        g.current_bgtileset = random.choices((
            g.bgtileset_grass,
            g.bgtileset_desert,
            g.bgtileset_jungle,
            g.bgtileset_city,
            g.bgtileset_frozen,
            g.bgtileset_snow,
            g.bgtileset_cherryblossom
        ), weights=(4, 3, 3, 2, 2, 2, 1))[0]
        g.generate_random_background()
        g.clear_object_stack()
        new_head_x, new_head_y = g.randomize_spawn_pos()
        g.direction = g.randomize_direction()
        g.snake_body = [(new_head_x, new_head_y, g.direction)]
        g.velocity = g.velocity_start
        Sound.setBGM(g.resource_path("audio/MainSoundtrack1.wav"))
        Sound.playBGM()
        Apple.init_apples_basic()
        Obstacle.init_obstacles_basic()
        initalized_state = g.Gamestate.MODE_BASIC

