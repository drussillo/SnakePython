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
def handle_boulders() -> None:
    if g.current_state == g.Gamestate.FAIL:
        boulder_1.new_instance()
    else:
        boulder_1.draw()
        boulder_1.check_collision_w_head()
