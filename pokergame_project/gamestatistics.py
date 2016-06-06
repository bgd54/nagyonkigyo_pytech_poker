__author__ = 'bgd'


class Statistics:

    # Constants of the class player codes:
    BOT = 1
    PLAYER = 0
    # state of current game turn:
    PRE_FLOP = 0
    FLOP = 1
    TURN = 2
    RIVER = 3
    # action codes:
    CHECK = 3
    GIVE = 0
    RAISE = 1
    FOLD = 2

    def __init__(self):
        """
        round_num: index of current game turn
        last_action_bot/player: last actions of bot and player (if we want to see some advanced statistics)
        round2stat: list of dictionaries: every dictionary has one key for each state
         (and states has a list with actions)
        curr
        """
        self.round_num = -1
        self.current_round_state = Statistics.PRE_FLOP
        self.last_action_bot = Statistics.CHECK
        self.last_action_player = Statistics.CHECK
        self.round2stat = []
        self.raise_after_check = [0, 0, 0, 0]
        self.fold_after_check = [0, 0, 0, 0]
        self.fold_after_raise = [0, 0, 0, 0]
        self._new_round()

    def _new_round(self):
        """
        start new round.
        :return:
        """
        self.last_action_bot = -1
        self.last_action_player = -1
        self.round_num += 1
        self.round2stat.append({Statistics.PRE_FLOP: [0, 0, 0], Statistics.FLOP: [0, 0, 0],
                                Statistics.TURN: [0, 0, 0], Statistics.RIVER: [0, 0, 0]})

    def set_state(self, state):
        """
        set the current state to the next. Start new round if state is PRE_FLOP
        :param state: 0-3: Statistics.PRE_FLOP - Statistics.RIVER
        """
        if state == Statistics.PRE_FLOP:
            self._new_round()
        self.last_action_bot = -1
        self.last_action_player = -1
        self.current_round_state = state

    def perform_action(self, action_code, player):
        """
        set actions.
        :param action_code: action code Statistics.GIVE-Statistics.CHECK
        :param player: 0-1 bot-player
        """
        if player == Statistics.BOT:
            self.last_action_bot = action_code
        else:
            if self.last_action_player == Statistics.CHECK and action_code == Statistics.RAISE:
                self.raise_after_check[self.current_round_state] += 1
            if self.last_action_player == Statistics.CHECK and action_code == Statistics.FOLD:
                self.fold_after_check[self.current_round_state] += 1
            if self.last_action_player == Statistics.RAISE and action_code == Statistics.FOLD:
                self.fold_after_raise[self.current_round_state] += 1
            self.last_action_player = action_code
            self.round2stat[self.round_num][self.current_round_state][
                action_code if action_code is not Statistics.CHECK else 0] += 1

    def stat_for_state(self, state):
        """
        Get statistics of a round of betting.
        :param state: state : 0-3 Statistics.GIVE-Statistics.CHECK
        :return list of 3 ints.
        """
        result = [0, 0, 0]
        for r in self.round2stat:
            for i in range(len(result)):
                result[i] += r[state][i]
        return result
