import Global as g
import Input
import Snake
import Apple as a
import HUD

g.pygame.init()
g.SCREEN.fill((255, 255, 255))
g.pygame.display.set_caption("Snake")
apple_1 = a.Apple()
fail_button_1 = HUD.Button(w=60, h=60, image_path="imgs/defaultapple.png")
fail_button_1.center()

running = True
while running:
    
    #main loop
    if not g.failstate:
        running = Input.handle_input_main()

        g.SCREEN.fill((200,255,200))
        HUD.draw()
        
        #draw and move the snake
        Snake.move()
        Snake.draw()
        Snake.follow_up()
        g.failstate = Snake.check_if_coll_itself() or Snake.out_of_bounds()

        if not apple_1.is_spawned and not apple_1.eaten:  
            apple_1.spawn()
        else:
            apple_1 = a.Apple()
        apple_1.check_collision_w_head()
    #end main loop
        
    #failstate
    else:
        running = Input.handle_input_fail()

        HUD.draw_fail_state_screen()
        fail_button_1.draw(g.SCREEN)
        fail_button_1.check_if_clicked()

    g.pygame.display.flip()
    g.clock.tick(120)
    
g.pygame.quit()