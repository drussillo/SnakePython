import Global as g
frame_count = 0

def draw():
    move()
    head_rect = g.pygame.Rect(g.snake_body[0][0], g.snake_body[0][1], 25, 25)
    if g.snake_body[0][2] == 'n': g.SCREEN.blit(g.snakehead_n, head_rect.topleft)
    if g.snake_body[0][2] == 's': g.SCREEN.blit(g.snakehead_s, head_rect.topleft)
    if g.snake_body[0][2] == 'e': g.SCREEN.blit(g.snakehead_e, head_rect.topleft)
    if g.snake_body[0][2] == 'w': g.SCREEN.blit(g.snakehead_w, head_rect.topleft)

    if len(g.snake_body) > 1:
        for segment in g.snake_body[1:-1]:
            segm_rect = g.pygame.Rect(segment[0], segment[1], 25, 25)
            if segment[2] == 'n' or segment[2] == 's': g.SCREEN.blit(g.snakesegment_vert, segm_rect.topleft)
            else: g.SCREEN.blit(g.snakesegment_hor, segm_rect.topleft)

        last_rect = g.pygame.Rect(g.snake_body[-1][0], g.snake_body[-1][1], 25, 25)
        if g.snake_body[-1][2] == 'n': g.SCREEN.blit(g.snakelast_n, last_rect.topleft)
        elif g.snake_body[-1][2] == 's': g.SCREEN.blit(g.snakelast_s, last_rect.topleft)
        elif g.snake_body[-1][2] == 'e': g.SCREEN.blit(g.snakelast_e, last_rect.topleft)
        elif g.snake_body[-1][2] == 'w': g.SCREEN.blit(g.snakelast_w, last_rect.topleft)

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

    #handle tail follow-up        
    global frame_count
    frame_count += 1
    if frame_count == 30 / g.velocity:
        frame_count = 0
        for i in range(len(g.snake_body)-1, 0, -1):
            fwd_segment_direction = g.snake_body[i-1][2]
            g.setBodDir(i, fwd_segment_direction)
        g.setBodDir(0, g.direction)
        
def add_segment():
    last_x, last_y, last_direction = g.snake_body[len(g.snake_body)-1]
    offset_dict = {'n': (0,30), 's': (0, -30), 'e': (-30, 0), 'w': (30, 0)}
    offset_x, offset_y = offset_dict[last_direction]
    g.snake_body.append((last_x + offset_x, last_y + offset_y, last_direction))
    
def check_if_coll_itself():
    head_rect = g.pygame.Rect(g.snake_body[0][0], g.snake_body[0][1], 25, 25)
    if len(g.snake_body) > 2:
        temp_rect = [not head_rect.colliderect(g.pygame.Rect(segment[0], segment[1], 25, 25)) for segment in g.snake_body[2:]]
        return not all(temp_rect)
    else: return False
    
def out_of_bounds():
    head_coords = (g.snake_body[0][0], g.snake_body[0][1])
    if head_coords[1] < 100: return True
    elif head_coords[1] > 700: return True
    elif head_coords[0] > 1260: return True
    elif head_coords[0] < 0: return True
    else: return False