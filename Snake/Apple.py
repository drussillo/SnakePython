import Global as g
import Snake 
from Object import Object

class Apple(Object):
    def __init__(self) -> None:
        self.eaten = False 
        super().__init__("./drawables/defaultapple.png")

    def apply_effect(self) -> None:
        if not self.eaten:
            Snake.add_segment()
            self.eaten = True
            print(f" apples: { len(g.snake_body) - 1 }") #debug

#handle apples
apple_1 = Apple()
def handle_apples() -> None:
    if apple_1.eaten or (g.current_state == g.Gamestate.FAIL):
        apple_1.new_instance()
    else:
        apple_1.draw()
        apple_1.check_collision_w_head()
