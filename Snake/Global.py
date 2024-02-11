import pygame

SCREEN = pygame.display.set_mode([1280, 720])
velocity = 1
direction = 'e' #north, s, e or w
clock = pygame.time.Clock()
snake_body = [(100, 100), (75, 100), (50, 100)]  # Example initial snake body