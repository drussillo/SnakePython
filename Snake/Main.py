import Global as g
import Input
import Snake
import Apple as a

g.pygame.init()
g.SCREEN.fill((255, 255, 255))

#Init Apple
#apple1 è il nome dell'oggetto 
#"a." è il riferimento al file Apple.py che è importato "as a", quindi sotto uno pseudonimo)
#Apple() è il nome della Classe con () per __init__ constructor
apple1 = a.Apple()

running = True
while running:
    running = Input.handle_input()
    
    Snake.draw()
    
    if not apple1.is_spawned: #se l'oggetto NON è spawnato:
        apple1.spawn()


    #debug segment positions
    #print(g.snake_body+["     Frame:"+str(Input.frame_count)])

    g.pygame.display.flip()
    g.clock.tick(120)
    
g.pygame.quit()