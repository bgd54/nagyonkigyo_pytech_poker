import threading
__author__ = 'bgd'


def format_converter(table, gui_to_bot=True):
    """
    Converts card representation for table from "COLORCHARNUMBER" to NUMBER, NUMBER or backwards(if gui_to_bot is False)
    :param table: list of cards
    :param gui_to_bot: True to convert gui format("CNN") to bot format(N,N). :type boolean
    :return: list of cards with the opposite format
    """
    if gui_to_bot:
        return sum([[(ord(s[0])-ord('A')+1), int(s[1:])] for s in table], [])
    else:
        return [str(chr(table[2*i]-1+ord('A')))+str(table[2*i+1]) for i in range(len(table)//2)]


def compare_hands(hand1, hand2, val1=-1, val2=-1):  # TODO count-tal mappal vmi rovid..
    """
    Compares two hand and return 1 if hand1<hand2 0 if hand1 == hand2 -1 if hand1>hand2
    :param hand1: list of 5 cards in bot format (C,V) C,V integer
    :param hand2: list of 5 cards in bot format (C,V) C,V integer
    :param val1: optional 0-9 the value of the hand1 :type int
    :param val1: optional 0-9 the value of the hand2 :type int
    :return: int: -1 if hand1>hand2 1 if hand1<hand2 and 0 if they're equals.
    """
    if val1 == -1:
        val1 = classificator(hand1)
    if val2 == -1:
        val2 = classificator(hand2)
    if val1 < val2:
        return 1
    elif val2 < val1:
        return -1
    elif val1 == 9:
        return 0
    values1 = [hand1[2*i+1] for i in range(len(hand1)//2)]
    values2 = [hand2[2*i+1] for i in range(len(hand2)//2)]
    values1 = [x if x != 1 else 14 for x in values1]
    values2 = [x if x != 1 else 14 for x in values2]
    values1.sort()
    values2.sort()
    formation1 = []
    formation2 = []
    if val1 == 1 or val1 == 2 or val1 == 3 or val1 == 7:  # kigyujti az azonos foma(ka)t novekvo sorrendben
        for i in range(len(values1)-1):
            if values1[i] == values1[i+1] and values1[i] not in formation1:
                formation1.append(values1[i])
            if values2[i] == values2[i+1] and values2[i] not in formation2:
                formation2.append(values2[i])
    if val1 == 6:
        if values1[0] == values1[2]:  # ful: 3+2 -> ha az 0. == 2. akkor az elso a drill -> nagyobb prioritas
            formation1 = [values1[3], values1[0]]
        else:
            formation1 = [values1[0], values1[3]]
        if values2[0] == values2[2]:
            formation2 = [values2[3], values2[0]]
        else:
            formation2 = [values2[0], values2[3]]
    if len(formation1) == 2:  # full es 2 par ha a nagyobb par / drill nagyobb az nyer
        if formation1[1] < formation2[1]:
            return 1
        elif formation1[1] > formation2[1]:
            return -1
    if len(formation1) > 0:  # ha van formacio es eljut idaig akkor az alapjan dont
        if formation1[0] < formation2[0]:
            return 1
        elif formation1[0] > formation2[0]:
            return -1
    for i in range(len(values1)-1, -1, -1):  # magas lap dont/sor legmagasabb lapja
        if values1[i] != values2[i]:
            return 1 if values1[i] < values2[i] else -1
    return 0


def classificator(hand):
    """
    Determine the value of the given hand. The hand must be in bot format: list of 10 integer where every 2 integer
     represents a card. The first integer is the suit the second is the value.
     Suit of a card:  1-4 1: hearts, 2: diamond, 3: spades, 4: clubs
     Value of a card: 1-13: 1: Ace, 2: 2, ... 13: King
    :param hand: list of 5 cards in bot format
    :return: 0-9 the value of the hand: 0 - high card 9 - royal flush
    """
    colors = [0, 0, 0, 0]
    for i in range(len(hand)//2):
        colors[hand[2*i]-1] += 1
    flush = 5 in colors

    values = [hand[1], hand[3], hand[5], hand[7], hand[9]]

    values = [x if x != 1 else 14 for x in values]
    values.sort()
    straight = True
    pairs = {values[0]: 1}
    for i in range(1, len(values)):
        if values[i] in pairs.keys():
            pairs[values[i]] += 1
        else:
            pairs[values[i]] = 1
        if values[i-1] != values[i]-1:
            straight = False

    same = [0, 0, 0, 0]

    for k in pairs.keys():
            v = pairs.get(k, 1)
            same[v-1] += 1

    if same[0] == 5 and not flush and not straight:
        return 0
    if flush:
        if straight:
            if values[0] == 10:
                return 9  # szin + sor + legkisebb 10 -> royal flush
            else:
                return 8  # szin + sor + legkisebb nem 10 -> szinsor
        else:
            return 5  # flush
    else:
        if straight:
            return 4  # sima sor
        if same[3]:
            return 7  # poker
        elif same[2]:
            if same[1]:
                return 6  # 3+2-> full
            else:
                return 3  # drill
        else:
            return same[1]  # 1 -> 1 par 2 -> 2 par


def get_best_hand(table, bot_format=False, out_fmt_bot=True):
    """
    Determines the value(0-9) of the best combination from 5-7 cards.
    sample call: score, best_hand = get_best_hand(table)
                 score, best_hand = get_best_hand(table=table, bot_format=False, out_fmt_bot=True)
    :param table: list of 5 to 7 cards in given format
        bot format: the suits of the cards represented as 1-4 1: hearts, 2: diamond, 3: spades, 4: clubs
                    the values of cards represented as 1-13: 1: Ace, 2: 2 ... 13: King card: C,V
        gui format: the suits of the cards represented with chars: A-D A: hearts, B: diamond, C: spades, D: clubs
                    the values represented the same way as above. card: "CVV"
    :param bot_format:  optional, specifies the format that given gui format by default. :type boolean
    :param out_fmt_bot: optional, specifies the format for the output best_hand. True-> bot format :type boolean
    :return: [value, best_hand] where value is an integer: 0-9 the value of the hand: 0 - high card 9 - royal flush and
        best_hand is a list containing the best hand with given format.
    """
    converted_table = table if bot_format else format_converter(table)

    if len(converted_table) == 10:
        return [classificator(converted_table),
                converted_table if out_fmt_bot else format_converter(table) if bot_format else table]

    results = [-1] * (6 if len(converted_table) == 12 else 7*6//2)
    thread_list = []
    # lock = threading.Lock()
    for i in range(0, len(converted_table)//2):
        if len(results) == 6:
            thread_list.append(MyWorker(i, results, converted_table[0:2*i]+converted_table[2*i+2:]))  # , lock))
            thread_list[i].start()
        else:
            for j in range(i+1, 7):  # 7*6/2
                my_hand = []
                for mi in range(0, len(results)):
                    if mi != i and mi != j:
                        my_hand.extend(converted_table[2*mi:2*mi+2])
                thread_list.append(MyWorker(len(thread_list), results, my_hand))  # , lock))
                thread_list[len(thread_list)-1].start()
    for t in thread_list:
        if t.is_alive():
            t.join()
    # if lock is not None:
    #    return results[0]
    max_ind = 0
    max_value = results[0]
    for i in range(1, len(results)):
        if results[i] == max_value:
            comp = compare_hands(thread_list[max_ind].hand, thread_list[i].hand, results[max_ind], results[i])

            if comp == 1:
                max_ind = i
                max_value = results[i]
        elif results[max_ind] < results[i]:
            max_ind = i
            max_value = results[i]
    return [max_value, thread_list[max_ind].hand if out_fmt_bot else format_converter(thread_list[max_ind].hand, False)]


def who_win(player_cards, bot_cards, table, is_bot_format=False, get_hands=False):
    """
    Determine which player has better hand.
    :param player_cards: cards of player(2) the format is given by is_bot_format
    :param bot_cards: cards of the bot(2) the format is given by is_bot_format
    :param table: cards on the table(5) the format is given by is_bot_format
    :param is_bot_format: :type boolean the format used as input True if bot format.
    :param get_hands: :type boolean if true it returns the hands of the players.
    :return: return -1 if player loose 0 if draw 1 if player has won, if asked gives back the hands.
    """
    player_score, player_hand = get_best_hand(player_cards+table, is_bot_format)
    bot_score, bot_hand = get_best_hand(bot_cards+table, is_bot_format)

    if not get_hands:
        return compare_hands(bot_hand, player_hand, bot_score, player_score)
    else:
        return [compare_hands(bot_hand, player_hand, bot_score, player_score), player_hand, bot_hand]


class MyWorker(threading.Thread):
    """
    Worker class for determine the value of a hand in a thread and store in result_list if better than
        the current value.
    Attributes:
        :param self.threadID:   unique id of the thread      :type int
        :param self.lock:        threading lock for concurrency      :type threading.Lock()
        :param self.result_list:  the list where the best result is stored az index 0      :type list(int)
        :param self.hand:         the hand corresponds to this thread. the hand must be in bot format! card=(S,V)
    """
    def __init__(self, thread_id, result_list, hand, lock=None):
        threading.Thread.__init__(self)
        self.threadID = thread_id
        self.lock = lock
        self.result_list = result_list
        self.hand = hand

    def run(self):
        """
        Do the job. Calculate the value of the hand, and save to the threadIDth place int the result_list
        if lock is not None then write to result_list[0] if this hand is better then the previous.
        :return: void
        """
        if self.lock is not None:
            res = classificator(self.hand)
            self.lock.acquire()
            if res > self.result_list[0]:
                self.result_list[0] = res
            self.lock.release()
        else:
            self.result_list[self.threadID] = classificator(self.hand)

"""
curr_table = [1,3, 3,12, 2,2, 2,4, 2,11]
bot = [2,8, 1,2]
player = [3,8, 3,7]

c, p, b = who_win(player, bot, curr_table, True, True)
print(c)
print(p)
print(b)
"""
