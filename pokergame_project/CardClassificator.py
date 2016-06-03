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
        return [str(chr(table[2*i]-1+ord('A')))+str(table[2*i+1]) for i in range(int(len(table)/2))]


def classificator(color1, value1, color2, value2, color3, value3, color4, value4, color5, value5):
    """
    Determine the value of the given hand.
    :param color1-5: the suit of the proper card 1-4 1: hearts, 2: diamond, 3: spades, 4: clubs
    :param value1-5: the value of the proper card 1-13: 1: Ace, 2: 2, ... 13: King
    :return: 0-9 the value of the hand: 0 - high card 9 - royal flush
    """
    colors = [0, 0, 0, 0]
    colors[color1-1] += 1
    colors[color2-1] += 1
    colors[color3-1] += 1
    colors[color4-1] += 1
    colors[color5-1] += 1
    flush = False
    for i in colors:
        if i == 5:
            flush = True

    values = [value1, value2, value3, value4, value5]

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
            v = pairs.get(k, 0)
            same[v-1] += 1

    if same[0] == 5 and not flush and not straight:
        return 0
    if flush:
        if straight:
            if values[0] == 10:
                return 9
            else:
                return 8
        else:
            return 5
    else:
        if straight:
            return 4  # sima sor
        if same[3]:
            return 7  # poker
        elif same[2]:
            if same[1]:
                return 6  # 3+2-> full
            else:
                return 2  # drill
        else:
            return same[1]  # 1 -> 1 par 2 -> 2 par


def get_best_hand_score(color1, value1, color2, value2, color3, value3, color4,
                        value4, color5, value5, color6=-1, value6=-1, color7=-1, value7=-1):
    """
    Determines the value(0-9) of the best combination from 5-7 cards.
    :param color1-7:  the suit of the proper card 1-4 1: hearts, 2: diamond, 3: spades, 4: clubs
    :param value1-7: the value of the proper card 1-13: 1: 2 ... 13: Ace
    :return: 0-9 the value of the hand: 0 - high card 9- royal flush
    """
    if color6 == -1:
        return classificator(color1, value1, color2, value2, color3, value3, color4,
                             value4, color5, value5)

    colors = [color1, color2, color3, color4, color5, color6]
    values = [value1, value2, value3, value4, value5, value6]
    results = [-1]  # * len(colors)
    if color7 != -1:
        colors.append(color7)
        values.append(value7)
        # results = [-1]*(7*3)
    thread_list = []
    lock = threading.Lock()
    for i in range(0, len(colors)):
        if len(colors) == 6:
            thread_list.append(MyWorker(i, lock, results, colors[i], values[i], colors[(i+1) % 6], values[(i+1) % 6],
                                        colors[(i+2) % 6], values[(i+2) % 6], colors[(i+3) % 6], values[(i+3) % 6],
                                        colors[(i+4) % 6], values[(i+4) % 6]))
            thread_list[i].start()
        else:
            for j in range(i+1, 6):  # 7*6/2
                my_colors = []
                my_values = []
                for mi in range(0, len(colors)):
                    if mi != i and mi != j:
                        my_colors.append(colors[mi])
                        my_values.append(values[mi])
                thread_list.append(MyWorker(i, lock, results, my_colors[0], my_values[0], my_colors[1], my_values[1],
                                            my_colors[2], my_values[2], my_colors[3], my_values[3],
                                            my_colors[4], my_values[4]))
                thread_list[len(thread_list)-1].start()
    for t in thread_list:
        if t.is_alive():
            t.join()
    return results[0]


class MyWorker(threading.Thread):
    """
    Worker class for determine the value of a hand in a thread and store in result_list if better than
        the current value.
    Attributes:
        :param self.threadID:   unique id of the thread      :type int
        :param self.lock:        threading lock for concurrency      :type threading.Lock()
        :param self.result_list:  the list where the best result is stored az index 0      :type list(int)
        :param self.color1-5:    the suit of the proper card 1-4 1: hearts, 2: diamond, 3: spades, 4: clubs :type int
        :param self.value1-5:    the value of the proper card 1-13: 1: 2 ... 13: Ace :type int
    """
    def __init__(self, thread_id, lock, result_list, color1, value1, color2, value2, color3, value3, color4, value4,
                 color5, value5):
        threading.Thread.__init__(self)
        self.threadID = thread_id
        self.lock = lock
        self.result_list = result_list
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
        self.color4 = color4
        self.color5 = color5
        self.value1 = value1
        self.value2 = value2
        self.value3 = value3
        self.value4 = value4
        self.value5 = value5

    def run(self):
        """
        Do the job. Calculate the value of the hand, acquire lock and change the result if needed.
        :return: void
        """
        res = classificator(self.color1, self.value1, self.color2, self.value2, self.color3, self.value3,
                            self.color4, self.value4, self.color5, self.value5)
        self.lock.acquire()
        if res > self.result_list[0]:
            self.result_list[0] = res
        self.lock.release()
