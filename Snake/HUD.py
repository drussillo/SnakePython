import Global as g

field = g.pygame.Rect(0, 0, g.HUD_w, g.HUD_h) 
def draw():
    g.pygame.draw.rect(g.SCREEN, (222,222,23), field)

def draw_fail_state_screen(): #without buttons
    g.SCREEN.fill((255, 255, 255))
    font = g.pygame.font.SysFont(None, 100)
    img = font.render('You Failed!', True, (200, 0, 0))
    g.SCREEN.blit(img, (420, 260))

#TODO: Button Class
class Button():
    def __init__(self, x, y, w, h, image_path):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.image = g.pygame.transform.scale(g.pygame.image.load(image_path), (w, h))
        self.rect = g.pygame.Rect(x, y, w, h)
        self.is_down = False

    def center(self):
        self.x, self.y = g.get_middle_pos(self.w, self.h)

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

    def check_if_clicked(self):
        if g.pygame.mouse.get_pressed(num_buttons=3)[0] and not self.is_down:
            mouse_x, mouse_y = g.pygame.mouse.get_pos()
            if self.x <= mouse_x <= self.x + self.w and self.y <= mouse_y <= self.y + self.h:
                print("Button clicked!")
        self.is_down = g.pygame.mouse.get_pressed(num_buttons=3)[0]