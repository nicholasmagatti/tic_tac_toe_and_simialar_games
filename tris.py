import random

EMPTY_CELL = 0

NONE_OF_THE_PLAYERS = 0
# they have to be successive numbers
USER_ID = 1
COMPUTER_ID = 2

matrix = [
    [EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
    [EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
    [EMPTY_CELL, EMPTY_CELL, EMPTY_CELL]
]


def display_matrix():
    for i in range(0, len(matrix)):
        print(matrix[i])


# requires turn_of_player == USER_ID || turn_of_player == COMPUTER_ID
def change_turn():
    global turn_of_player
    if turn_of_player == USER_ID:
        turn_of_player = COMPUTER_ID
    else:
        turn_of_player = USER_ID


# Keep asking the user to insert an input until it is acceptable,
# then return the input as an int
def custom_input(message_before_input, acceptable_inputs):
    acceptable = False
    # convert acceptable_inputs in strings
    [str(elem) for elem in acceptable_inputs]
    while not acceptable:
        input_received = int(input(message_before_input))
        if isinstance(input_received, int):
            if input_received in acceptable_inputs:
                acceptable = True
            else:
                print("Illegal input.")
    return input_received


def random_move_computer():
    line = random.choice(available_lines())
    column = random.choice(available_columns_on_specified_line(line))
    make_move(line, column, COMPUTER_ID)


def computer_turn():
    print("It's your opponent turn.")
    random_move_computer()


def available_lines():
    markable_lines = []
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            if (matrix[i][j] == NONE_OF_THE_PLAYERS) & (i not in markable_lines):
                markable_lines.append(i)
    return markable_lines


def available_columns_on_specified_line(line):
    available_columns = []
    for col in range(0, len(matrix[line])):
        if (matrix[line][col] == NONE_OF_THE_PLAYERS) & (col not in available_columns):
            available_columns.append(col)
    return available_columns


def make_move(line, column, player_mark):
    matrix[line][column] = player_mark


def add_n_to_each_element(n, list_par):
    return list(map(lambda x: x + n, list_par))


def manage_user_move():
    acceptable_lines = available_lines()
    # making elements start from 1 instead of 0
    # acceptable_lines = list(map(lambda x: x + 1, acceptable_lines))
    acceptable_lines = add_n_to_each_element(1, acceptable_lines)
    # less one to make it start from 0 instead of 1
    chosen_line = custom_input("line: ", acceptable_lines) - 1
    available_columns = available_columns_on_specified_line(chosen_line)
    # making elements start from 1 instead of 0
    available_columns = add_n_to_each_element(1, available_columns)
    # less one to make it start from 0 instead of 1
    chosen_col = custom_input("column: ", available_columns) - 1

    make_move(chosen_line, chosen_col, USER_ID)


def user_turn():
    print("It's your turn.")
    print("Type line and column of the spot you want to mark.")
    manage_user_move()


# Return the winner id if there is one, the NONE_OF_THE_PLAYERS number otherwise
def winner():
    # find winner in lines (horizontal win)
    for line in matrix:
        same_marks = 1
        while line[0] == line[same_marks]:
            same_marks += 1
            if same_marks == len(line):
                return line[0]

    # find winner in columns (vertical win)
    for col in range(len(matrix[0])-1):
        same_marks = 1
        for row in range(1, len(matrix)):
            if matrix[row][col] == matrix[0][col]:
                same_marks += 1
            if same_marks == len(matrix):
                return matrix[0][col]

    # find winner in diagonal
    # under the hypothesis that the matrix is a square
    # first diagonal
    same_marks = 1
    for i in range(1, len(matrix)):
        if matrix[0][0] == matrix[i][i]:
            same_marks += 1
        if same_marks == len(matrix):
            return matrix[0][0]

    # second diagonal
    same_marks += 1
    index_max = len(matrix) - 1
    for i in range(len(matrix)):
        if matrix[0][index_max] == matrix[i][index_max - i]:
            same_marks += 1
        if same_marks == len(matrix):
            return matrix[0][0]

    # if no winner has been found
    return NONE_OF_THE_PLAYERS


def manage_current_turn():
    if turn_of_player == USER_ID:
        user_turn()
    else:
        computer_turn()


# execution

print("TRIS")
print("You are the player number 1.")
print("The game starts now!")

turn_of_player = random.randint(USER_ID, COMPUTER_ID)


while winner() == NONE_OF_THE_PLAYERS:
    display_matrix()
    manage_current_turn()
    change_turn()

display_matrix()
winner = winner()
if winner == USER_ID:
    print("You won!!!")
elif winner == COMPUTER_ID:
    print("You lost.")
else:
    print("Error: something went wrong!")



