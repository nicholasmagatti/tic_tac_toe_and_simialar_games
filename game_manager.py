from constants import *


class GameManager:

    # array_players contains an array of int numbers, that identify each player
    def __init__(self, rows, columns, marks_to_win, array_players):
        self.MARKS_TO_WIN = marks_to_win
        self.players = array_players
        # initialize the matrix (representing the board)
        self.matrix = [[EMPTY_CELL]*columns for r in range(rows)]

    def display_matrix(self):
        for i in range(0, len(self.matrix)):
            print(self.matrix[i])

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

    def make_move(self, line, column, player_mark):
        self.matrix[line][column] = player_mark

    def no_available_cells_remaining(self):
        return EMPTY_CELL not in self.matrix

    # Return the winner id if there is one, return None otherwise
    def winner(self):
        # find winner in lines (horizontal win)
        for line in self.matrix:
            same_marks = 1
            mark = line[0]
            if mark != EMPTY_CELL:
                while mark == line[same_marks]:
                    same_marks += 1
                    if same_marks == self.MARKS_TO_WIN:
                        return mark

        # find winner in columns (vertical win)
        for col in range(len(self.matrix[0]) - 1):
            same_marks = 1
            mark = self.matrix[0][col]
            if mark != EMPTY_CELL:
                for row in range(1, len(self.matrix)):
                    if self.matrix[row][col] == mark:
                        same_marks += 1
                    if same_marks == self.MARKS_TO_WIN:
                        return mark

        # find winner in diagonal

        """ First diagonal:
            [1, 0, 0]
            [0, 1, 0]
            [0, 0, 1]
        """
        same_marks = 1
        mark = self.matrix[0][0]
        if mark != EMPTY_CELL:
            for i in range(1, len(self.matrix)):
                if mark == self.matrix[i][i]:
                    same_marks += 1
                if same_marks == self.MARKS_TO_WIN:
                    return mark

        """ Second diagonal:
                    [0, 0, 1]
                    [0, 1, 0]
                    [1, 0, 0]
        """
        # TODO fix bug: it does not work
        same_marks += 1
        index_max = len(self.matrix) - 1
        mark = self.matrix[0][index_max]
        for i in range(len(self.matrix)):
            if mark == self.matrix[i][index_max - i]:
                same_marks += 1
            if same_marks == self.MARKS_TO_WIN:
                return mark

        # if no winner has been found
        return None