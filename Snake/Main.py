import Global as g
import Input
import Snake
import Apple
import UI

g.pygame.init()
g.SCREEN.fill((110, 135, 97))
g.pygame.display.set_caption("Snake")

running:bool = True

#main loop
while running:
    match g.current_state:

        case g.Gamestate.MODE_BASIC:
            running = Input.handle_input_main()

            UI.draw_background()
            UI.draw_HUD()
            
            #draw and move the snake
            Snake.move()
            Snake.draw()
            Snake.follow_up()
            if Snake.check_if_coll_itself() or Snake.out_of_bounds():
                g.current_state = g.Gamestate.FAIL
            
            Apple.handle_apples()
        case g.Gamestate.FAIL:
            UI.draw_fail_state_screen()
            running = Input.handle_input_fail()

        case g.Gamestate.MENU:
            UI.draw_main_menu_screen()
            running = Input.handle_input_menu()

        case _:
            print("Unknown or unhandled gamestate")
            exit()

    g.pygame.display.flip()
    g.clock.tick(g.max_fps)
    
g.pygame.quit()
