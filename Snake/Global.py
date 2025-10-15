import pygame
import random
from enum import Enum

# Settings
# 500x500 min res
screen_w:int = 720
screen_h:int = 720
fullscreen:bool = False
velocity:int = 2 #pixels per frame; MAX is tile_size or size + dist
max_fps:int = 120
d_size:int = 60 #default size
d_dist:int = 5 #default distance
sfx:bool = True 
music:bool = True
HUD_divisor:int = 10

d_tile_size:int = d_size + d_dist
#adjust tile size according to velocity
def adjust_d_tile_size() -> None:
    global d_tile_size
    global d_size
    global d_dist
    d_tile_size = d_size + d_dist
    if d_tile_size % velocity != 0:
        adj_size = (d_tile_size % velocity) // 2
        adj_dist = (d_tile_size % velocity) - adj_size
        d_size -= adj_size
        d_dist -= adj_dist
        d_tile_size = d_size + d_dist
adjust_d_tile_size()

#miscellaneous
default_font = None
REAL_SCREEN = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) if fullscreen else pygame.display.set_mode([screen_w, screen_h])
SCREEN = pygame.Surface((screen_w, screen_h))
clock = pygame.time.Clock()

# temp settings
screen_w_temp:int
screen_h_temp:int
fullscreen_temp:bool = fullscreen
velocity_temp:int
max_fps_temp:int
d_size_temp:int
d_dist_temp:int
sfx_temp:bool
music_temp:bool


# gamestates
class Gamestate(Enum):
    VOID = 0
    MENU = 1
    FAIL = 2
    SETTINGS = 3
    MODE_BASIC = 4

current_state: Gamestate = Gamestate.MENU

HUD_w:int = 0
HUD_h:int = 0
def set_HUD() -> None:
    global HUD_w
    global HUD_h
    HUD_w = screen_w
    HUD_h = screen_h // HUD_divisor
set_HUD()
velocity_start:int = velocity
offset_x:int
offset_y:int
def set_offsets() -> None:
    global offset_x
    global offset_y
    offset_x = screen_w % d_tile_size // 2
    offset_y = (screen_h - HUD_h) % d_tile_size // 2
set_offsets()

def get_sprite(sheet, x, y, width, height):
    # Create a new Surface for the individual sprite
    sprite_image = pygame.Surface((width, height), pygame.SRCALPHA)
    # Blit the desired portion of the sprite sheet onto the new Surface
    sprite_image.blit(sheet, (0, 0), (x, y, width, height))
    return sprite_image

#start drawables
buttonscale:int = 4  # each row is 14px
buttons = pygame.image.load("drawables/buttons.png").convert_alpha()
emptybutton = pygame.transform.scale(get_sprite(buttons, 0, 0, 41, 14), (41 * buttonscale, 14 * buttonscale))
menubutton = pygame.transform.scale(get_sprite(buttons, 0, 14, 34, 14), (34 * buttonscale, 14 * buttonscale))
retrybutton = pygame.transform.scale(get_sprite(buttons, 0, 28, 41, 14), (41 * buttonscale, 14 * buttonscale))
startbutton = pygame.transform.scale(get_sprite(buttons, 0, 42, 41, 14), (41 * buttonscale, 14 * buttonscale))
settingsbutton = pygame.transform.scale(get_sprite(buttons, 0, 56, 61, 14), (61 * buttonscale, 14 * buttonscale))
cancelbutton = pygame.transform.scale(get_sprite(buttons, 0, 70, 48, 14), (48 * buttonscale, 14 * buttonscale))
savebutton = pygame.transform.scale(get_sprite(buttons, 0, 84, 34, 14), (34 * buttonscale, 14 * buttonscale))
sfxonbutton = pygame.transform.scale(get_sprite(buttons, 0, 98, 17, 14), (17 * buttonscale, 14 * buttonscale))
sfxoffbutton = pygame.transform.scale(get_sprite(buttons, 0, 112, 17, 14), (17 * buttonscale, 14 * buttonscale))
musiconbutton = pygame.transform.scale(get_sprite(buttons, 0, 126, 17, 14), (17 * buttonscale, 14 * buttonscale))
musicoffbutton = pygame.transform.scale(get_sprite(buttons, 0, 140, 17, 14), (17 * buttonscale, 14 * buttonscale))
fullscreenbutton = pygame.transform.scale(get_sprite(buttons, 0, 154, 17, 14), (17 * buttonscale, 14 * buttonscale))

