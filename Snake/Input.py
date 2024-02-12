import Global as g

clock = g.pygame.time.Clock()

def handle_input():
    for event in g.pygame.event.get():
        if event.type == g.pygame.QUIT:
            return False
        elif event.type == g.pygame.KEYDOWN:
            if event.key == g.pygame.K_ESCAPE:
                return False
            elif event.key == g.pygame.K_w:
                g.direction = 'n'
                g.setBodDir(0, 'n')
            elif event.key == g.pygame.K_s:
                g.direction = 's'
                g.setBodDir(0, 's')
            elif event.key == g.pygame.K_d:
                g.direction = 'e'
                g.setBodDir(0, 'e')
            elif event.key == g.pygame.K_a:
                g.direction = 'w'
                g.setBodDir(0, 'w')
     

    # TODO every 25 frames, update segment direction to following segment's direction
    # this code is not functional rn
    frame_count += 1
    if frame_count % 25 == 0:
        frame_intervall += 1
        g.setBodDir(frame_intervall, g.direction)

    return True


'''
    for i in range(1, len(g.snake_body)):
        if g.direction == 'n' or g.direction == 's':
            if g.snake_body[i][0] == g.snake_body[i-1][0]:
                g.setBodDir(i, g.direction)
        elif g.direction == 'e' or g.direction == 'w':
            if g.snake_body[i][1] == g.snake_body[i-1][1]:
                g.setBodDir(i, g.direction)
'''