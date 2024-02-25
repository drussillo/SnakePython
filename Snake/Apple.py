import Global as g
import Snake 
import random

class Apple: 
    def __init__(self):
        self.eaten = False 
        self.is_spawned = False
        loop = True
        while loop:
            rnd_x = random.randint(g.d_tile_size * 2, g.screen_w - g.d_tile_size * 2)
            rnd_y = random.randint(g.HUD_h + g.d_tile_size * 2, g.screen_h - g.d_tile_size * 2)
            loop = not self.valid_pos(rnd_x, rnd_y)    
        self.x_coord = rnd_x - rnd_x % g.d_tile_size
        self.y_coord = rnd_y - rnd_y % g.d_tile_size
        
    def valid_pos(self, x, y):
        validity = [not(segment[0] <= x <= segment[0]+g.d_tile_size and segment[1] <= y <= segment[1]+g.d_tile_size) for segment in g.snake_body]
        return all(validity)
   
    def check_collision_w_head(self):
        apple_rect = g.pygame.Rect(self.x_coord, self.y_coord, g.d_size, g.d_size)
        head_rect = g.pygame.Rect(g.snake_body[0][0], g.snake_body[0][1], g.d_size, g.d_size)
        collides = apple_rect.colliderect(head_rect)
        if collides and not self.eaten:
            Snake.add_segment()
            self.eaten = True
            print(f" apples: { len(g.snake_body) - 1 }") #debug

    def spawn(self):
        g.SCREEN.blit(g.defapple, (self.x_coord, self.y_coord))