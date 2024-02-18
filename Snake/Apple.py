import Global as g
import Snake 
import random

class Apple: 
    def __init__(self):
        self.eaten = False 
        self.is_spawned = False
        loop = True
        while loop:
            rnd_x = random.randint(50, 1230)
            rnd_y = random.randint(150, 670)
            loop = not self.valid_pos(rnd_x, rnd_y)    
        self.x_coord = rnd_x - rnd_x % 25 
        self.y_coord = rnd_y - rnd_y % 25
        
    def valid_pos(self, x, y):
        for segment in g.snake_body:
            if segment[0] <= x <= segment[0]+25 and segment[1] <= y <= segment[1]:
                return False
                break
            else: return True
   
    def check_collision(self):
        rect1 = g.pygame.Rect(self.x_coord, self.y_coord, 20, 20)
        head_coordinate_x = g.snake_body[0][0]
        head_coordinate_y = g.snake_body[0][1]
        rect2 = g.pygame.Rect(head_coordinate_x,head_coordinate_y,20,20)

        collides = rect1.colliderect(rect2)
        if collides and not self.eaten:
            Snake.add_segment()
            self.eaten = True 
            self.despawn()
            print(f" apples: { len(g.snake_body) - 1 }")

    
    def despawn(self):
        g.pygame.draw.rect(g.SCREEN, (255,255,255),g.pygame.Rect(self.x_coord,self.y_coord,20,20))

    def spawn(self):
        g.pygame.draw.rect(g.SCREEN, (200, 0, 0), g.pygame.Rect(self.x_coord, self.y_coord, 20, 20))
        self.is_spawned