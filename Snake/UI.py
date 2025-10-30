import Global as g

def draw_HUD() -> None:
    HUD_field = g.pygame.Rect(0, 0, g.HUD_w, g.HUD_h) 
    g.pygame.draw.rect(g.SCREEN, (222,222,23), HUD_field)
    apple_icon_w, apple_icon_h = g.d_tile_size//1.5, g.d_tile_size//1.5
    apple_icon = g.pygame.transform.scale(g.defapple, (apple_icon_w, apple_icon_h))
    apple_icon_pos_x, apple_icon_pos_y = g.HUD_w//g.HUD_divisor, g.HUD_h // 2 - apple_icon.get_height()//2
    g.SCREEN.blit(apple_icon, (apple_icon_pos_x, apple_icon_pos_y))
    apple_counter = g.font_tile_size.render(f" x {len(g.snake_body) - 1}", True, (0, 0, 0))
    apple_counter_pos_x, apple_counter_pos_y = apple_icon_pos_x + apple_icon_w, apple_icon_pos_y + (apple_icon_h - g.font_tile_size.get_height()) // 2
    g.SCREEN.blit(apple_counter, (apple_counter_pos_x, apple_counter_pos_y))
    objective_title = g.font_tile_size.render(f"Objective: {g.objective}", True, (0, 0, 0))
    g.SCREEN.blit(objective_title, (g.screen_w - objective_title.get_width() - g.d_tile_size, apple_counter_pos_y))

def draw_game_background() -> None:
    g.SCREEN.blit(g.game_background, (0, 0))

def draw_menu_background() -> None:
    g.SCREEN.blit(g.menu_background, (0, 0))

