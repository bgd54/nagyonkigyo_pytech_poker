import pokergame_alap
import bot_sample

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(BASE_DIR, "poker")+os.path.sep

# gui betoltese

#master = tk.Tk()
#gui = pokergui_alap.PokerGui(master)
pokergame_alap.master.mainloop()
