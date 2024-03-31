import Global as g


def draw_HUD():
    HUD_field = g.pygame.Rect(0, 0, g.HUD_w, g.HUD_h) 
    g.pygame.draw.rect(g.SCREEN, (222,222,23), HUD_field)
    apple_icon_w, apple_icon_h = g.d_tile_size//1.5, g.d_tile_size//1.5
    apple_icon = g.pygame.transform.scale(g.defapple, (apple_icon_w, apple_icon_h))
    apple_icon_pos_x, apple_icon_pos_y = g.HUD_w//g.HUD_divisor, g.HUD_h // 2 - apple_icon.get_height()//2
    g.SCREEN.blit(apple_icon, (apple_icon_pos_x, apple_icon_pos_y))
    font = g.pygame.font.SysFont(None, apple_icon.get_width())
    apple_counter = font.render(f" x {len(g.snake_body)}", True, (0,0,0))
    apple_counter_pos_x, apple_counter_pos_y = apple_icon_pos_x + apple_icon_w, apple_icon_pos_y + apple_icon_w//4
    g.SCREEN.blit(apple_counter, (apple_counter_pos_x, apple_counter_pos_y))

def draw_background():
    for y, row in enumerate(g.background_arr):
        for x, bgimg in enumerate(row):
            g.SCREEN.blit(bgimg, (x * g.d_tile_size + g.offset_x, y * g.d_tile_size + g.HUD_h + g.offset_y))

def draw_fail_state_screen(): #without buttons
    g.SCREEN.fill((255, 255, 255))
    font = g.pygame.font.SysFont(None, 100)
    fail_title = font.render('You Failed!', True, (200, 0, 0))
    fail_title_pos_x, fail_title_pos_y = g.get_middle_pos(fail_title.get_width(), fail_title.get_height())
    g.SCREEN.blit(fail_title, (fail_title_pos_x, fail_title_pos_y-200))
    fail_button_1.center()
    fail_button_1.move(y=200)
    fail_button_1.draw(g.SCREEN)
    fail_button_1.check_if_clicked(g.reset)

class Button():
    def __init__(self, x=0, y=0, w=None, h=None, image_path="drawables/defaultapple.png"):
        self.x = x
        self.y = y
        img_obj = g.pygame.image.load(image_path)
        self.w = w if w != None else img_obj.get_width() * 4
        self.h = h if h != None else img_obj.get_height() * 4
        self.image = g.pygame.transform.scale(img_obj, (self.w, self.h))
        self.rect = g.pygame.Rect(x, y, self.w, self.h)
        self.is_down = False

    def center(self):
        self.x, self.y = g.get_middle_pos(self.w, self.h)

    def move(self, x=0, y=0):
        self.x += x
        self.y += y

    def resize(self, w=30, h=30):
        self.image = g.pygame.transform.scale(self.image, (w, h))

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

    def check_if_clicked(self, function):
        if g.pygame.mouse.get_pressed(num_buttons=3)[0] and not self.is_down:
            mouse_x, mouse_y = g.pygame.mouse.get_pos()
            if self.x <= mouse_x <= self.x + self.w and self.y <= mouse_y <= self.y + self.h:
                function()
        self.is_down = g.pygame.mouse.get_pressed(num_buttons=3)[0]

#declare button objects
fail_button_1 = Button(w=200, h=68.3, image_path="drawables/resetbutton.png")
