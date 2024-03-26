import Global as g

def draw():
    #Head first
    head_coords = (g.snake_body[0][0]  + g.d_dist // 2, g.snake_body[0][1] + g.d_dist // 2)
    if g.snake_body[0][2] == 'n': g.SCREEN.blit(g.snakehead_n, head_coords)
    if g.snake_body[0][2] == 's': g.SCREEN.blit(g.snakehead_s, head_coords)
    if g.snake_body[0][2] == 'e': g.SCREEN.blit(g.snakehead_e, head_coords)
    if g.snake_body[0][2] == 'w': g.SCREEN.blit(g.snakehead_w, head_coords)
    #Then center body
    if len(g.snake_body) > 1:
        for segment in g.snake_body[1:-1]:
            segm_coords = (segment[0] + g.d_dist // 2, segment[1] + g.d_dist // 2)
            if segment[2] == 'n' or segment[2] == 's': g.SCREEN.blit(g.snakesegment_vert, segm_coords)
            else: g.SCREEN.blit(g.snakesegment_hor, segm_coords)
        #Tail segment last
        tail_coords = (g.snake_body[-1][0] + g.d_dist // 2, g.snake_body[-1][1] + g.d_dist // 2)
        if g.snake_body[-1][2] == 'n': g.SCREEN.blit(g.snakelast_n, tail_coords)
        elif g.snake_body[-1][2] == 's': g.SCREEN.blit(g.snakelast_s, tail_coords)
        elif g.snake_body[-1][2] == 'e': g.SCREEN.blit(g.snakelast_e, tail_coords)
        elif g.snake_body[-1][2] == 'w': g.SCREEN.blit(g.snakelast_w, tail_coords)

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

def follow_up():
    if (g.snake_body[0][0] - g.offset_x) % g.d_tile_size == 0 and (g.snake_body[0][1] - g.offset_y - g.HUD_h) % g.d_tile_size == 0:
        for current_index in range(len(g.snake_body)-1, 0, -1): #from tail to head, excluding the head
            next_segment_direction = g.snake_body[current_index-1][2]
            set_segment_dir(current_index, next_segment_direction)
        #set head to global direction
        set_segment_dir(0, g.direction)
        
def set_segment_dir(index, direction):
    g.snake_body[index] = (g.snake_body[index][0], g.snake_body[index][1], direction)

def add_segment():
    last_x, last_y, last_direction = g.snake_body[len(g.snake_body)-1]
    offset_dict = {
        'n': (0, g.d_tile_size),
        's': (0, -g.d_tile_size),
        'e': (-g.d_tile_size, 0),
        'w': (g.d_tile_size, 0)
        }
    offset_x, offset_y = offset_dict[last_direction]
    g.snake_body.append((last_x + offset_x, last_y + offset_y, last_direction))

def check_if_coll_itself():
    head_rect = g.pygame.Rect(g.snake_body[0][0], g.snake_body[0][1], g.d_size, g.d_size)
    if len(g.snake_body) > 2:
        collides_with_head_list = [head_rect.colliderect(g.pygame.Rect(segment[0], segment[1], g.d_size, g.d_size)) for segment in g.snake_body[2:]]
        return any(collides_with_head_list)
    else: 
        return False

def out_of_bounds():
    head_x, head_y, _ = g.snake_body[0]
    check_sides_list = [
        head_y < g.HUD_h + g.offset_y,
        head_y > g.screen_h - g.d_size - g.offset_y,
        head_x > g.screen_w - g.d_size - g.offset_x,
        head_x < g.offset_x
        ]
    return any(check_sides_list)