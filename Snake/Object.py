import Global as g
import random

from typing import Self

class Object:
    def __init__(self, drawable:g.pygame.surface.Surface=g.defapple, width:int=g.d_size, height:int=g.d_size) -> None:
        # set drawable
        self.drawable:g.pygame.surface.Surface = drawable
        # set width and height
        self.width = width
        self.height = height
        # set posx and posy
        loop = True
        while loop:
            rnd_x = random.randint(0, g.screen_w - 2 * g.offset_x - 1)
            rnd_x -= rnd_x % g.d_tile_size
            rnd_x += g.offset_x
            rnd_y = random.randint(0, g.screen_h - 2 * g.offset_y - g.HUD_h - 1)
            rnd_y -= rnd_y % g.d_tile_size
            rnd_y += g.offset_y + g.HUD_h
            loop = not self.valid_pos(rnd_x, rnd_y)
        self.x_coord = rnd_x
        self.y_coord = rnd_y

    def valid_pos(self, x:int, y:int) -> bool:
        head_x:int = g.snake_body[0][0]
        head_y:int = g.snake_body[0][1]
        head_direction:str = g.snake_body[0][2]
        distance_from_head:int = g.d_tile_size * 4

        # check if in front of head (current direction)
        valid:bool = True
        match(g.direction):
            case 'n':
                valid = not (y <= head_y and y >= head_y - distance_from_head)
            case 's':
                valid = not (y >= head_y and y <= head_y + distance_from_head)
            case 'e':
                valid = not (x >= head_x and x <= head_x + distance_from_head)
            case 'w':
                valid = not (x <= head_x and x >= head_x - distance_from_head)
        if valid:
            # check if tile is occupied
            new_rect = g.pygame.Rect(x, y, g.d_tile_size, g.d_tile_size)
            for segment in g.snake_body:
                segment_rect = g.pygame.Rect(segment[0], segment[1], g.d_tile_size, g.d_tile_size)
                if new_rect.colliderect(segment_rect):
                    return False
            for obj in g.object_stack:
                object_rect = g.pygame.Rect(obj.x_coord, obj.y_coord, g.d_tile_size, g.d_tile_size)
                if new_rect.colliderect(object_rect):
                    return False
        return valid

    def check_collision_w_head(self) -> None:
        object_rect = g.pygame.Rect(self.x_coord, self.y_coord, g.d_size, g.d_size)
        head_rect = g.pygame.Rect(g.snake_body[0][0], g.snake_body[0][1], g.d_size, g.d_size)
        collides = object_rect.colliderect(head_rect)
        if collides:
            self.apply_effect()
        else:
            self.not_on_head()

    def handle_self(self) -> None:
        pass
        # insert handling in override function

    def apply_effect(self) -> None:
        pass
        # insert effect in override function

    def not_on_head(self) -> None:
        pass
        # insert what to do when not on head in override function

    def draw(self) -> None:
        g.SCREEN.blit(self.drawable, (self.x_coord, self.y_coord))
        
    def new_instance(self) -> Self:
        self.__init__()
        return self

    def add_to_stack(self) -> Self:
        g.object_stack.append(self)
        return self

    def remove_from_stack(self) -> None:
        g.object_stack.remove(self)

def handle_objects() -> None:
    for obj in g.object_stack:
        obj.handle_self()


