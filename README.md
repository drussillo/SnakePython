# Snake

This is my attempt at making snake with python!  

## Installation:  

### Executable  
- If the executable for your specific system is available under the latest release, download and run it.  

### Run from source
- Install python  
- Run pip install pygame on the terminal to install pygame  
- Download as zip and extract or clone into repository
- Go into Snake/ directory and run Main.py

## Notes:

### TODO:
Settings  
- Add velocity setting ?
- Add tilesize (d_size + adj tilesize) setting ?
- Add max_fps / gamespeed setting

Modes:  
- Add basic mode selection from menu 
- Add level mode

Graphics:  
- Custom backgrounds for menu, fail, etc.  
- Custom text  
- HUD improvement

Audio:  
- Add different soundtracks depending on the current background  
  
Obstacles:  
- Obstacle amount changes based on background array size
- Scissors: snake cuts in half

### Ideas for future features (in priority order):   
Different apples  
- Normal apples (1 lenght)
- Big apples (2 lenght)
- Golden apples (5 lenght)
- Magical apples with effects  
            --> Speed boost with [spacebar]  
            --> Invulnerability / eat obstacles  
            --> 2x points!  
            --> Ouroboros? (every second of eating your tail adds a point)  

Obstacles
- dangerous animals  
            --> bird (insta death)  
            --> spider (poison shortens you)  
            --> scorpion (poison shortens you until you eat again)  
            --> ?  

Levels (bigger field, more obstacles, different obstacles; the higher the level, the harder it gets)
