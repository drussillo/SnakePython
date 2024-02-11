import Global as g

def draw():
    clear(g.snake_body)
    move()
    for segment in g.snake_body:
        g.pygame.draw.rect(g.SCREEN, (0, 200, 0), g.pygame.Rect(segment[0], segment[1], 20, 20))

def move():
    
    dirChngd = False
    for i, segment in enumerate(g.snake_body):
       
        if g.direction == 'n':
            g.snake_body[i] = (segment[0], segment[1]-g.velocity)
        elif g.direction == 's':
            g.snake_body[i] = (segment[0], segment[1]+g.velocity)
        elif g.direction == 'e':
            g.snake_body[i] = (segment[0]+g.velocity, segment[1])
        elif g.direction == 'w':
            g.snake_body[i] = (segment[0]-g.velocity, segment[1])
        

def clear(body):
    for segment in body:
        g.pygame.draw.rect(g.SCREEN, (255, 255, 255), g.pygame.Rect(segment[0], segment[1], 20, 20))
        