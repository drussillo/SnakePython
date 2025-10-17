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
legacy_mode:bool = False
HUD_divisor:int = 10 #screen_w // HUD_divisor

d_tile_size:int = d_size + d_dist
#adjust tile size according to velocity
def adjust_d_tile_size() -> None:
    global d_tile_size
    global d_size
    global d_dist
    if d_tile_size % (velocity*2) != 0:
        adj_size = (d_tile_size % (velocity*2)) // 2
        adj_dist = (d_tile_size % (velocity*2)) - adj_size
        d_size -= adj_size
        d_dist -= adj_dist
        d_tile_size = d_size + d_dist
adjust_d_tile_size()

#miscellaneous
# TODO: CREDIT: Comicoro font by jeti
default_font:str = "./fonts/mainfont.ttf"
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
legacy_mode_temp:bool


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
ogonbutton = pygame.transform.scale(get_sprite(buttons, 0, 168, 17, 14), (17 * buttonscale, 14 * buttonscale))
ogoffbutton = pygame.transform.scale(get_sprite(buttons, 0, 182, 17, 14), (17 * buttonscale, 14 * buttonscale))

bgtiles = pygame.image.load("drawables/bgtiles.png").convert_alpha()
bgtileset_grass:tuple[pygame.surface.Surface, ...] = (
    pygame.transform.scale(get_sprite(bgtiles, 00, 0, 15, 15), (d_tile_size, d_tile_size)),
    pygame.transform.scale(get_sprite(bgtiles, 15, 0, 15, 15), (d_tile_size, d_tile_size)),
    pygame.transform.scale(get_sprite(bgtiles, 30, 0, 15, 15), (d_tile_size, d_tile_size)),
    pygame.transform.scale(get_sprite(bgtiles, 45, 0, 15, 15), (d_tile_size, d_tile_size))
)
bgtileset_desert:tuple[pygame.surface.Surface, ...] = (
    pygame.transform.scale(get_sprite(bgtiles, 00, 15, 15, 15), (d_tile_size, d_tile_size)),
    pygame.transform.scale(get_sprite(bgtiles, 15, 15, 15, 15), (d_tile_size, d_tile_size)),
    pygame.transform.scale(get_sprite(bgtiles, 30, 15, 15, 15), (d_tile_size, d_tile_size)),
    pygame.transform.scale(get_sprite(bgtiles, 45, 15, 15, 15), (d_tile_size, d_tile_size))
)
bgtileset_jungle:tuple[pygame.surface.Surface, ...] = (
    pygame.transform.scale(get_sprite(bgtiles, 00, 30, 15, 15), (d_tile_size, d_tile_size)),
    pygame.transform.scale(get_sprite(bgtiles, 15, 30, 15, 15), (d_tile_size, d_tile_size)),
    pygame.transform.scale(get_sprite(bgtiles, 30, 30, 15, 15), (d_tile_size, d_tile_size)),
    pygame.transform.scale(get_sprite(bgtiles, 45, 30, 15, 15), (d_tile_size, d_tile_size))
)
bgtileset_city:tuple[pygame.surface.Surface, ...] = (
    pygame.transform.scale(get_sprite(bgtiles, 00, 45, 15, 15), (d_tile_size, d_tile_size)),
    pygame.transform.scale(get_sprite(bgtiles, 15, 45, 15, 15), (d_tile_size, d_tile_size)),
    pygame.transform.scale(get_sprite(bgtiles, 30, 45, 15, 15), (d_tile_size, d_tile_size)),
    pygame.transform.scale(get_sprite(bgtiles, 45, 45, 15, 15), (d_tile_size, d_tile_size))
)
bgtileset_snow:tuple[pygame.surface.Surface, ...] = (
    pygame.transform.scale(get_sprite(bgtiles, 00, 60, 15, 15), (d_tile_size, d_tile_size)),
    pygame.transform.scale(get_sprite(bgtiles, 15, 60, 15, 15), (d_tile_size, d_tile_size)),
    pygame.transform.scale(get_sprite(bgtiles, 30, 60, 15, 15), (d_tile_size, d_tile_size)),
    pygame.transform.scale(get_sprite(bgtiles, 45, 60, 15, 15), (d_tile_size, d_tile_size))
)
# TODO: snow / frozen background + more backgrounds?
bgtileset_cherryblossom:tuple[pygame.surface.Surface, ...] = (
    pygame.transform.scale(get_sprite(bgtiles, 00, 75, 15, 15), (d_tile_size, d_tile_size)),
    pygame.transform.scale(get_sprite(bgtiles, 15, 75, 15, 15), (d_tile_size, d_tile_size)),
    pygame.transform.scale(get_sprite(bgtiles, 30, 75, 15, 15), (d_tile_size, d_tile_size)),
    pygame.transform.scale(get_sprite(bgtiles, 45, 75, 15, 15), (d_tile_size, d_tile_size))
)

bgtilesmenuscale:int = 6
bgtilesmenu = pygame.image.load("drawables/bgtilesmenu.png").convert_alpha()
bgtilemenu1 = pygame.transform.scale(get_sprite(bgtilesmenu, 0, 0, 14, 14), (14 * bgtilesmenuscale, 14 * bgtilesmenuscale))
# TODO: improve current menu bgtile
# TODO: add more bg tiles for menu

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
cactus = pygame.transform.scale(get_sprite(objects, 30, 0, 15, 15), (d_size, d_size))

# random tile background array
current_bgtileset:tuple[pygame.surface.Surface, ...] = bgtileset_grass  # default to grass
background_arr:list[list[pygame.surface.Surface]]
def generate_random_background():
    global background_arr
    background_arr = [
        [
            random.choice(current_bgtileset)
            for x in range(screen_w // d_tile_size)
        ]
        for y in range((screen_h - HUD_h) // d_tile_size)
    ]

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

def toggle_legacy_mode() -> None:
    global legacy_mode
    legacy_mode = not legacy_mode

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

