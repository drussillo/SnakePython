import Global as g
import Snake
from Object import Object
import random

class Boulder(Object):
    def __init__(self) -> None:
        super().__init__(g.boulder)

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
        Snake.die()

    def handle_self(self) -> None:
        self.draw()
        self.check_collision_w_head()

#handle obstacles
boulder_1 = Boulder()

def init_obstacles_basic() -> None:
    boulder_1.new_instance()
    boulder_1.add_to_stack()

