from abc import ABC, abstractmethod
from constants import *


class Player(ABC):
    """
    Abstract class representing a player (automatic or human).
    """
    human = None

    def __init__(self, is_human_player: bool):
        """
        Constructor.

        :param is_human_player
        """
        self.human = is_human_player

    def is_human(self) -> bool:
        """
        Returns True if this player is a human user, False otherwise.

        :return: True if this player is a human user, False otherwise
        """
        return self.human

    def set_id(self, assigned_id: int) -> None:
        """
        Sets the id (unique identifier) for this player.

        :param assigned_id: unique identifier assigned to this player

        :raises Exception: The id is equal to the int used to identify
            empty cells on the grid
        """
        if assigned_id == EMPTY_CELL:
            raise Exception("The id is also the sign used to write on the grid and " +
                            "cannot be " + str(EMPTY_CELL) + " because it is used " +
                            "for identifying empty cells.")
        self.id = assigned_id

    def get_id(self) -> int:
        """
        Gets this player's unique identifier.

        :return: this player's unique identifier
        """
        return self.id



