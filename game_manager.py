import random
from constants import *
from user_input_manager import *


class GameManager:

    # array_players contains an array of int numbers, that identify each player
    def __init__(self, rows: int, columns: int, marks_to_win: int, players: list, computer_difficulty=None):
        self.MARKS_TO_WIN = marks_to_win
        self.players = players
        # initialize the matrix (representing the board)
        self.matrix = [[EMPTY_CELL]*columns for r in range(rows)]
        self.COMPUTER_DIFFICULTY_LEVEL = computer_difficulty
        self.player_of_current_turn = players[0]

    def start_game(self):
        while (self.winner() is None) & (not self.is_tie()):
            self.display_matrix()
            self.manage_current_turn()
            self.change_turn()

        self.display_matrix()
        winner = self.winner()
        if self.is_tie():
            print("Tie. Nobody won.")
        else:
            print("The player number " + str(winner) + " won!!!")

    def change_turn(self):
        index_player_current_turn = self.players.index(self.player_of_current_turn)
        if index_player_current_turn == len(self.players) - 1:
            self.player_of_current_turn = self.players[0]
        else:
            self.player_of_current_turn = self.players[index_player_current_turn + 1]

    def manage_current_turn(self):
        player_number = self.player_of_current_turn.get_id()
        if self.player_of_current_turn.is_human():
            # uppercase only first letter of the name
            name_to_print = self.player_of_current_turn.name
            name_to_print = name_to_print[0].upper() + name_to_print[1:]
            print(name_to_print + ": it's your turn!")
            print("You are the number " + str(player_number) + ".")
            self.make_user_move(player_number)
        else:
            print("Turn of the player number " + str(player_number))
            self.make_automatic_player_move()

    def make_user_move(self, user_number: int):
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

        self.make_move_if_empty_cell(chosen_line, chosen_col, user_number)

    def make_automatic_player_move(self):
        mode = self.player_of_current_turn.difficulty_level
        if mode == DIFFICULTY_LEVEL_RANDOM:
            line = random.choice(self.available_lines())
            column = random.choice(self.available_columns_on_specified_line(line))
            self.make_move_if_empty_cell(line, column, self.player_of_current_turn.get_id())

    def display_matrix(self):
        for i in range(0, len(self.matrix)):
            print(self.matrix[i])

    def get_matrix_copy(self):
        return self.matrix.copy()

    def is_tie(self):
        for line in self.matrix:
            if EMPTY_CELL in line:
                return False
        return True

    def available_lines(self):
        markable_lines = []
        for i in range(0, len(self.matrix)):
            for j in range(0, len(self.matrix[i])):
                if (self.matrix[i][j] == EMPTY_CELL) & (i not in markable_lines):
                    markable_lines.append(i)
        return markable_lines

    def available_columns_on_specified_line(self, line):
        available_columns = []
        for col in range(0, len(self.matrix[line])):
            if (self.matrix[line][col] == EMPTY_CELL) & (col not in available_columns):
                available_columns.append(col)
        return available_columns

    def make_move_if_empty_cell(self, line, column, player_mark):
        if self.matrix[line][column] != EMPTY_CELL:
            raise Exception("The chosen cell is not empty.")
        self.matrix[line][column] = player_mark

    def no_available_cells_remaining(self):
        return EMPTY_CELL not in self.matrix

    # Return the winner id if there is one, return None otherwise
    def winner(self):

        # find winner in lines (horizontal win)
        for line in self.matrix:
            same_marks = 1
            for i in range(1, len(line)):
                if (line[i] != EMPTY_CELL) & (line[i] == line[i-1]):
                    same_marks += 1
                    if same_marks == self.MARKS_TO_WIN:
                        return line[i]
                else:  # reset same_marks
                    same_marks = 1

        # find winner in columns (vertical win)
        for col in range(len(self.matrix[0]) - 1):
            same_marks = 1
            for row in range(1, len(self.matrix)):
                analyzed_mark = self.matrix[row][col]
                if (analyzed_mark != EMPTY_CELL) & (analyzed_mark == self.matrix[row - 1][col]):
                    same_marks += 1
                    if same_marks == self.MARKS_TO_WIN:
                        return analyzed_mark

        """ Find winner in first diagonal:
            [1, 0, 0]
            [0, 1, 0]
            [0, 0, 1]
        """
        # TODO not necessarily starting from matrix[0][0]
        """
        same_marks = 1
        mark = self.matrix[0][0]
        if mark != EMPTY_CELL:
            for i in range(1, len(self.matrix)):
                if mark == self.matrix[i][i]:
                    same_marks += 1
                if same_marks == self.MARKS_TO_WIN:
                    return mark
        """
        """ Find winner in second diagonal:
                    [0, 0, 1]
                    [0, 1, 0]
                    [1, 0, 0]
        """
        # TODO not necessarily starting from matrix[0][index_max]
        """
        same_marks += 1
        index_max = len(self.matrix) - 1
        mark = self.matrix[0][index_max]
        for i in range(len(self.matrix)):
            if mark == self.matrix[i][index_max - i]:
                same_marks += 1
            if same_marks == self.MARKS_TO_WIN:
                return mark
        """
        # if no winner has been found
        return None
