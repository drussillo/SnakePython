import Global as g

def draw():
    clear()
    move()
    for segment in g.snake_body:
        g.pygame.draw.rect(g.SCREEN, (0, 200, 0), g.pygame.Rect(segment[0], segment[1], 20, 20))

def move():
    for i, segment in enumerate(g.snake_body):
        if segment[2] == 'n':
            g.snake_body[i] = (segment[0], segment[1]-g.velocity, segment[2])
        elif segment[2] == 's':
            g.snake_body[i] = (segment[0], segment[1]+g.velocity, segment[2])
        elif segment[2] == 'e':
            g.snake_body[i] = (segment[0]+g.velocity, segment[1], segment[2])
        elif segment[2] == 'w':
            g.snake_body[i] = (segment[0]-g.velocity, segment[1], segment[2])
        

def clear():
    for segment in g.snake_body:
        g.pygame.draw.rect(g.SCREEN, (255, 255, 255), g.pygame.Rect(segment[0], segment[1], 20, 20))
        