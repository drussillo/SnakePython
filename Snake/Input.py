import Global as g

def handle_input():
    for event in g.pygame.event.get():
        if event.type == g.pygame.QUIT:
            return False
        elif event.type == g.pygame.KEYDOWN:
            if event.key == g.pygame.K_ESCAPE:
                return False
            elif event.key == g.pygame.K_w:
                g.direction = 'n'
            elif event.key == g.pygame.K_s:
                g.direction = 's'
            elif event.key == g.pygame.K_d:
                g.direction = 'e'
            elif event.key == g.pygame.K_a:
                g.direction = 'w'
    return True