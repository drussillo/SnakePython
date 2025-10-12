import Global as g
from enum import Enum

class Type(Enum):
    VOID = 0
    GROW = 1
    DEATH = 2
    SPAWN = 3

def playBGM() -> None:
    if g.music:
        g.pygame.mixer.music.play(-1,0.0)

def setBGM(path:str) -> None:
    g.pygame.mixer.music.load(path)

def stop() -> None:
    g.pygame.mixer.music.stop()

def is_playing() -> bool:
    return g.pygame.mixer.get_busy()

def play(type:Type) -> None:
    if g.sfx:
        match type:
            case Type.GROW:
                path = "./audio/grow.wav"
            case Type.DEATH:
                path = "./audio/death.wav"
            case Type.SPAWN:
                path = "./audio/spawn.wav"
            case _:
                path = "./audio/error.wav"

        sound = g.pygame.mixer.Sound(path)
        sound.set_volume(0.2)
        sound.play()
