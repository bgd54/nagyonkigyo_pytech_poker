import pokergame_alap

def send_to_bot(esemeny,player_money,player_bet,bot_money,bot_bet):

    print esemeny,player_money,player_bet,bot_money,bot_bet
    pokergame_alap.give(who="bot")

