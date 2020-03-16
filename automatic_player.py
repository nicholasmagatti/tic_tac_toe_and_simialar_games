from player import *
from constants import *


class AutomaticPlayer(Player):

    def __init__(self, difficulty_level):
        self.difficulty_level = difficulty_level
        # set human = false in the superclass
        if difficulty_level not in DIFFICULTY_LEVELS:
            raise Exception("The difficulty level '" + difficulty_level + "' does not exist")
        super(AutomaticPlayer, self).__init__(False)

    def get_difficulty_level(self):
        return self.difficulty_level
