import Global as g
import Input
import Snake
import Apple
import UI
import States
import Object
import Sound

g.pygame.display.set_caption("Snake")
g.pygame.mixer.init()

running:bool = True

#main loop
while running:
    match g.current_state:

        case g.Gamestate.MENU:
            States.init_menu()
            UI.draw_main_menu_screen()
            running = Input.handle_input_menu()

        case g.Gamestate.FAIL:
            UI.draw_fail_state_screen()
            States.init_fail()
            running = Input.handle_input_fail()

        case g.Gamestate.WIN:
            UI.draw_win_state_screen()
            States.init_win()
            running = Input.handle_input_fail()

        case g.Gamestate.SETTINGS:
            States.init_settings()
            UI.draw_settings_screen()
            running = Input.handle_input_settings()

        case g.Gamestate.MODE_BASIC:
            States.init_mode_basic()
            UI.draw_background()
            UI.draw_HUD()
            running = Input.handle_input_main()

            #draw and move the snake
            Snake.draw()
            Snake.movement()
            Snake.check_if_fail()
            Snake.check_if_win()

            Object.handle_objects()

        case _:
            print("Unknown or unhandled gamestate")
            exit()

    g.REAL_SCREEN.blit(g.SCREEN, ((g.REAL_SCREEN.get_width() - g.screen_w) // 2, (g.REAL_SCREEN.get_height() - g.screen_h) // 2))
    g.pygame.display.flip()
    g.clock.tick(g.max_fps)

g.pygame.quit()
