import Global as g
from enum import Enum

class Type(Enum):
    VOID = 0
    GROW = 1
    DEATH = 2
    SPAWN = 3
    DAMAGE = 4

def playBGM() -> None:
    if g.music:
        g.pygame.mixer.music.play(-1,0.0)

def setBGM(path:str) -> None:
    g.pygame.mixer.music.load(path)

def setCurrentBGM() -> None:
    match g.current_bgtileset:
        case g.bgtileset_jungle:
            setBGM(g.resource_path("audio/MainSoundtrack1-jungle.wav"))
        #TODO: Add more soundtracks
        case _:
            setBGM(g.resource_path("audio/MainSoundtrack1.wav"))

def stop() -> None:
    g.pygame.mixer.music.stop()

def is_playing() -> bool:
    return g.pygame.mixer.get_busy()

def play(type:Type) -> None:
    if g.sfx:
        match type:
            case Type.GROW:
                path = g.resource_path("audio/grow.wav")
            case Type.DEATH:
                path = g.resource_path("audio/death.wav")
            case Type.SPAWN:
                path = g.resource_path("audio/spawn.wav")
            case Type.DAMAGE:
                path = g.resource_path("audio/damage.wav")
            case _:
                path = g.resource_path("audio/error.wav")

        sound = g.pygame.mixer.Sound(path)
        sound.set_volume(0.2)
        sound.play()
