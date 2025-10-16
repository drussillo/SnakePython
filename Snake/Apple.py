import Global as g
import Snake 
from Object import Object

class Apple(Object):
    def __init__(self) -> None:
        self.eaten = False 
        super().__init__(g.defapple)

    def apply_effect(self) -> None:
        if not self.eaten:
            Snake.add_segment()
            print(f" apples: { len(g.snake_body) - 1 }") #debug
            self.new_instance()

    def handle_self(self) -> None:
        if self.eaten:
            self.remove_from_stack()
            self.new_instance()
        else:
            self.draw()
            self.check_collision_w_head()

#handle apples
apple_1 = Apple()

def init_apples_basic() -> None:
    apple_1.new_instance()
    apple_1.add_to_stack()

