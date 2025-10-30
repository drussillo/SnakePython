import Global as g
import Sound


def draw() -> None:
    if len(g.snake_body) > 1:
        # Tail segment
        tail_coords:(int, int) = (g.snake_body[-1][0] + g.d_dist // 2, g.snake_body[-1][1] + g.d_dist // 2)
        match g.snake_body[-1][2]: # tail direction
            case 'n': g.SCREEN.blit(g.snakelast_n, tail_coords)
            case 's': g.SCREEN.blit(g.snakelast_s, tail_coords)
            case 'e': g.SCREEN.blit(g.snakelast_e, tail_coords)
            case 'w': g.SCREEN.blit(g.snakelast_w, tail_coords)
        # Center body
        for segment in reversed(g.snake_body[1:-1]): # exclude head and tail
            segm_coords:(int, int) = (segment[0] + g.d_dist // 2, segment[1] + g.d_dist // 2)
            match segment[2]: # segment direction
                case 'n' | 's': g.SCREEN.blit(g.snakesegment_vert, segm_coords)
                case 'e' | 'w': g.SCREEN.blit(g.snakesegment_hor, segm_coords)
    # Head 
    head_coords:(int, int) = (g.snake_body[0][0] + g.d_dist // 2, g.snake_body[0][1] + g.d_dist // 2) # top left of tile + dist
    match g.snake_body[0][2]:  # head direction
        case 'n': g.SCREEN.blit(g.snakehead_n, head_coords)
        case 's': g.SCREEN.blit(g.snakehead_s, head_coords)
        case 'e': g.SCREEN.blit(g.snakehead_e, head_coords)
        case 'w': g.SCREEN.blit(g.snakehead_w, head_coords)

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
    
def align_with_tile(x:int, y:int, current_direction:str, next_direction:str) -> (int, int):
    horizontal_offset = (x - g.offset_x) % g.d_tile_size
    vertical_offset = (y - g.HUD_h - g.offset_y) % g.d_tile_size
    match (current_direction, next_direction):
        case ('e', 'n') | ('e', 's'):
            if horizontal_offset > 0:
                return (x - horizontal_offset + g.d_tile_size, y)
            else:
                return (x, y)
        case ('w', 'n') | ('w', 's'):
            return (x - horizontal_offset, y)
        case ('n', 'e') | ('n', 'w'):
            return (x, y - vertical_offset)
        case ('s', 'e') | ('s', 'w'):
            if vertical_offset > 0:
                return (x, y - vertical_offset + g.d_tile_size)
            else:
                return (x, y)
        case _:
            print("Error: attempting to realign with invalid directions")
            return (0, 0)

# align_snake_if_turn
def head_align_if_turn() -> None:
    next_direction = g.direction
    if g.snake_body[0][2] != next_direction:
        for i in range(len(g.snake_body)): 
            current_x, current_y, current_direction = g.snake_body[i]
            if i > 0 and g.snake_body[i - 1][2] != current_direction:
                next_direction = g.snake_body[i - 1][2]

            if current_direction != next_direction:
                new_x, new_y = align_with_tile(current_x, current_y, current_direction, next_direction)
                g.snake_body[i] = (new_x, new_y, current_direction)

def follow_up_quick() -> None:
    head_aligned:bool = (
            (g.snake_body[0][0] - g.offset_x) % g.d_tile_size == 0 and 
            (g.snake_body[0][1] - g.offset_y - g.HUD_h) % g.d_tile_size == 0
    )
    if head_aligned:
        for i in range(len(g.snake_body)-1, 0, -1): #from tail to head, excluding the head
            set_segment_dir(i, g.snake_body[i - 1][2])
        # update head direction
        set_segment_dir(0, g.direction)

def follow_up_legacy() -> None:
    if (g.snake_body[0][0] - g.offset_x) % g.d_tile_size == 0 and (g.snake_body[0][1] - g.offset_y - g.HUD_h) % g.d_tile_size == 0:
        for current_index in range(len(g.snake_body)-1, 0, -1): #from tail to head, excluding the head
            next_segment_direction = g.snake_body[current_index-1][2]
            set_segment_dir(current_index, next_segment_direction)
        #set head to global direction
        set_segment_dir(0, g.direction)

def movement() -> None:
    if g.legacy_mode:
        follow_up_legacy()
        advance()
    else:
        head_align_if_turn()
        follow_up_quick()
        advance()

def check_if_fail() -> None:
    if check_if_coll_itself() or out_of_bounds():
        die()

def check_if_win() -> None:
    g.score = len(g.snake_body) - 1
    if g.score >= g.objective:
        win()

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

def lose_segments(amount:int=1) -> None:
    apple_amount = len(g.snake_body) - 1 
    if apple_amount == 0:
        die()
    elif amount >= apple_amount:
        g.snake_body = [g.snake_body[0]]
    else:
        g.snake_body = g.snake_body[:-amount]

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
    g.reset_fail()

def win() -> None:
    advance()
    Sound.stop()
    Sound.play(Sound.Type.SPAWN)
    while Sound.is_playing():
        continue
    g.reset_win()

