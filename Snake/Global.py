import pygame
import random

SCREEN = pygame.display.set_mode([1280, 720])
velocity = 2 #can only be 1, 2 or 3
clock = pygame.time.Clock()
failstate = False

#start drawables
snakesegment_hor = pygame.image.load("snake/imgs/snakesegment.png")
snakesegment_vert = pygame.transform.rotate(snakesegment_hor, 90)

snakehead_n = pygame.image.load("snake/imgs/dipre.jpg")
snakehead_n = pygame.transform.scale(snakehead_n, (25, 25))
snakehead_e = pygame.transform.rotate(snakehead_n, -90)
snakehead_s = pygame.transform.rotate(snakehead_e, -90)
snakehead_w = pygame.transform.rotate(snakehead_s, -90)

snakelast_w = pygame.image.load("snake/imgs/snakesegmentlast.png")
snakelast_n = pygame.transform.rotate(snakelast_w, -90)
snakelast_e = pygame.transform.rotate(snakelast_n, -90)
snakelast_s = pygame.transform.rotate(snakelast_e, -90)

defapple = pygame.image.load("snake/imgs/defaultapple.jpg")
defapple = pygame.transform.scale(defapple, (25, 25))
#end drawables

rnd_x = random.randint(250, 1130) 
rnd_y = random.randint(250, 570)
rnd_char_dict = {0: 'n', 1: 's', 2: 'e', 3: 'w'}
direction = rnd_char_dict[random.randint(0, 3)] #north, s, e or w


snake_body = [(rnd_x - rnd_x%30, rnd_y - rnd_y%30, direction)]  # Example initial snake body


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


def setBody(n, x, y, d):
    for i, segment in enumerate(snake_body):
        if n == i:
            snake_body[n] = (x, y, d)
            
def setBodDir(n, d):
    setBody(n, snake_body[n][0], snake_body[n][1], d)