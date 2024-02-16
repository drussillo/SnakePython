# Snake

This is my attempt at making snake with python!



# _Notes:
Utilizza questo spazio per scrivere messaggi, progressi,
cosa intendi ancora fare etc.


---IMPORTANTE---
utilizza il branch leonardos_branch per fare i commit.
voglio provare così, dato che è più diretto di usare i fork.

per pull usa:
git pull origin leonardos_branch
per add usa:
git add .
per commit usa:
git commit -m "messaggio"         //per favore non usare parolacce, il repo è pubblico
per push usa:
git push origin leonardos_branch

le due cose più importanti sono:
git pull origin leonrados_branch;
git push origin leonardos_branch;

non usare pull o push senza 'origin leonardos_branch' perché potrebbe causare conflitto / dare errori

sto ancora sperimentando pure io quindi se ti 
serve aiuto chiamami o scrivimi su ds o whatsapp.



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