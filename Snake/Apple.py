import Global as g
import Snake 
import random

class Apple: 
    def __init__(self) -> None:
        self.eaten = False 
        loop = True
        while loop:
            rnd_x = random.randint(g.d_tile_size * 2, g.screen_w - g.d_tile_size * 2)
            rnd_y = random.randint(g.d_tile_size * 2, g.screen_h - g.d_tile_size * 3 - g.HUD_h)
            loop = not self.valid_pos(rnd_x + g.offset_x, rnd_y + g.offset_y + g.HUD_h)
        self.x_coord = rnd_x - rnd_x % g.d_tile_size + g.d_dist // 2 + g.offset_x
        self.y_coord = rnd_y - rnd_y % g.d_tile_size + g.d_dist // 2 + g.offset_y + g.HUD_h

    def valid_pos(self, x:int, y:int) -> bool:
        check_rect = g.pygame.Rect(x, y, g.d_tile_size, g.d_tile_size)
        for current_segment in g.snake_body:
            snake_segment_rect = g.pygame.Rect(current_segment[0], current_segment[1], g.d_tile_size, g.d_tile_size)
            if check_rect.colliderect(snake_segment_rect):
                return False
        return True

    def check_collision_w_head(self) -> None:
        apple_rect = g.pygame.Rect(self.x_coord, self.y_coord, g.d_size, g.d_size)
        head_rect = g.pygame.Rect(g.snake_body[0][0], g.snake_body[0][1], g.d_size, g.d_size)
        collides = apple_rect.colliderect(head_rect)
        if collides and not self.eaten:
            Snake.add_segment()
            self.eaten = True
            print(f" apples: { len(g.snake_body) - 1 }") #debug

    def draw(self) -> None:
        g.SCREEN.blit(g.defapple, (self.x_coord, self.y_coord))
        
    def new_apple(self) -> None:
        self.__init__()


#handle apples
apple_1 = Apple()
def handle_apples() -> None:
    if apple_1.eaten or (g.current_state == g.Gamestate.FAIL):
        apple_1.new_apple()
    else:
        apple_1.draw()
        apple_1.check_collision_w_head()
