import Global as g
import random

class Object:
    def __init__(self, drawable_path:str="", width:int=g.d_size, height:int=g.d_size) -> None:
        # set drawable
        self.drawable:g.pygame.surface.Surface = g.defapple
        if drawable_path:
            self.drawable = g.pygame.image.load("drawables/defaultapple.png")
            self.drawable = g.pygame.transform.scale(self.drawable, (width, height))
        # set width and height
        self.width = width
        self.height = height
        # set posx and posy
        loop = True
        while loop:
            rnd_x = random.randint(g.d_tile_size * 2, g.screen_w - g.d_tile_size * 2)
            rnd_y = random.randint(g.d_tile_size * 2, g.screen_h - g.d_tile_size * 3 - g.HUD_h)
            loop = not self.valid_pos(rnd_x + g.offset_x, rnd_y + g.offset_y + g.HUD_h)
        self.x_coord = rnd_x - rnd_x % g.d_tile_size + g.d_dist // 2 + g.offset_x
        self.y_coord = rnd_y - rnd_y % g.d_tile_size + g.d_dist // 2 + g.offset_y + g.HUD_h

    def valid_pos(self, x:int, y:int) -> bool:
        # TODO:
        # make area around snake illegal
        # check if inside other object
        check_rect = g.pygame.Rect(x, y, self.width, self.height)
        for current_segment in g.snake_body:
            snake_segment_rect = g.pygame.Rect(current_segment[0], current_segment[1], g.d_tile_size, g.d_tile_size)
            if check_rect.colliderect(snake_segment_rect):
                return False
        return True

    def check_collision_w_head(self) -> None:
        object_rect = g.pygame.Rect(self.x_coord, self.y_coord, g.d_size, g.d_size)
        head_rect = g.pygame.Rect(g.snake_body[0][0], g.snake_body[0][1], g.d_size, g.d_size)
        collides = object_rect.colliderect(head_rect)
        if collides:
            self.apply_effect()

    def apply_effect(self) -> None:
        pass
        # insert effect in override function

    def draw(self) -> None:
        g.SCREEN.blit(self.drawable, (self.x_coord, self.y_coord))
        
    def new_instance(self) -> None:
        self.__init__()
