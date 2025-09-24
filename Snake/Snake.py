import Global as g
import Sound

def draw() -> None:
    #Head first
    head_coords:(int, int) = (g.snake_body[0][0] + g.d_dist // 2, g.snake_body[0][1] + g.d_dist // 2) # top left of tile + dist
    match g.snake_body[0][2]:  # head direction
        case 'n': g.SCREEN.blit(g.snakehead_n, head_coords)
        case 's': g.SCREEN.blit(g.snakehead_s, head_coords)
        case 'e': g.SCREEN.blit(g.snakehead_e, head_coords)
        case 'w': g.SCREEN.blit(g.snakehead_w, head_coords)
    #Then center body
    if len(g.snake_body) > 1:
        for segment in g.snake_body[1:-1]: # exclude head and tail
            segm_coords:(int, int) = (segment[0] + g.d_dist // 2, segment[1] + g.d_dist // 2)
            match segment[2]: # segment direction
                case 'n' | 's': g.SCREEN.blit(g.snakesegment_vert, segm_coords)
                case 'e' | 'w': g.SCREEN.blit(g.snakesegment_hor, segm_coords)
        #Tail segment last
        tail_coords:(int, int) = (g.snake_body[-1][0] + g.d_dist // 2, g.snake_body[-1][1] + g.d_dist // 2)
        match g.snake_body[-1][2]: # tail direction
            case 'n': g.SCREEN.blit(g.snakelast_n, tail_coords)
            case 's': g.SCREEN.blit(g.snakelast_s, tail_coords)
            case 'e': g.SCREEN.blit(g.snakelast_e, tail_coords)
            case 'w': g.SCREEN.blit(g.snakelast_w, tail_coords)

def advance() -> None:
    for i, segment in enumerate(g.snake_body):
        match segment[2]:
            case 'n':
                g.snake_body[i] = (segment[0], segment[1] - g.velocity, segment[2])
            case 's':
                g.snake_body[i] = (segment[0], segment[1] + g.velocity, segment[2])
            case 'e':
                g.snake_body[i] = (segment[0] + g.velocity, segment[1], segment[2])
            case 'w':
                g.snake_body[i] = (segment[0] - g.velocity, segment[1], segment[2])
    

def head_update_direction_quick() -> None:
    head = g.snake_body[0]
    if g.direction != head[2]:  # direction currently being changed
        horizontal_offset = (head[0] - g.offset_x) % g.d_tile_size
        vertical_offset = (head[1] - g.HUD_h - g.offset_y) % g.d_tile_size
        # print(horizontal_offset, vertical_offset)
        match (head[2], g.direction):  # from, to
            case ('e', 'n') | ('e', 's'):
                if horizontal_offset < g.d_tile_size // 2 and horizontal_offset > 0:
                    print("early")
                    g.snake_body[0] = (head[0] - horizontal_offset, head[1], head[2])
                elif horizontal_offset > g.d_tile_size // 2:
                    print("late")
                    g.snake_body[0] = (head[0] - horizontal_offset + g.d_tile_size, head[1], head[2])
            case ('w', 'n') | ('w', 's'):
                if horizontal_offset > g.d_tile_size // 2:
                    print("early")
                    g.snake_body[0] = (head[0] - horizontal_offset + g.d_tile_size, head[1], head[2])
                elif horizontal_offset < g.d_tile_size // 2 and horizontal_offset > 0:
                    print("late")
                    g.snake_body[0] = (head[0] - horizontal_offset, head[1], head[2])
            case ('n', 'e') | ('n', 'w'):
                if vertical_offset > g.d_tile_size // 2 and vertical_offset < g.d_tile_size:
                    print("early")
                    g.snake_body[0] = (head[0], head[1] - vertical_offset + g.d_tile_size, head[2])
                elif vertical_offset < g.d_tile_size // 2:
                    print("late")
                    g.snake_body[0] = (head[0], head[1] - vertical_offset, head[2])
            case ('s', 'e') | ('s', 'w'):
                if vertical_offset < g.d_tile_size // 2:
                    print("early")
                    g.snake_body[0] = (head[0], head[1] - vertical_offset, head[2])
                elif vertical_offset > g.d_tile_size // 2 and vertical_offset < g.d_tile_size:
                    print("late")
                    g.snake_body[0] = (head[0], head[1] - vertical_offset + g.d_tile_size, head[2])

def follow_up_quick() -> None:
    # if head is aligned
    for i in range(len(g.snake_body)-1, 0, -1): #from tail to head, excluding the head
        current_x = g.snake_body[i][0]
        current_y = g.snake_body[i][1]
        current_direction = g.snake_body[i][2]
        next_direction = g.snake_body[i-1][2]
        next_segment_aligned:bool = (g.snake_body[i-1][0] - g.offset_x) % g.d_tile_size == 0 and (g.snake_body[i-1][1] - g.offset_y - g.HUD_h) % g.d_tile_size == 0
        if current_direction != next_direction and next_segment_aligned:
            horizontal_offset = (current_x - g.offset_x) % g.d_tile_size
            vertical_offset = (current_y - g.HUD_h - g.offset_y) % g.d_tile_size
            # print(g.direction, i, horizontal_offset, current_direction, vertical_offset, next_direction, len(g.snake_body))
            match (current_direction, next_direction):
                case ('e', 'n') | ('e', 's'):
                    if horizontal_offset < g.d_tile_size // 2 and horizontal_offset > 0:
                        print("early segment", i)
                        g.snake_body[i] = (current_x - horizontal_offset, current_y, current_direction)
                    elif horizontal_offset > g.d_tile_size // 2:
                        print("late segment", i)
                        g.snake_body[i] = (current_x - horizontal_offset + g.d_tile_size, current_y, current_direction)
                case ('w', 'n') | ('w', 's'):
                    if horizontal_offset > g.d_tile_size // 2:
                        print("early segment", i)
                        g.snake_body[i] = (current_x - horizontal_offset + g.d_tile_size, current_y, current_direction)
                    elif horizontal_offset < g.d_tile_size and horizontal_offset > 0:
                        print("late segment", i)
                        g.snake_body[i] = (current_x - horizontal_offset, current_y, current_direction)
                case ('n', 'e') | ('n', 'w'):
                    if vertical_offset > g.d_tile_size // 2:
                        print("early segment", i)
                        g.snake_body[i] = (current_x, current_y - vertical_offset + g.d_tile_size, current_direction)
                    elif vertical_offset < g.d_tile_size // 2 and vertical_offset > 0:
                        print("late segment", i)
                        g.snake_body[i] = (current_x, current_y - vertical_offset, current_direction)
                case ('s', 'e') | ('s', 'w'):
                    if vertical_offset < g.d_tile_size // 2 and vertical_offset > 0:
                        print("early segment", i)
                        g.snake_body[i] = (current_x, current_y - vertical_offset, current_direction)
                    elif vertical_offset > g.d_tile_size // 2:
                        print("late segment", i)
                        g.snake_body[i] = (current_x, current_y - vertical_offset + g.d_tile_size, current_direction)
            set_segment_dir(i, next_direction)
    # update head direction
    if (g.snake_body[0][0] - g.offset_x) % g.d_tile_size == 0 and (g.snake_body[0][1] - g.offset_y - g.HUD_h) % g.d_tile_size == 0:
        set_segment_dir(0, g.direction)

def movement() -> None:
    head_update_direction_quick()
    follow_up_quick()
    advance()
    # follow_up()

def set_segment_dir(index:int, direction:str) -> None:
    g.snake_body[index] = (g.snake_body[index][0], g.snake_body[index][1], direction)

def add_segment() -> None:
    Sound.play(Sound.Type.GROW)
    last_x, last_y, last_direction = g.snake_body[len(g.snake_body)-1]
    offset_dict = {
        'n': (0, g.d_tile_size),
        's': (0, -g.d_tile_size),
        'e': (-g.d_tile_size, 0),
        'w': (g.d_tile_size, 0)
        }
    offset_x, offset_y = offset_dict[last_direction]
    g.snake_body.append((last_x + offset_x, last_y + offset_y, last_direction))

def check_if_coll_itself() -> bool:
    head_rect = g.pygame.Rect(g.snake_body[0][0], g.snake_body[0][1], g.d_size, g.d_size)
    for current_segment in g.snake_body[3:]:
        current_segment_rect = g.pygame.Rect(current_segment[0], current_segment[1], g.d_tile_size, g.d_tile_size)
        if head_rect.colliderect(current_segment_rect):
            return True
    return False

def out_of_bounds() -> bool:
    head_x, head_y, _ = g.snake_body[0]
    check_sides_list = [
        head_y < g.HUD_h + g.offset_y,
        head_y > g.screen_h - g.d_size - g.offset_y,
        head_x > g.screen_w - g.d_size - g.offset_x,
        head_x < g.offset_x
        ]
    return any(check_sides_list)

def die() -> None:
    advance()
    Sound.stop()
    Sound.play(Sound.Type.DEATH)
    while Sound.is_playing():
        continue
    g.current_state = g.Gamestate.FAIL
