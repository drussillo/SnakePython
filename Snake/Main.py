import Global as g
import Input
import Snake
import Apple
import UI
import States
import Obstacle
import Object

g.pygame.init()
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

        case g.Gamestate.MODE_BASIC:
            States.init_mode_basic()
            UI.draw_background()
            UI.draw_HUD()
            running = Input.handle_input_main()

            #draw and move the snake
            Snake.draw()
            Snake.movement()
            # if Snake.check_if_coll_itself() or Snake.out_of_bounds():
            #     Snake.die()
            
            Apple.handle_apples_basic()
            Obstacle.handle_obstacles()

        case _:
            print("Unknown or unhandled gamestate")
            exit()

    g.pygame.display.flip()
    g.clock.tick(g.max_fps)
    
g.pygame.quit()
