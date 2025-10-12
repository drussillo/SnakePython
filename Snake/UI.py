import Global as g


def draw_HUD() -> None:
    HUD_field = g.pygame.Rect(0, 0, g.HUD_w, g.HUD_h) 
    g.pygame.draw.rect(g.SCREEN, (222,222,23), HUD_field)
    apple_icon_w, apple_icon_h = g.d_tile_size//1.5, g.d_tile_size//1.5
    apple_icon = g.pygame.transform.scale(g.defapple, (apple_icon_w, apple_icon_h))
    apple_icon_pos_x, apple_icon_pos_y = g.HUD_w//g.HUD_divisor, g.HUD_h // 2 - apple_icon.get_height()//2
    g.SCREEN.blit(apple_icon, (apple_icon_pos_x, apple_icon_pos_y))
    font = g.pygame.font.SysFont(None, apple_icon.get_width())
    apple_counter = font.render(f" x {len(g.snake_body) - 1}", True, (0,0,0))
    apple_counter_pos_x, apple_counter_pos_y = apple_icon_pos_x + apple_icon_w, apple_icon_pos_y + apple_icon_w//4
    g.SCREEN.blit(apple_counter, (apple_counter_pos_x, apple_counter_pos_y))

def draw_background() -> None:
    g.SCREEN.fill((110, 135, 97))
    for y, row in enumerate(g.background_arr):
        for x, bgimg in enumerate(row):
            g.SCREEN.blit(bgimg, (x * g.d_tile_size + g.offset_x, y * g.d_tile_size + g.HUD_h + g.offset_y))

def draw_fail_state_screen() -> None: #without buttons
    g.SCREEN.fill((110, 135, 97))
    font = g.pygame.font.SysFont(None, 100)
    fail_title = font.render('You Failed!', True, (56, 79, 93))
    fail_title_pos_x, fail_title_pos_y = g.get_middle_pos(fail_title.get_width(), fail_title.get_height())
    g.SCREEN.blit(fail_title, (fail_title_pos_x, fail_title_pos_y-200))
    # reset button
    button_1.set_image(g.retrybutton)
    button_1.center()
    button_1.move(y=200, x=150)
    button_1.draw(g.SCREEN)
    button_1.check_if_clicked(g.reset_mode_basic)
    # menu button
    button_2.set_image(g.menubutton)
    button_2.center()
    button_2.move(y=200, x=-150)
    button_2.draw(g.SCREEN)
    button_2.check_if_clicked(g.reset_menu)

def draw_main_menu_screen() -> None:
    g.SCREEN.fill((110, 135, 97))
    font = g.pygame.font.SysFont(None, 100)
    main_title = font.render('Snake Python', True, (56, 79, 93))
    main_title_pos_x, main_title_pos_y = g.get_middle_pos(main_title.get_width(), main_title.get_height())
    g.SCREEN.blit(main_title, (main_title_pos_x, main_title_pos_y-200))
    button_1.set_image(g.startbutton)
    button_1.center()
    button_1.move(y=200)
    button_1.draw(g.SCREEN)
    button_1.check_if_clicked(g.reset_mode_basic)

def draw_settings_menu_screen() -> None:
    g.SCREEN.fill((110, 135, 97))
    font = g.pygame.font.SysFont(None, 100)
    settings_title = font.render('Settings', True, (56, 79, 93))
    settings_rect = settings_title.get_rect()
    g.SCREEN.blit(settings_title, (settings_rect.x, settings_rect.y))
    button_1.set_image(g.emptybutton)
    button_1.center()
    button_1.move(y=200)
    button_1.draw(g.SCREEN)
    button_1.check_if_clicked(g.reset_mode_basic)


class Button():
    def __init__(self, x=0, y=0, w=0, h=0, drawable:g.pygame.surface.Surface=g.emptybutton) -> None:
        self.x = x
        self.y = y
        self.w = w if w > 0 else drawable.get_width()
        self.h = h if h > 0 else drawable.get_height()
        self.image = drawable
        self.rect = g.pygame.Rect(x, y, self.w, self.h)
        self.is_down = False

    def set_image(self, drawable:g.pygame.surface.Surface=g.defapple) -> None:
        self.w = drawable.get_width()
        self.h = drawable.get_height()
        self.image = drawable

    def center(self) -> None:
        self.x, self.y = g.get_middle_pos(self.w, self.h)

    def move(self, x=0, y=0) -> None:
        self.x += x
        self.y += y

    def resize(self, w=30, h=30) -> None:
        self.image = g.pygame.transform.scale(self.image, (w, h))

    def draw(self, surface:type(g.SCREEN)) -> None:
        surface.blit(self.image, (self.x, self.y))

    def check_if_clicked(self, function) -> None:
        if g.pygame.mouse.get_pressed(num_buttons=3)[0] and not self.is_down:
            mouse_x, mouse_y = g.pygame.mouse.get_pos()
            if self.x <= mouse_x <= self.x + self.w and self.y <= mouse_y <= self.y + self.h:
                function()
        self.is_down = g.pygame.mouse.get_pressed(num_buttons=3)[0]

#declare multiuse button objects
button_1 = Button()
button_2 = Button()

