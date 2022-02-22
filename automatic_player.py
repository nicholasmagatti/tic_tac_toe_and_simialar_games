from player import *
from constants import *


class AutomaticPlayer(Player):
    """
    Class representing information about a specific player controlled by the computer.
    """

    def __init__(self, difficulty_level: str):
        """
        Constructor.

        :param difficulty_level: intelligence level for this player controlled
            by the computer
        """
        if difficulty_level not in DIFFICULTY_LEVELS:
            raise Exception("The difficulty level '" + difficulty_level + "' does not exist")

        self.difficulty_level = difficulty_level
        # set human = false in the superclass
        super(AutomaticPlayer, self).__init__(False)

    def get_difficulty_level(self) -> str:
        """
        Gets the level of the intelligence of this automatic player.
        
        :return: level of the intelligence of this automatic player
        """
        return self.difficulty_level
