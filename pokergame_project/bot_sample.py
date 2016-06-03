import pokergame_alap

class botbeta:
    def __init__(self, logic):
        self.logic = logic

    def send_to_bot(self,esemeny,player_money,player_bet,bot_money,bot_bet):

        print esemeny,player_money,player_bet,bot_money,bot_bet
        self.logic.give(who="bot")

