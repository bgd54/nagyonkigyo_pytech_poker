import pickle
from sklearn.externals import joblib
import CardClassificator
import pokergame_alap

__author__ = 'szlge'


class PokerBot:

    # a current_hand egy list, amiben szin-ertek parok vannak felsorolva
    def __init__(self, logic, current_hand=None, statistics=None):

        self._estimator = joblib.load('train/traineddata_27.pkl')
        self._current_hand = current_hand
        self._is_preflop = True
        self._game_score = 0  # az eddig jateklepesek alapjan kapott erteket tartja nyilvan
        self._statistics = statistics
        self._logic = logic
        self._current_value = 0

    # a preflop kezdokezeket kulon kell kezelnunk, mert ez csak ket lapot jelent
    # ezekhez kulon rendelunk score-okat es eleg lazan ertekeljuk,
    # mert heads-up mar egy par is igen sokat er
    # itt nem veszi figyelembe az ellenfelet meg, de kesobb ide kellene azt a funkciot is beepiteni
    def preFlopHandEvaluation(self):

        preflop_score = 0

        if self._is_preflop == True:

            if self._current_hand[0] == self._current_hand[2]:

                preflop_score += 1

            if self._current_hand[1] == self._current_hand[3]:

                preflop_score += 4.5

            if self._current_hand[1] == 1 | self._current_hand[1] > 9:

                preflop_score += 0.5

            if self._current_hand[3] == 1 | self._current_hand[3] > 9:

                preflop_score += 0.5

            if preflop_score > 9:

                preflop_score = 9

            return preflop_score

        else:

            return 0

    def setGameScore(self, new_score):

        self._game_score = new_score

    def setIsPreFlop(self, val):
        print(val)
        self._is_preflop = val

    def giveBlind(self):

        self._logic.give(who="bot")

    def setCurrentHand(self, current_hand, form=False):

        self._current_hand = current_hand if form else CardClassificator.format_converter(current_hand)

    # minden postflop lepesnel ennek az fv-nek kell lefutnia
    def setPostFlopHand(self, hands):
        self._current_value, self._current_hand = CardClassificator.get_best_hand(hands)

    # svm alapjan kiertekeli a kezet random kez ellen
    # 5 lapbol allo kezdokezeket ertekel ki
    def randomHandEvaluation(self):

        prediction_value = self._estimator.predict([self._current_hand])
        return prediction_value

    # statisztikai informaciok alapjan hatarozza meg a kez erejet
    def statisticalHandEvaluation(self):
        pass

    # dontes a kovetkezo lepesrol, 0-dob, 1-call, 2-bet/raise/reraise
    def makeDecision(self):

        decision = 0

        if self._is_preflop:

            hand_value = self.preFlopHandEvaluation()

            if hand_value >= 4.5:

                decision = 2
                return decision
            elif hand_value > 0:
                return 1

        else:
            print(self._current_hand)
            hand_value = self.randomHandEvaluation()

            if hand_value >= 5:

                decision = 2
                return decision

        return decision
