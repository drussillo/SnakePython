import Global as g

field = g.pygame.Rect(0, 0, g.HUD_w, g.HUD_h) 
def draw():
    g.pygame.draw.rect(g.SCREEN, (222,222,23), field)