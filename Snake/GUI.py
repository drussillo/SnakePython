import Global as g

field = g.pygame.Rect(0, 0, 1280, 100) 
def draw():
    g.pygame.draw.rect(g.SCREEN, (222,222,23), field)