import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


class Adapter:

    def __init__(self):
        pass

    @staticmethod
    def start_turn(player_hand, bot_hand, player_money, bot_money, blind):
        """
        Adott kor kezdese. Megkapjuk a lapokat es kiosztja a botnak es a GUInak.
        :param player_hand:  A gui jatekos lapja
        :param bot_hand:     Bot lapjai
        :param player_money: Jatekos penze
        :param bot_money:    Bot penze
        :param blind:        Ki a vak pl 0 bot 1 jatekos.
        :return:
        """
        pass

    def flop(self, card1, card2, card3):
        """
        A flop felforditasa. Kuldes Guinak es a botnak.
        :param card1: lap1
        :param card2: lap2
        :param card3: lap3
        :return:
        """
        pass

    def turn(self, card):
        """
        Turn. funkcio ugyanaz mint a flopnak.
        :param card: lap1
        :return:
        """
        pass

    def river(self, card):
        """
        Utolso lap. funkcio ugyanaz mint a flopnak.
        :param card: lap1
        :return:
        """
        pass

    def request_act(self, player): #TODO itt ki kell talalni, h milyen strukturaban erdemes a licitet megcsinalni.
        """
        A soron kovetkezo jatekostol varjuk a lepest.
        :param player:
        :return:
        """
        pass

    def endturn(self):
        """
        Kor befejezese. Eredmenyek kozlese a jatekosokkal. Esetleges tovabb engedesre varni a guitol.
        :return:
        """
        pass
