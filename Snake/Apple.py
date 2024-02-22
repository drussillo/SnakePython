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
        self.x_coord = rnd_x - rnd_x % 30 
        self.y_coord = rnd_y - rnd_y % 30
        
    def valid_pos(self, x, y):
        validity = [not(segment[0] <= x <= segment[0]+30 and segment[1] <= y <= segment[1]+30) for segment in g.snake_body]
        return all(validity)
   
    def check_collision(self):
        rect1 = g.pygame.Rect(self.x_coord, self.y_coord, 25, 25)
        head_coordinate_x = g.snake_body[0][0]
        head_coordinate_y = g.snake_body[0][1]
        rect2 = g.pygame.Rect(head_coordinate_x,head_coordinate_y,25,25)

        collides = rect1.colliderect(rect2)
        if collides and not self.eaten:
            Snake.add_segment()
            self.eaten = True 
            print(f" apples: { len(g.snake_body) - 1 }")

    
    def despawn(self):
        g.pygame.draw.rect(g.SCREEN, (255,255,255),g.pygame.Rect(self.x_coord,self.y_coord,25,25))

    def spawn(self):
        apple_rect = g.pygame.Rect(self.x_coord, self.y_coord, 25, 25)
        g.SCREEN.blit(g.defapple, apple_rect.topleft)