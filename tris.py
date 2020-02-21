import random

EMPTY_CELL = 0
# they have to be successive numbers
USER_ID = 1
COMPUTER_ID = 2

turn_of_player = -1

matrix = [
    [EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
    [EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
    [EMPTY_CELL, EMPTY_CELL, EMPTY_CELL]
    ]

#requires turn_of_player == USER_ID || turn_of_player == COMPUTER_ID
def change_turn():
    global turn_of_player
    if turn_of_player == USER_ID:
        turn_of_player = COMPUTER_ID
    else:
        turn_of_player = USER_ID



#TODO
def computer_turn():
    print("It's your opponent turn.")

def user_turn():
    print("It's your turn.")


#TODO
def someone_won():
    pass

#TODO
def winner():
    pass

def manage_turn(turn_of_player):
    if(turn_of_player == USER_ID):
        user_turn()
    else:
        computer_turn()

def user_interface_turn(turn_of_player):

    if someone_won():
        if winner() == USER_ID:
            print("You won!!!")
        else:
            print("You lost!")
    else:
        manage_turn(turn_of_player)


#execution

print("TRIS")
print("The game starts now!")


turn_of_player = random.randint(USER_ID, COMPUTER_ID)

for i in range(1,10):
    user_interface_turn(turn_of_player)
    change_turn()

