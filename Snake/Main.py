import Global as g
import Input
import Snake
import Apple
import UI

g.pygame.init()
g.SCREEN.fill((255, 255, 255))
g.pygame.display.set_caption("Snake")

running = True
while running:
    
    #main loop
    if not g.failstate:
        running = Input.handle_input_main()

        g.SCREEN.fill((200,255,200))
        UI.draw()
        
        #draw and move the snake
        Snake.move()
        Snake.draw()
        Snake.follow_up()
        g.failstate = Snake.check_if_coll_itself() or Snake.out_of_bounds()
        
        Apple.handle_apples()

    #end main loop
        
    #failstate
    else:
        running = Input.handle_input_fail()
        UI.draw_fail_state_screen()

    g.pygame.display.flip()
    g.clock.tick(g.max_fps)
    
g.pygame.quit()