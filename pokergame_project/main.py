from pokergui_alap import PokerGui
from pokergame_alap import Logic


def main():
    gui = PokerGui()
    logic = Logic(gui)
    gui.setLogic(logic)
    gui.start()

main()
