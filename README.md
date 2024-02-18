# Snake

This is my attempt at making snake with python!


# Personal Branch Setup
---IMPORTANTE---
NON UTILIZZARE IL FORK
segui questi passi per il setup del tuo branch personale:
(0.) diventa collaboratore. se mi dai il tuo username github ti invito e devi solo accettare.
1. cancella il tuo fork (lo trovi sotto i tuoi repos)
2. cancella la vecchia cartella e fanne una nuova vuota. dentro alla cartella apri il CMD
3. fai 'git clone https://github.com/BigDave0071/SnakePython.git' per scaricare il repo.
4. fai 'git checkout -b leonardos_branch' per fare un nuovo branch e selezionarlo. 'leonardos_branch' è il nome del branch. per favore dargli un nome volgare.
(5.) (opzionale) fai dei cambiamenti ai file
6. fai 'git add .' per settare tutti i file per il commit
7. fai 'git commit -m "<messaggio>" ' per fare un commit locale (non ancora uploadato)
8. fai 'git push origin leonardos_branch' per salvare i tuoi cambiamenti

ora dovresti avere il tuo branch personale che funziona un pò come il fork, solo che è più diretto.
sul branch ci puoi fare modifiche quando vuoi.
Una volta fatti abbastanza commit, con una feature nuova che funziona, fai un Pull Request al master branch:
1. controlla che tutto ciò che hai aggiunto dall'ultimo sync funzioni
2. vai sul sito github.com
3. vai sul repo di SnakePython
4. seleziona il branch 'leonardos_branch' sopra alla casella con i file.
5. se lo hai selezionato correttamente dovresti vedere i tuoi file invece dei miei.
6. premi su 'contribute' e segui i passi per fare il Pull Request
7. aspetta che ti accetti il PR e dovresti aver finito

dopo il PR accettato, con i tuoi cambiamenti 'merge'ati nel mio 'master' branch, devi
syncare il mio branch con il tuo per proseguire sul un'altra feature, in modo da avere i 
le mie aggiunte a disposizione nel tuo branch. Questo lo puoi in qualsiasi momento (anche 
mentre hai dei commit non Pull Requestati), con il rischio che possa causare conflitti in 
alcune parti del codice. Il sync si fa così:
1. vai nella tua cartella del repo
2. fai 'git branch' e controlla di essere sul tuo branch
(3.) se sei su master (con * e font verde) invece di leonardos_branch, fai 'git checkout leonardos_branch' e torna a step 2.
4. se sei sul tuo branch, fai 'git pull origin master' per scaricare tutti i miei cambiamenti nel tuo branch.
(5.) se ci sono merge conflicts, risolvili usando vscode (vedi se ci riesci)
6. una volta fatto tutto fai il solito 'git add .'; 'git commit -m <message>'; 'git push origin leonardos_branch'
7. Finito!

sto ancora sperimentando pure io quindi se ti 
serve aiuto chiamami o scrivimi su ds o whatsapp.



# _Notes:
Utilizza questo spazio per scrivere messaggi, progressi,
cosa intendi ancora fare etc.



COME CONTINUARE NEL PROGETTO?
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

------