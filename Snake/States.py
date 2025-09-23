import Global as g
import Sound

initalized_state = g.Gamestate.VOID

def init_menu() -> None:
    global initalized_state
    if initalized_state != g.Gamestate.MENU:
        Sound.setBGM("./audio/MainSoundtrack1-trianglewave.wav")
        Sound.playBGM()
        initalized_state = g.Gamestate.MENU

def init_fail() -> None:
    global initalized_state
    if initalized_state != g.Gamestate.FAIL:
        Sound.stop()
        initalized_state = g.Gamestate.FAIL


def init_mode_basic() -> None:
    global initalized_state
    if initalized_state != g.Gamestate.MODE_BASIC:
        Sound.setBGM("./audio/MainSoundtrack1.wav")
        Sound.playBGM()
        initalized_state = g.Gamestate.MODE_BASIC

