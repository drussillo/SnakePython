import Global as g
import random



class Apple:
    def __init__(self):
        loop = True
        while loop:
            self.rnd_x = random.randint(0, 1280)
            self.rnd_y = random.randint(0, 720)
            loop = not self.valid_pos(rnd_x, rnd_y)    

        self.x_coord = rnd_x
        self.y_coord = rnd_y
        
    def valid_pos(x, y):
        for segment in g.snake_body:
            if segment[0] <= x <= segment[0]+25 and segment[1] <= y <= segment[1]:
                return False
                break
            else: return True

    def spawn(self):
        g.pygame.draw.rect(g.SCREEN, (200, 0, 0), g.pygame.Rect(self.x_coord, self.y_coord, 20, 20))
    