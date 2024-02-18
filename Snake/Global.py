import pygame
import random

SCREEN = pygame.display.set_mode([1280, 720])
velocity = 1
clock = pygame.time.Clock()
failstate = False

rnd_x = random.randint(200, 1180) 
rnd_y = random.randint(200, 620)
rnd_char_dict = {0: 'n', 1: 's', 2: 'e', 3: 'w'}
direction = rnd_char_dict[random.randint(0, 3)] #north, s, e or w


snake_body = [(rnd_x - rnd_x%25, rnd_y - rnd_y%25, direction)]  # Example initial snake body


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