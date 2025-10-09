import Global as g
import Snake
from Object import Object
import random

class Boulder(Object):
    def __init__(self) -> None:
        super().__init__("./drawables/boulder.png")

    def apply_effect(self) -> None:
        Snake.die()

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
            print("HELLO")
            return False
        else:
            return super().valid_pos(x, y)


#handle obstacles
boulder_1 = Boulder()

def init_obstacles_basic() -> None:
    boulder_1.new_instance()
    print(boulder_1.valid_pos(650, 590))
    print(g.screen_w - g.offset_x - g.d_tile_size, g.screen_h-g.offset_y-2*g.d_tile_size)
    print(boulder_1.x_coord, boulder_1.y_coord)

def handle_obstacles() -> None:
    boulder_1.draw()
    boulder_1.check_collision_w_head()
