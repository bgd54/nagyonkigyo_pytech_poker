__author__ = 'szlge'


class GameTree(object):

    def __init__(self, root=None, currentnode=None):
        super(GameTree, self).__init__()
        self._root = root
        self._currentnode = currentnode

    # a dontesi fa node-jainak reprezentaciojahoz
    class Node:

        def __init__(self, left = None, middle = None, right = None,
                     score = 0):
            self._left = left
            self._middle = middle
            self._right = right
            self._score = score

        def _getLeft(self):
            return self._left

        def _getMiddle(self):
            return self._middle

        def _getRight(self):
            return self._right

        def _isLeaf(self):

            if self._left == None and self._middle == None and self._right == None:

                return True

            else:

                return False

    def _getTemplate(self, num):

        template = self.Node(self.Node(None, None, None, 2 + num),
                     self.Node(None, None, None, 3 + num),
                     self.Node(self.Node(None, None, None, 4 + num),
                          self.Node(None, None, None, 5 + num),
                          self.Node(self.Node(None, None, None, 6 + num),
                                    self.Node(None, None, None, 7 + num),
                                    None, 6 + num), 4 + num), 2 + num)

        return template

    # ket implementacioja lesz attol fuggoen, hogy pre-vagy postflop vagyunk eppen
    def generateTree(self):
        raise NotImplementedError

    def simulationhelper(self, value):

            if value == 0:

                if self._currentnode._getLeft() != None:

                    self._currentnode = self._currentnode._getLeft()
                    print(self._currentnode._score)

                else:

                    print('LeafNode')
                    print(self._currentnode._score)

            elif value == 1:

                if self._currentnode._getMiddle() != None:

                    self._currentnode = self._currentnode._getMiddle()
                    print(self._currentnode._score)

                else:

                    print('LeafNode')
                    print(self._currentnode._score)

            elif value == 2:

                if self._currentnode._getRight() != None:

                    self._currentnode = self._currentnode._getRight()
                    print(self._currentnode._score)

                else:

                    print('LeafNode')
                    print(self._currentnode._score)


    # egy lepes az allapotfan, amit a pokerbot vagy a jatekos hajt vegre
    def makeStep(self, value):

        if value == 0:

            if self._currentnode._getLeft() != None:

                self._currentnode = self._currentnode._getLeft()
                print(self._currentnode._score)

            else:

                print('LeafNode')
                print(self._currentnode._score)

        elif value == 1:

            if self._currentnode._getMiddle() != None:

                self._currentnode = self._currentnode._getMiddle()
                print(self._currentnode._score)

            else:

                print('LeafNode')
                print(self._currentnode._score)

        elif value == 2:

            if self._currentnode._getRight() != None:

                self._currentnode = self._currentnode._getRight()
                print(self._currentnode._score)

            else:

                print('LeafNode')
                print(self._currentnode._score)

        else:

            print('invalid input')


    # csak a teszteleshez fog meg kelleni ez a metodus, a vegleges implementaciobol toroljuk
    def simulate(self):

        while True:

            number = input('Please give a number:')
            value = int(number)

            if value == 0:

                if self._currentnode._getLeft() != None:

                    self._currentnode = self._currentnode._getLeft()
                    print(self._currentnode._score)

                else:

                    print('LeafNode')
                    print(self._currentnode._score)
                    break

            elif value == 1:

                if self._currentnode._getMiddle() != None:

                    self._currentnode = self._currentnode._getMiddle()
                    print(self._currentnode._score)

                else:

                    print('LeafNode')
                    print(self._currentnode._score)
                    break

            elif value == 2:

                if self._currentnode._getRight() != None:

                    self._currentnode = self._currentnode._getRight()
                    print(self._currentnode._score)

                else:

                    print('LeafNode')
                    print(self._currentnode._score)
                    break

            else:

                print('invalid input')
                break



class PreFlopTree(GameTree):

    def __init__(self):
        super(GameTree, self).__init__()
        self._generateTree()

    def _generateTree(self):

        right = self._getTemplate(0)

        middle = self.Node(self.Node(None, None, None, 1),
                        None,
                        self._getTemplate(1),
                        1)

        left = self.Node(None, None, None, 0)

        self._root = self.Node(self.Node(None, None, None, 0), middle, right)
        self._currentnode = self._root


class PostFlopTree(GameTree):

    def __init__(self, lastscore):
        super(GameTree, self).__init__()
        self._lastscore = lastscore
        self._generateTree()

    def _generateTree(self):

        left = self.Node(self.Node(None, None, None, self._lastscore),
                   None,
                   self._getTemplate(self._lastscore), self._lastscore)

        right = self._getTemplate(self._lastscore)

        self._root = self.Node(left, None, right)
        self._currentnode = self._root

"""
ptree = PostFlopTree(10)
ptree.makeStep(2)
ptree.makeStep(2)
ptree.makeStep(2)
"""
