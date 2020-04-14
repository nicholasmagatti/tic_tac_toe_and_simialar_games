from player import *


class HumanPlayer(Player):
    """
    Class representing information about a specific human player.
    """

    def __init__(self, name: str):
        """
        Constructor.

        :param name: name of the player
        """
        self.name = name
        # set human = false in the superclass
        super(HumanPlayer, self).__init__(True)
