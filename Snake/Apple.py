import Global as g
import random



class Apple:
    def __init__(self, x_coord, y_coord):
        self.x_coord = random.randint(0, 1280)
        self.y_coord = random.randint(0, 720)    

    def spawn(self):
        g.pygame.draw.rect(g.SCREEN, (200, 0, 0), g.pygame.Rect(self.x_coord, self.y_coord, 20, 20))
        