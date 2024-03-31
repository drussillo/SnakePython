import Global as g
import Input
import Snake
import Apple
import UI

g.pygame.init()
g.SCREEN.fill((110, 135, 97))
g.pygame.display.set_caption("Snake")

running = True
while running:
    
    #main loop
    if not g.failstate:
        running = Input.handle_input_main()

        UI.draw_background()
        UI.draw_HUD()
        
        #draw and move the snake
        Snake.move()
        Snake.draw()
        Snake.follow_up()
        g.failstate = Snake.check_if_coll_itself() or Snake.out_of_bounds()
        
        Apple.handle_apples()
    #end main loop
        
    #failstate
    else:
        UI.draw_fail_state_screen()
        running = Input.handle_input_fail()

    g.pygame.display.flip()
    g.clock.tick(g.max_fps)
    
g.pygame.quit()
