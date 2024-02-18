import pygame
import random

SCREEN = pygame.display.set_mode([1280, 720])
velocity = 1
clock = pygame.time.Clock()

rnd_x = random.randint(100, 1180) 
rnd_y = random.randint(100, 620)
rnd_char_dict = {0: 'n', 1: 's', 2: 'e', 3: 'w'}
direction = rnd_char_dict[random.randint(0, 3)] #north, s, e or w


snake_body = [(rnd_x - rnd_x%25, rnd_y - rnd_y%25, direction)]  # Example initial snake body

def setBody(n, x, y, d):
    for i, segment in enumerate(snake_body):
        if n == i:
            snake_body[n] = (x, y, d)
            
def setBodDir(n, d):
    setBody(n, snake_body[n][0], snake_body[n][1], d)