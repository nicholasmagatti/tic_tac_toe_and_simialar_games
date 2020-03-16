from player import *


class HumanPlayer(Player):

    def __init__(self, name):
        self.name = name
        # set human = false in the superclass
        super(HumanPlayer, self).__init__(True)