def draw_fail_state_screen() -> None: #without buttons
    draw_menu_background()
    fail_title = g.font_100.render('You Failed!', True, (56, 79, 93))
    g.SCREEN.blit(fail_title, (g.screen_w // 2 - fail_title.get_width() // 2, g.screen_h // 5))
    # reset button
    button_1.set_image(g.retrybutton)
    button_1.center()
    button_1.move(y=200, x=150)
    button_1.draw()
    button_1.check_if_clicked(g.reset_mode_basic)
    # menu button
    button_2.set_image(g.menubutton)
    button_2.center()
    button_2.move(y=200, x=-150)
    button_2.draw()
    button_2.check_if_clicked(g.reset_menu)

def draw_win_state_screen() -> None:
    draw_menu_background()
    win_title = g.font_100.render('You Won!', True, (56, 79, 93))
    g.SCREEN.blit(win_title, (g.screen_w // 2 - win_title.get_width() // 2, g.screen_h // 5))
    # TODO: add high score
    score = g.font_60.render(f'Score: {g.score}', True, (56, 79, 93))
    g.SCREEN.blit(score, (g.screen_w // 2 - score.get_width() // 2, g.screen_h // 3))
    # reset button
    button_1.set_image(g.retrybutton)
    button_1.center()
    button_1.move(y=200, x=150)
    button_1.draw()
    button_1.check_if_clicked(g.reset_mode_basic)
    # menu button
    button_2.set_image(g.menubutton)
    button_2.center()
    button_2.move(y=200, x=-150)
    button_2.draw()
    button_2.check_if_clicked(g.reset_menu)

def draw_main_menu_screen() -> None:
    draw_menu_background()
    main_title = g.font_100.render('Snake Python', True, (56, 79, 93))
    g.SCREEN.blit(main_title, (g.screen_w // 2 - main_title.get_width() // 2, g.screen_h // 5))
    # start button
    button_1.set_image(g.startbutton)
    button_1.center()
    button_1.move(y=g.screen_h//5)
    button_1.draw()
    button_1.check_if_clicked(g.reset_mode_basic)
    # settings button
    button_2.set_image(g.settingsbutton)
    button_2.center()
    button_2.move(y=button_1.y-button_2.y+75)
    button_2.draw()
    button_2.check_if_clicked(g.reset_settings)

def draw_settings_screen() -> None:
    draw_menu_background()
    settings_title = g.font_100.render('Settings', True, (56, 79, 93))
    g.SCREEN.blit(settings_title, (g.screen_w // 2 - settings_title.get_width() // 2, g.screen_h // 5))
    # cancel button
    button_1.set_image(g.cancelbutton)
    button_1.center()
    button_1.move(x=-150, y=g.screen_h//2.5)
    button_1.draw()
    button_1.check_if_clicked(cancel)
    # save button
    button_2.set_image(g.savebutton)
    button_2.center()
    button_2.move(x=150, y=g.screen_h//2.5)
    button_2.draw()
    button_2.check_if_clicked(save)
    # sfx button
    if g.sfx_temp:
        button_3.set_image(g.sfxonbutton)
    else:
        button_3.set_image(g.sfxoffbutton)
    button_3.center()
    button_3.move(x=-50)
    button_3.draw()
    button_3.check_if_clicked(g.toggle_sfx_temp)
    # music button
    if g.music_temp:
        button_4.set_image(g.musiconbutton)
    else:
        button_4.set_image(g.musicoffbutton)
    button_4.center()
    button_4.move(x=50)
    button_4.draw()
    button_4.check_if_clicked(g.toggle_music_temp)
    # fullscreen button
    button_5.set_image(g.fullscreenbutton)
    button_5.center()
    button_5.move(x=-50, y=g.screen_h//10)
    button_5.draw()
    button_5.check_if_clicked(g.toggle_fullscreen)
    # legacy mode button
    if g.legacy_mode:
        button_6.set_image(g.ogonbutton)
    else:
        button_6.set_image(g.ogoffbutton)
    button_6.center()
    button_6.move(x=50, y=g.screen_h//10)
    button_6.draw()
    button_6.check_if_clicked(g.toggle_legacy_mode)
    # resolution title
    resolution_title = g.font_35.render('Res:', True, (56, 79, 93))
    resolution_title_centered:(int, int) = ((g.screen_w - resolution_title.get_width()) // 2, (g.screen_h - resolution_title.get_height()) // 2 )
    g.SCREEN.blit(resolution_title, (resolution_title_centered[0] - 140, resolution_title_centered[1] + g.screen_h // 5))
    # resolution text boxes
    if not textbox_1.default_string:
        textbox_1.set_default_string(f"{g.screen_w}")
    textbox_1.set_input_validity_function(textbox_validity_check)
    textbox_1.set_font(g.font_35)
    textbox_1.set_fontcolor((56, 79, 93))
    textbox_1.set_w(100)
    textbox_1.center()
    textbox_1.move(x=-50, y=g.screen_h//5)
    textbox_1.draw()
    textbox_1.check_if_clicked()
    textbox_1.edit()
    g.screen_w_temp = int(textbox_1.default_string)
    if not textbox_2.default_string:
        textbox_2.set_default_string(f"{g.screen_h}")
    textbox_2.set_input_validity_function(textbox_validity_check)
    textbox_2.set_font(g.font_35)
    textbox_2.set_fontcolor((56, 79, 93))
    textbox_2.set_w(100)
    textbox_2.center()
    textbox_2.move(x=50,y=g.screen_h//5)
    textbox_2.draw()
    textbox_2.check_if_clicked()
    textbox_2.edit()
    g.screen_h_temp = int(textbox_2.default_string)
    # TODO: Add max_fps / gamespeed setting
    # TODO: Add d_size and velocity setting for basic mode???

# settings helper
def save() -> None:
    g.screen_w = g.screen_w_temp
    g.screen_h = g.screen_h_temp
    g.fullscreen = g.fullscreen_temp
    g.velocity = g.velocity_temp
    g.max_fps = g.max_fps_temp
    g.d_size = g.d_size_temp
    g.d_dist = g.d_dist_temp
    g.sfx = g.sfx_temp
    g.music = g.music_temp
    g.REAL_SCREEN = g.pygame.display.set_mode((0, 0), g.pygame.FULLSCREEN) if g.fullscreen else g.pygame.display.set_mode([g.screen_w, g.screen_h])
    g.SCREEN = g.pygame.Surface((g.screen_w, g.screen_h))
    g.set_HUD()
    g.set_offsets()
    g.reset_menu()

# settings helper
def cancel() -> None:
    g.fullscreen_temp = g.fullscreen
    g.REAL_SCREEN = g.pygame.display.set_mode((0, 0), g.pygame.FULLSCREEN) if g.fullscreen else g.pygame.display.set_mode([g.screen_w, g.screen_h])
    g.reset_menu()

class Button():
    def __init__(self, x=0, y=0, w=0, h=0, drawable:g.pygame.surface.Surface=g.emptybutton) -> None:
        self.x = x
        self.y = y
        self.w = w if w > 0 else drawable.get_width()
        self.h = h if h > 0 else drawable.get_height()
        self.image = drawable
        self.rect = g.pygame.Rect(x, y, self.w, self.h)
        self.is_down = False

    def set_w(self, w:int) -> None:
        self.w = w

    def set_h(self, h:int) -> None:
        self.h = h

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

    def draw(self) -> None:
        g.SCREEN.blit(g.pygame.transform.scale(self.image, (self.w, self.h)), (self.x, self.y))

    def check_if_clicked(self, function=None) -> None:
        if g.pygame.mouse.get_pressed(num_buttons=3)[0] and not self.is_down:
            mouse_x, mouse_y = g.pygame.mouse.get_pos()
            if g.fullscreen or g.fullscreen_temp:
                mouse_x -= (g.REAL_SCREEN.get_width() - g.screen_w) // 2
                mouse_y -= (g.REAL_SCREEN.get_height() - g.screen_h) // 2
            was_clicked = self.x <= mouse_x <= self.x + self.w and self.y <= mouse_y <= self.y + self.h
            if was_clicked and function:
                function()
        self.is_down = g.pygame.mouse.get_pressed(num_buttons=3)[0]
    
class TextBox(Button):
    def __init__(self, x=0, y=0, w=0, h=0, drawable:g.pygame.surface.Surface=g.emptybutton, font=g.font_35, fontcolor=(0, 0, 0)) -> None:
        self.string = ""
        self.default_string = ""
        self.font = font
        self.fontcolor = fontcolor
        self.active:bool = False
        self.validityf = lambda: True
        super().__init__(x, y, w, h, drawable)

    def set_input_validity_function(self, f) -> None:
        self.validityf = f

    def set_default_string(self, string:str) -> None:
        self.default_string = string

    def clear_string(self) -> None:
        self.string = ""

    def set_font(self, font) -> None:
        self.font = font

    def set_fontcolor(self, color:(int, int, int)) -> None:
        self.fontcolor = color

    def draw(self) -> None:
        super().draw()
        if self.active:
            title = self.font.render(self.string, True, (self.fontcolor[0]+15, self.fontcolor[1]+15, self.fontcolor[2]+15))
        else:
            title = self.font.render(self.string, True, self.fontcolor)
        g.SCREEN.blit(title, (self.x + (self.w - title.get_width()) // 2, self.y + (self.h - title.get_height()) // 2))

    def check_if_clicked(self) -> None:
        if g.pygame.mouse.get_pressed(num_buttons=3)[0] and not self.is_down:
            mouse_x, mouse_y = g.pygame.mouse.get_pos()
            if g.fullscreen or g.fullscreen_temp:
                mouse_x -= (g.REAL_SCREEN.get_width() - g.screen_w) // 2
                mouse_y -= (g.REAL_SCREEN.get_height() - g.screen_h) // 2
            self.active = self.x <= mouse_x <= self.x + self.w and self.y <= mouse_y <= self.y + self.h
            if self.active:
                self.string = ""
            else:
                if self.validityf(self):
                    self.default_string = self.string
                else:
                    self.string = self.default_string
        self.is_down = g.pygame.mouse.get_pressed(num_buttons=3)[0]

    def edit(self) -> None:
        if self.active:
            for event in g.pygame.event.get():
                if event.type == g.pygame.KEYDOWN:
                    if event.key == g.pygame.K_RETURN:
                        if self.validityf(self):
                            self.default_string = self.string
                        else:
                            self.string = self.default_string
                        self.active = False
                    elif event.key == g.pygame.K_BACKSPACE:
                        self.string = self.string[:-1]
                    else:
                        self.string += event.unicode

# settings helper
def textbox_validity_check(textbox:TextBox) -> bool:
    return textbox.string.isdigit() and int(textbox.string) >= 500 and len(textbox.string) <= 6

#declare multiuse button objects
button_1 = Button()
button_2 = Button()
button_3 = Button()
button_4 = Button()
button_5 = Button()
button_6 = Button()
textbox_1 = TextBox()
textbox_2 = TextBox()
