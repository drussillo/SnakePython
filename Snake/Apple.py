import Global as g
import Snake 
import random

#Yo epic tutorial incoming

#classe Apple con attr: 
# -> bool is_spawned; int x_coord; int y_coord 
class Apple: #Questa è la classe della mela
    def __init__(self): #Questo è il constructor
        self.eaten = False 
        self.is_spawned = False #"self." equivale a "this." su java
        loop = True
        while loop: #Tutta questa parte con il loop e i randint è semplicemente la logica per generare coordinate random.
            rnd_x = random.randint(50, 1230)
            rnd_y = random.randint(50, 670)
            loop = not self.valid_pos(rnd_x, rnd_y)    
        self.x_coord = rnd_x - rnd_x % 25 
        self.y_coord = rnd_y - rnd_y % 25
        
    def valid_pos(self, x, y): #Controlla se le coordinate sono su uno dei segmenti del serpente
        for segment in g.snake_body:
            if segment[0] <= x <= segment[0]+25 and segment[1] <= y <= segment[1]:
                return False
                break
            else: return True
   
    def check_collision(self):
        rect1 = g.pygame.Rect(self.x_coord, self.y_coord, 20, 20)
        head_coordinate_x = g.snake_body[0][0]
        head_coordinate_y = g.snake_body[0][1]
        rect2 = g.pygame.Rect(head_coordinate_x,head_coordinate_y,20,20)

        collides = rect1.colliderect(rect2)
        if collides and not self.eaten:
            Snake.add_segment()
            self.eaten = True 
            self.despawn()
            print(f" apples: { len(g.snake_body) - 1 }")

    
    def despawn(self):
        g.pygame.draw.rect(g.SCREEN, (255,255,255),g.pygame.Rect(self.x_coord,self.y_coord,20,20))

    def spawn(self): #Questa method semplicemente prende le coordinate x, y dell'oggetto e disegna il quadrato rosso della mela
        g.pygame.draw.rect(g.SCREEN, (200, 0, 0), g.pygame.Rect(self.x_coord, self.y_coord, 20, 20))
        self.is_spawned

    

    
#Guarda Main.py per l'init dell'oggetto Apple, Line 9
        

"""
quindi: 
la mela può essere creata come oggetto, sceglie delle
coordinate random sullo schermo entro 50px di bordo su
tutti i lati, con valid_pos() controlla se le coordinate 
si trovano sul serpente, con spawn() viene disegnata la 
mela sulle coordinate scelte. Già implementato nel loop
su Main.py controllando se è già spawnata, quindi se la
despawni basta cambiare la variabile self.is_spawned in
'False'.

COME CONTINUARE?
1. Mangiare la mela:
bisogna fare un modo per detectare se il serpente tocca
la mela. Due approcci sono possibili:
    1. (pygame)p.Rect.colliderect(rect)
        non ho ancora testato questa funzione
        quindi poi devi vedere tu come usarla
    2. Spawna le mele solo dove può passare il serpente
        (griglia 25px) e if snake_body[0] == apple.coords:
        apple.gets_eaten() o qualcosa del genere
    Tu prova ad usare la libreria pygame.Rect

2. Allungare il serpente:
se vai a vedere in Input.py, nell'if-elif sotto p.KEYDOWN
vedrai Snake.add_segment(), che allunga automaticamente il 
serpente (trovi la definizione in Snake.py).
Basta Chiamare questa funzione quando collided = True (vedi 1.)

3. Implementa ciò che vuoi
io mi occuperò del fail_state di quando il serpente tocca se 
stesso o i bordi. Lavorerò anche sulla GUI, su un ipotetico menù
iniziale e magari anche su una specie di scoreboard.
Questo lascialo fare a me in modo da evitare conflitti di merge.


Per comunicare le prossime volte usiamo il README.md file, così
quando facciamo un pull possiamo leggere tutto da lì.

Copierò queste istruzioni sul README quindi se vuoi le puoi 
cancellare da qui / cancellare i commenti lasciati con #.

"""
