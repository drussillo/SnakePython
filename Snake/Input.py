import Global as g
import Snake

def handle_input_main() -> bool:
    for event in g.pygame.event.get():
        if event.type == g.pygame.QUIT:
            return False
    #key down events
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
    #key up events
        elif event.type == g.pygame.KEYUP:
            if event.key == g.pygame.K_SPACE:
                g.velocity = g.velocity_start
    #other events
    if (g.pygame.key.get_pressed()[g.pygame.K_SPACE] and
        g.velocity != g.velocity_start * 2 and
        (g.snake_body[0][0] - g.offset_x) % (g.velocity * 2) == 0 and
        (g.snake_body[0][1] - g.offset_y - g.HUD_h) % (g.velocity * 2) == 0):
        g.velocity *= 2
        
    return True
            
def handle_input_fail() -> bool:
    for event in g.pygame.event.get():
        if event.type == g.pygame.QUIT:
            return False
        elif event.type == g.pygame.KEYDOWN:
            if event.key == g.pygame.K_ESCAPE:
                return False
            if event.key == g.pygame.K_r:
                g.reset()

    return True