bgtiles = pygame.image.load("drawables/bgtiles.png").convert_alpha()
bgtile1 = pygame.transform.scale(get_sprite(bgtiles, 0, 0, 15, 15), (d_tile_size, d_tile_size))
bgtile2 = pygame.transform.scale(get_sprite(bgtiles, 15, 0, 15, 15), (d_tile_size, d_tile_size))
bgtile3 = pygame.transform.scale(get_sprite(bgtiles, 30, 0, 15, 15), (d_tile_size, d_tile_size))
bgtile4 = pygame.transform.scale(get_sprite(bgtiles, 45, 0, 15, 15), (d_tile_size, d_tile_size))

snakesegments = pygame.image.load("drawables/segments.png").convert_alpha()
snakesegment_vert = pygame.transform.scale(get_sprite(snakesegments, 0, 0, 15, 15), (d_size, d_size))
snakesegment_hor = pygame.transform.rotate(snakesegment_vert, 90)

snakehead_n = pygame.transform.scale(get_sprite(snakesegments, 30, 0, 15, 15), (d_size, d_size))
snakehead_e = pygame.transform.rotate(snakehead_n, -90)
snakehead_s = pygame.transform.rotate(snakehead_e, -90)
snakehead_w = pygame.transform.rotate(snakehead_s, -90)

snakelast_n = pygame.transform.scale(get_sprite(snakesegments, 15, 0, 15, 15), (d_size, d_size))
snakelast_e = pygame.transform.rotate(snakelast_n, -90)
snakelast_s = pygame.transform.rotate(snakelast_e, -90)
snakelast_w = pygame.transform.rotate(snakelast_s, -90)

objects = pygame.image.load("drawables/objects.png").convert_alpha()
defapple = pygame.transform.scale(get_sprite(objects, 0, 0, 15, 15), (d_size, d_size))
boulder = pygame.transform.scale(get_sprite(objects, 15, 0, 15, 15), (d_size, d_size))


#randomize background
background_arr:list[list[type(SCREEN)]]
def generate_random_background() -> None:
    global background_arr
    background_arr = [[random.choice([bgtile1, bgtile2, bgtile3, bgtile4]) for x in range(screen_w // d_tile_size)] for y in range((screen_h - HUD_h) // d_tile_size)]
generate_random_background()

def randomize_spawn_pos() -> (int, int):
    min_x = d_size * 5 * velocity if d_size * 5 * velocity < screen_w // 2 - d_size else screen_w // 2 - d_size
    max_x = screen_w - d_size * 5 * velocity if screen_w - d_size * 5 * velocity > screen_w // 2 + d_size else screen_w // 2 + d_size
    min_y = HUD_h + d_size * 5 * velocity if HUD_h + d_size * 5 * velocity < screen_h // 2 - d_size else screen_h // 2 - d_size
    max_y = screen_h - d_size * 5 * velocity if screen_h - d_size * 5 * velocity > screen_h // 2 + d_size else screen_h // 2 + d_size
    rnd_x, rnd_y = (random.randint(min_x, max_x), random.randint(min_y, max_y))
    return (rnd_x - rnd_x % d_tile_size + offset_x, rnd_y - rnd_y % d_tile_size + HUD_h + offset_y)

def randomize_direction() -> str:
    rnd_char_dict = {
        0: 'n',
        1: 's',
        2: 'e',
        3: 'w'
    }
    return rnd_char_dict[random.randint(0, 3)] #north, s, e or w

# initial snake body
head_x, head_y = randomize_spawn_pos()
direction = randomize_direction()
snake_body:list[(int, int, str)] = [(head_x, head_y, direction)]

# objects
object_stack = []

def clear_object_stack() -> None:
    global object_stack
    object_stack = []

#Help functions
def get_middle_pos(w=0, h=0) -> (int, int):
    return (screen_w // 2 - w // 2, screen_h // 2 - h // 2)

def toggle_sfx_temp() -> None:
    global sfx_temp
    sfx_temp = not sfx_temp

def toggle_music_temp() -> None:
    global music_temp
    music_temp = not music_temp

def toggle_fullscreen() -> None:
    global fullscreen_temp
    global SCREEN
    fullscreen_temp = not fullscreen_temp
    REAL_SCREEN = pygame.display.set_mode([screen_w, screen_h], pygame.FULLSCREEN, pygame.SCALED) if fullscreen_temp else pygame.display.set_mode([screen_w, screen_h])

# reset functions

def reset_menu() -> None:
    global current_state
    current_state = Gamestate.MENU

def reset_fail() -> None:
    global current_state
    current_state = Gamestate.FAIL

def reset_settings() -> None:
    global current_state
    current_state = Gamestate.SETTINGS

def reset_mode_basic() -> None:
    global current_state
    current_state = Gamestate.MODE_BASIC

