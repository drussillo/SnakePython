import pygame
import random

#Settings
screen_w = 1920
screen_h = 1080
SCREEN = pygame.display.set_mode([screen_w, screen_h])
velocity = 3 #pixels per frame; MAX is tile_size or size + dist
d_size = 60 #default size
d_dist = 5 #default distance
d_tile_size = d_size + d_dist
#adjust tile size according to velocity
if d_tile_size % velocity != 0:
    adj_size = (d_tile_size % velocity) // 2
    adj_dist = (d_tile_size % velocity) - adj_size
    d_size -= adj_size
    d_dist -= adj_dist
    d_tile_size = d_size + d_dist
    print(f"{d_size}, {d_dist}, {d_tile_size}, {velocity}") #debug
HUD_w = screen_w
HUD_h = 100

clock = pygame.time.Clock()
failstate = False

#start drawables
snakesegment_hor = pygame.image.load("imgs/snakesegment.png")
snakesegment_hor = pygame.transform.scale(snakesegment_hor, (d_size, d_size))
snakesegment_vert = pygame.transform.rotate(snakesegment_hor, 90)

snakehead_n = pygame.image.load("imgs/snakehead.png")
snakehead_n = pygame.transform.scale(snakehead_n, (d_size, d_size))
snakehead_e = pygame.transform.rotate(snakehead_n, -90)
snakehead_s = pygame.transform.rotate(snakehead_e, -90)
snakehead_w = pygame.transform.rotate(snakehead_s, -90)

snakelast_w = pygame.image.load("imgs/snakelast.png")
snakelast_w = pygame.transform.scale(snakelast_w, (d_size, d_size))
snakelast_n = pygame.transform.rotate(snakelast_w, -90)
snakelast_e = pygame.transform.rotate(snakelast_n, -90)
snakelast_s = pygame.transform.rotate(snakelast_e, -90)

defapple = pygame.image.load("imgs/defaultapple.png")
defapple = pygame.transform.scale(defapple, (d_size, d_size))
#end drawables

min_x = d_size * 5 * velocity if d_size * 5 * velocity < screen_w // 2 - d_size else screen_w // 2 - d_size
max_x = screen_w - d_size * 5 * velocity if screen_w - d_size * 5 * velocity < screen_w // 2 + d_size else screen_w // 2 + d_size
min_y = HUD_h + d_size * 5 * velocity if HUD_h + d_size * 5 * velocity < screen_h // 2 - d_size else screen_h // 2 - d_size
max_y = screen_h - d_size * 5 * velocity if screen_h - d_size * 5 * velocity > screen_h // 2 + d_size else screen_h // 2 + d_size
rnd_x = random.randint(min_x, min_x)
rnd_y = random.randint(min_y, min_y)
rnd_char_dict = {0: 'n', 1: 's', 2: 'e', 3: 'w'}
direction = rnd_char_dict[random.randint(0, 3)] #north, s, e or w
direction = 'n'
# initial snake body
snake_body = [(rnd_x - rnd_x % d_tile_size, rnd_y - rnd_y % d_tile_size, direction)]


#TODO: Button Class
class Button():
    def __init__(self, x, y, image):
        self.coords = (x, y)
        self.image = image
        self.rect = pygame.Rect(x, y, image.get_width(), image.get_height())
    
    def draw(self):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouseget_pressed()[0] == 1:
                print("clicked button")