import random
import time
from constants import *
from user_input_manager import *
from typing import Tuple, List, Union
from player import Player
from human_player import HumanPlayer
from automatic_player import AutomaticPlayer


class GameManager:
    """
    Class that manages a single game session.
    """
    # array_players contains an array of int numbers, that identify each player
    def __init__(self, rows: int, columns: int, marks_to_win: int,
                 players: Tuple[Union[HumanPlayer, AutomaticPlayer]], computer_difficulty: str = None):
        """
        Constructor.

        :param rows: number of rows on the grid
        :param columns: number of columns on the grid
        :param marks_to_win: number of marks to put on a line to
            win the game, vertically, horizontally or diagonally
        :param players: tuple of the players in order for the game.
            The first turn starts from the player in the first position
        :param computer_difficulty: intelligence level for the players
            controlled by the computer
        """
        self.MARKS_TO_WIN = marks_to_win
        self.players = players
        # initialize the matrix (representing the board)
        self.grid = [[EMPTY_CELL] * columns for r in range(rows)]
        self.COMPUTER_DIFFICULTY_LEVEL = computer_difficulty
        self.player_of_current_turn = players[0]

    def start_game(self) -> None:
        """
        Starts a game session and manages it until its end.
        """
        self.display_grid()
        winner = None
        while (winner is None) & (not self.is_grid_full()):
            self.manage_current_turn()
            self.display_grid()
            self.change_turn()
            winner = self.winner()
        # end of the game
        if winner is not None:
            print("The player number " + str(winner) + " won!!!")
        else:
            print("Tie. Nobody won.")

    def change_turn(self) -> None:
        """
        Sets the next player as the active player: the one of the current turn.
        """
        index_player_current_turn = self.players.index(self.player_of_current_turn)
        # if the current is the last player of the tuple, the next is the first of the tuple
        if index_player_current_turn == len(self.players) - 1:
            self.player_of_current_turn = self.players[0]
        else:
            self.player_of_current_turn = self.players[index_player_current_turn + 1]

    def manage_current_turn(self) -> None:
        """
        Manages a single turn, interacting with the user or making
        an automatic player choose the move to name, then mark the
        designed cell on the grid.
        """
        player_number = self.player_of_current_turn.get_id()
        if self.player_of_current_turn.is_human():
            # uppercase only first letter of the name (attribute of the class HumanPlayer)
            name_to_print = self.player_of_current_turn.name
            name_to_print = name_to_print[0].upper() + name_to_print[1:]
            print(name_to_print + ": it's your turn!")
            print("You are the number " + str(player_number) + ".")
            self.make_user_move(player_number)
        else:  # automatic player (controlled by the computer)
            print("Turn of the player number " + str(player_number) + ":")
            """
            Sleep for a while, so that users see automatic players wait a short time
            before making their move, as they were real users.
            In case the move already took a relevant amount of time, measure its
            execution time to decide then a suitable sleep duration.
            """
            min_seconds_wait = 2.1
            start_timer = time.time()
            self.make_automatic_player_move()
            seconds_elapsed = time.time() - start_timer
            sleep_duration = min_seconds_wait - seconds_elapsed
            if sleep_duration > 0:
                time.sleep(sleep_duration)

    def make_user_move(self, user_number: int) -> None:
        """
        Makes the user choose their move and mark the chosen cell on the grid.

        :param user_number: user's identifier
        """
        acceptable_lines = self.available_lines()
        # making elements start from 1 instead of 0
        # acceptable_lines = list(map(lambda x: x + 1, acceptable_lines))
        acceptable_lines = add_n_to_each_element(1, acceptable_lines)
        # less one to make it start from 0 instead of 1
        chosen_line = custom_int_input("line: ", acceptable_lines) - 1
        available_columns = self.available_columns_on_specified_line(chosen_line)
        # making elements start from 1 instead of 0
        available_columns = add_n_to_each_element(1, available_columns)
        # less one to make it start from 0 instead of 1
        chosen_col = custom_int_input("column: ", available_columns) - 1

        self.make_move(chosen_line, chosen_col, user_number)

    def make_automatic_player_move(self) -> None:
        """
        Makes the automatic player of this turn choose and make its move,
        assuming that the player of the turn is an automatic player.

        :raises Exception: the player of the turn is a human player
        """
        if self.player_of_current_turn.is_human():
            raise Exception("The current player is a human player.")
        mode = self.player_of_current_turn.difficulty_level
        if mode == DIFFICULTY_LEVEL_RANDOM:
            cell_to_mark = random.choice(self.get_empty_cells())
            line = cell_to_mark[0]
            column = cell_to_mark[1]
            self.make_move(line, column, self.player_of_current_turn.get_id())

    def get_cells_marked_as(self, mark: int) -> Tuple[Tuple[int, int]]:
        """
        Returns a list representing the cells on the grid with the specified
        mark in the form of ((x_1,y_2),...,(x_n,y_n)).

        :param mark: number representing the mark of a player on the
            grid or the mark to represent empty cells

        :return: cells on the grid with the specified mark in the form
        of ((x_1,y_2),...,(x_n,y_n)), where x is the line and y the column
        """
        list_cells = []
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] == mark:
                    list_cells.append((i, j))
        return tuple(list_cells)

    def get_empty_cells(self) -> Tuple[Tuple[int, int]]:
        """
        Returns a tuple containing couples of values representing the
        position of the empty cells on the grid (the ones that have
        not been marked yet).

        :return: tuple containing couples of values representing the
            position of the empty cells on the grid
        """
        return self.get_cells_marked_as(EMPTY_CELL)

    def display_grid(self) -> None:
        """
        Prints the grid to the user.
        """
        for i in range(len(self.grid)):
            print(self.grid[i])

    def get_grid_copy(self) -> List[List[int]]:
        """
        Returns a copy of the grid.

        :return: copy of the grid
        """
        return self.grid.copy()

    def is_grid_full(self) -> bool:
        """
        Returns True if there are no empty spaces left on the grid, False otherwise.

        :return: True if there are no empty spaces left on the grid, False otherwise
        """
        for line in self.grid:
            if EMPTY_CELL in line:
                return False
        return True

    def available_lines(self) -> Tuple[int]:
        """
        Returns a tuple containing the indexes of the lines that have at least one empty cell.

        :return: indexes of the lines that have at least one empty cell
        """
        markable_lines = []
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if (self.grid[i][j] == EMPTY_CELL) & (i not in markable_lines):
                    markable_lines.append(i)
        return tuple(markable_lines)

    def available_columns_on_specified_line(self, line: int) -> Tuple[int]:
        """
        Returns a tuple containing the indexes of the empty cells on the
        specified line.

        :param line: specified line
        :return: indexes of the empty cells on the specified line
        """
        available_columns = []
        for col in range(len(self.grid[line])):
            if (self.grid[line][col] == EMPTY_CELL) & (col not in available_columns):
                available_columns.append(col)
        return tuple(available_columns)

    def make_move(self, line: int, column: int, player_mark: int) -> None:
        """
        Marks the specified cell with the sign of the designed player.

        :param line: line of the cell to mark
        :param column: column on the cell to mark
        :param player_mark: identifier of the player who has to make the move

        :raises Exception: the designed cell is already marked
        """
        if self.grid[line][column] != EMPTY_CELL:
            raise Exception("The chosen cell is not empty.")
        self.grid[line][column] = player_mark

    def no_available_cells_remaining(self) -> bool:
        """
        Returns True if there are no empty cells to mark on the grid, False otherwise.

        :return: True if there are no empty cells to mark on the grid, False otherwise
        """
        return EMPTY_CELL not in self.grid

    def winner(self) -> Union[int, None]:
        """
        Returns the winner's id if there is one, returns None otherwise,
        assuming there is at most one winner.

        :return: identifier of the winner, None if there is none
        """
        winner = self.vertical_winner()
        if winner is None:
            winner = self.horizontal_winner()
            if winner is None:
                winner = self.diagonal_winner()

        return winner

    def vertical_winner(self) -> Union[int, None]:
        """
        Returns the vertical winner's id if there is one, returns None otherwise,
        assuming there is at most one vertical winner.

        :return: identifier of the vertical winner, None if there is none
        """
        # if columns are not long enough to win vertically, return None immediately
        if len(self.grid) < self.MARKS_TO_WIN:
            return None
        # search for a winner in every column
        for col in range(len(self.grid[0])):
            # counter of same lined marks on a column
            same_marks = 1
            for row in range(1, len(self.grid)):
                analyzed_mark = self.grid[row][col]
                if (analyzed_mark != EMPTY_CELL) & (analyzed_mark == self.grid[row - 1][col]):
                    same_marks += 1
                    if same_marks == self.MARKS_TO_WIN:
                        return analyzed_mark

    def horizontal_winner(self) -> Union[int, None]:
        """
        Returns the horizontal winner's id if there is one, returns None otherwise,
        assuming there is at most one horizontal winner.

        :return: identifier of the vertical winner, None if there is none
        """
        # if rows are not long enough to win horizontally, return None immediately
        if len(self.grid[0]) < self.MARKS_TO_WIN:
            return None
        # search for a winner in every raw
        for line in self.grid:
            same_marks = 1
            for i in range(1, len(line)):
                if (line[i] != EMPTY_CELL) & (line[i] == line[i - 1]):
                    same_marks += 1
                    if same_marks == self.MARKS_TO_WIN:
                        return line[i]
                else:  # reset same_marks
                    same_marks = 1

    def diagonal_winner(self) -> Union[int, None]:
        """
        Returns the diagonal winner's id if there is one, returns None otherwise,
        assuming there is at most one vertical winner.

        :return: identifier of the diagonal winner, None otherwise
        """
        ROWS = len(self.grid)
        COLUMNS = len(self.grid[0])

        for row_start in range(ROWS):
            # from up-left to down-right
            winner = self.winner_specific_diagonal(row_start, True, ROWS, COLUMNS, True, True)
            if winner is None:
                # from down-right to up-left
                winner = self.winner_specific_diagonal(row_start, True, ROWS, COLUMNS, False, True)
            if winner is not None:
                return winner
        for col_start in range(1, COLUMNS):
            # from up-left to down-right
            winner = self.winner_specific_diagonal(col_start, False, ROWS, COLUMNS, True, True)
            if winner is None:
                # from down-right to up-left
                winner = self.winner_specific_diagonal(col_start, False, ROWS, COLUMNS, False, True)
            if winner is not None:
                return winner
        # if no winner has been found, return None
        return None

    def winner_specific_diagonal(self, ref_start: int, ref_start_is_row: bool, rows: int, columns: int,
                                 left_to_right: bool, up_to_down: bool) -> Union[int, None]:
        """
        Returns the player who won specifically on the given diagonal, if there is one, assuming there is at most one.
        Returns None otherwise.

        :param ref_start: index of the line or column used as reference to indicate one of the cells at the edge of the
            grid, that together with the direction given as parameter, identifies the diagonal to scan
        :param ref_start_is_row: boolean that indicates whether the reference to the start of the diagonal is a row or
            a column
        :param rows: number of rows on the grid
        :param columns: number of columns on the grid
        :param left_to_right: boolean that indicates whether the diagonal scan, starting from the position of reference,
            proceeds from left to right or vice versa
        :param up_to_down: boolean that indicates whether the diagonal scan, starting from the position of reference,
            proceeds from up to down or vice versa
        :return: the player who won specifically on the given diagonal, if there is one, None otherwise
        """
        # set parameters for ranges of the following loop
        # set steps for range (+1 or -1) and indexes of first/last rows and columns
        # for rows
        if up_to_down:
            step_row = 1
            row_end = rows - 1
        else:
            step_row = -1
            row_end = 0  # because it goes backwards
        # for columns
        if left_to_right:
            step_column = 1
            col_end = columns - 1
        else:
            step_column = -1
            col_end = 0  # because it goes backwards
        # set range for rows and columns in the following loop
        if ref_start_is_row:
            row_start = ref_start
            # set start columns
            if left_to_right:
                col_start = 0
            else:
                col_start = columns - 1  # last column
        else:  # ref_start is a column
            col_start = ref_start
            # set start rows
            if up_to_down:
                row_start = 0
            else:
                row_start = rows - 1
        """
        The following loop scans the cells of the specific diagonal comparing every cell to the previous,
        that is why the loop starts with the second cell of the diagonal.
        For the same reason, the counter of aligned cells of the same user will start from 1 instead of 0,  
        because it increases its value of one every time there is a mach, but the first match between cells will 
        identify two cells aligned.
        """
        same_marks = 1
        # search for winner in the specific diagonal
        for row, col in zip(
                range(row_start + step_row, row_end + step_row, step_row),  # row
                range(col_start + step_column, col_end + step_column, step_column)):   # col
            if (self.grid[row][col] != EMPTY_CELL) & (self.grid[row][col] == self.grid[row - step_row][col - step_column]):
                same_marks += 1
                if same_marks == self.MARKS_TO_WIN:
                    return self.grid[row][col]
            else:  # reset counter to 1
                same_marks = 1
        # if no winner has been found, return None
        return None
