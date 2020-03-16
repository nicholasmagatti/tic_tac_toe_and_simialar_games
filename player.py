from abc import ABC, abstractmethod
from constants import *


class Player(ABC):
    """ Abstract class to represent a player (automatic or human)
        and manage their choices during the game.
    """
    human = None

    def __init__(self, is_human_player: bool):
        self.human = is_human_player

    def is_human(self):
        return self.human

    def set_id(self, assigned_id: int):
        if assigned_id == EMPTY_CELL:
            raise Exception("The id is also the sign used to write on the board and " +
                            "cannot be " + str(EMPTY_CELL) + " because it is used " +
                            "for identifying empty cells.")
        self.id = assigned_id

    def get_id(self):
        return self.id



