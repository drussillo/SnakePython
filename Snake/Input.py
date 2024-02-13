from pickle import FRAME
from tkinter import CURRENT
import Global as g

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
                g.direction = 'n'
            elif event.key == g.pygame.K_s:
                g.direction = 's'
            elif event.key == g.pygame.K_d:
                g.direction = 'e'
            elif event.key == g.pygame.K_a:
                g.direction = 'w'

    global frame_count
    global frame_shift
    
    frame_count += 1
    if frame_count == 25:
        frame_count = 0
        

        if frame_shift == 0:
            g.setBodDir(0, g.direction)
        else:
            current_segment_x = g.snake_body[frame_shift][0]
            current_segment_y = g.snake_body[frame_shift][1]
            fwd_segment_direction = g.snake_body[frame_shift-1][2]
            g.snake_body[frame_shift] = (current_segment_x, current_segment_y, fwd_segment_direction)
        
        frame_shift += 1
    if frame_shift == len(g.snake_body):
            frame_shift = 0

    return True