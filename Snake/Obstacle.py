import Global as g
import Snake
from Object import Object
import random

class Boulder(Object):
    def __init__(self) -> None:
        super().__init__("./drawables/boulder.png")

    def apply_effect(self) -> None:
        Snake.die()

#handle obstacles
boulder_1 = Boulder()

def init_obstacles_basic() -> None:
    boulder_1.new_instance()

def handle_obstacles() -> None:
    boulder_1.draw()
    boulder_1.check_collision_w_head()
