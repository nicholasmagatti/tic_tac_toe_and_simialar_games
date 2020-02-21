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


def custom_input(message_before, acceptable_inputs):
    acceptable = False
    while not acceptable:
        input_received = int(input(message_before))
        if input_received in acceptable_inputs:
            acceptable = True
        else:
            print("Illegal input.")
    return input_received


# TODO
def computer_turn():
    print("It's your opponent turn.")


def available_lines():
    markable_lines = []
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            if matrix[i][j] == NONE_OF_THE_PLAYERS:
                markable_lines.append(i)
    return markable_lines


def available_columns_on_specified_line(line):
    available_columns = []
    for col in range(0, len(matrix[line])):
        if matrix[line][col] == NONE_OF_THE_PLAYERS:
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


# TODO
def user_turn():
    print("It's your turn.")
    print("Type line and column of the spot you want to mark.")
    manage_user_move()


# TODO
def someone_won():
    pass


# TODO
# Return the winner id if there is one, the NONE_OF_THE_PLAYERS number otherwise
def winner():
    return NONE_OF_THE_PLAYERS


def manage_current_turn():
    if turn_of_player == USER_ID:
        user_turn()
    else:
        computer_turn()


def user_interface_turn():
    winner_player = winner()
    # if there is still no winner
    if winner_player == NONE_OF_THE_PLAYERS:
        manage_current_turn()
    elif winner_player == USER_ID:
        print("You won!!!")
    elif winner_player == COMPUTER_ID:
        print("You lost!")
    else:
        print("Error. Something went wrong.")


# execution

print("TRIS")
print("You are the player number 1.")
print("The game starts now!")

turn_of_player = random.randint(USER_ID, COMPUTER_ID)


for i in range(1, 10):
    display_matrix()
    user_interface_turn()
    change_turn()
