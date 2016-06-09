import pokergame_alap
import random

class botbeta:
    def __init__(self, logic):
        self.logic = logic

    def send_to_bot(self,esemeny,player_money,player_bet,bot_money,bot_bet):

        print esemeny,player_money,player_bet,bot_money,bot_bet
        values = []
        for i in range(50):
            values.append(i)
        next_step = random.choice(values)

        if esemeny == "kezdes":
            self.logic.give(who="bot")
            print "a bot betette a nagyvak tetet"
        
        else:

            if next_step <10:

                self.logic.throw(who="bot")
                print "a bot eldobja"
                
            elif next_step >=10 and next_step <40:

                self.logic.give(who="bot")
                print "a bot tartja"
                
            else:

                self.logic.raise1(who="bot")
                print "a bot emel"

    def send_to_bot_cards(self,cards):

        print cards
