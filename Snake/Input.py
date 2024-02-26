import Global as g
import Snake
import HUD

def handle_input_main():
    for event in g.pygame.event.get():
        if event.type == g.pygame.QUIT:
            return False
        elif event.type == g.pygame.KEYDOWN:
            if event.key == g.pygame.K_ESCAPE:
                return False
            elif event.key == g.pygame.K_w:
                g.direction = 'n' if g.snake_body[0][2] != 's' else 's'
            elif event.key == g.pygame.K_s:
                g.direction = 's' if g.snake_body[0][2] != 'n' else 'n'
            elif event.key == g.pygame.K_d:
                g.direction = 'e' if g.snake_body[0][2] != 'w' else 'w'
            elif event.key == g.pygame.K_a:
                g.direction = 'w' if g.snake_body[0][2] != 'e' else 'e'
            elif event.key == g.pygame.K_t:
                #test key
                Snake.add_segment() #lenghten snake
        #elif event.type == g.pygame.MOUSEBUTTONDOWN and event.button == 1:#
    return True
            
def handle_input_fail():
    for event in g.pygame.event.get():
        if event.type == g.pygame.QUIT:
            return False
        elif event.type == g.pygame.KEYDOWN:
            if event.key == g.pygame.K_ESCAPE:
                return False

    return True