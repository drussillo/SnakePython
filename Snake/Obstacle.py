import Global as g
import Snake
from Object import Object
import random

class StaticObstacle(Object):
    def __init__(self, drawable:g.pygame.surface.Surface=g.defapple) -> None:
        super().__init__(drawable)

    def valid_pos(self, x:int, y:int) -> bool:
        if (
            # first, second, second-to-last, and last columns
            x == g.offset_x and 
            (y == g.offset_y + g.HUD_h + g.d_tile_size or y == g.screen_h - g.offset_y - 2 * g.d_tile_size) 
            or
            x == g.offset_x + g.d_tile_size and 
            (y == g.offset_y + g.HUD_h or y == g.screen_h - g.offset_y - g.d_tile_size) 
            or
            x == g.screen_w - g.offset_x - 2 * g.d_tile_size and 
            (y == g.offset_y + g.HUD_h or y == g.screen_h - g.offset_y - g.d_tile_size) 
            or
            x == g.screen_w - g.offset_x - g.d_tile_size and 
            (y == g.offset_y + g.HUD_h + g.d_tile_size or y == g.screen_h - g.offset_y - 2 * g.d_tile_size)
        ):
            return False
        else:
            return super().valid_pos(x, y)

    def apply_effect(self) -> None:
        pass
        # insert effect in override function

    def handle_self(self) -> None:
        self.draw()
        self.check_collision_w_head()

class Boulder(StaticObstacle):
    def __init__(self) -> None:
        super().__init__(drawable=g.boulder)

    def apply_effect(self) -> None:
        Snake.die()

class Cactus(StaticObstacle):
    def __init__(self) -> None:
        super().__init__(drawable=g.cactus)

    def apply_effect(self) -> None:
        if len(g.snake_body) > 1:
            Snake.lose_segment()
            # TODO: Limit segment loss to 1 per cactus hit
            # TODO: Add cactus hit sound

#handle obstacles
boulder_1 = Boulder()
cactus_1 = Cactus()

def init_obstacles_basic() -> None:
    boulder_1.new_instance().add_to_stack()
    cactus_1.new_instance().add_to_stack()

