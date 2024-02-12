import pygame

SCREEN = pygame.display.set_mode([1280, 720])
velocity = 1
direction = 'e' #north, s, e or w
clock = pygame.time.Clock()
snake_body = [(100, 100, 'e'), (75, 100, 'e'), (50, 100, 'e'), (25, 100, 'e'), (0, 100, 'e')]  # Example initial snake body

def setBody(n, x, y, d):
    for i, segment in enumerate(snake_body):
        if n == i:
            snake_body[n] = (x, y, d)
            
def setBodDir(n, d):
    setBody(n, snake_body[n][0], snake_body[n][1], d)