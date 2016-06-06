from pokergui_alap import PokerGui
from pokergame_alap import Logic

import time


def main():
    gui = PokerGui()
    logic = Logic(gui)
    gui.setLogic(logic)
    gui.select_player()
    gui.start()
    

main()
