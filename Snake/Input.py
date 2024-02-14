import Global as g
import Snake

clock = g.pygame.time.Clock()
frame_count = 0
frame_shift = 0

def handle_input():
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
                Snake.add_segment()

    global frame_count
    frame_count += 1
    if frame_count == 25:
        frame_count = 0
        for i in range(len(g.snake_body)-1, 0, -1):
            fwd_segment_direction = g.snake_body[i-1][2]
            g.setBodDir(i, fwd_segment_direction)
        g.setBodDir(0, g.direction)        

    return True