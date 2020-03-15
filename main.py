import random
from game_manager import *
from user_input_manager import *


def main():
    print("Welcome!")
    while True:  # infinite loop
        print("Choose details for a new game:")
        lines = custom_int_input("Number of rows: ", range(3, 31))
        columns = custom_int_input("Number of columns: ", range(3, 31))
        marks_to_win_the_game = custom_int_input(
            "Marks to win the game: ",
            range(3, max(lines, columns) + 1))
        number_of_players = custom_int_input("Number of players: ", range(2, 10))
        number_of_human_users = custom_int_input("Number of human users: ", range(number_of_players + 1))
        print("Write the name of each user: ")
        username_list = []
        for n in range(number_of_human_users):
            acceptable_name_received = False
            while not acceptable_name_received:
                name_received = input("Username " + str(n + 1) + ": ")
                if name_received == "":
                    print("Error")
                elif name_received not in username_list:
                    acceptable_name_received = True
                    username_list.append(name_received)
                else:
                    print("This username is already taken")
        print("Choose the level of the players controlled by the computer: ")
        acceptable_inputs_difficulty_level = []
        if number_of_players > number_of_human_users:
            for i in range(0, len(DIFFICULTY_LEVELS)):
                print(i + 1, ":", DIFFICULTY_LEVELS[i])
                acceptable_inputs_difficulty_level.append(i)
            computer_difficulty_level = DIFFICULTY_LEVELS[
                custom_int_input("Chosen level: ",
                                 add_n_to_each_element(1, acceptable_inputs_difficulty_level)) - 1]
        # create the list of the players
        player_list = []
        # start from the users
        for name in username_list:
            player_list.append(Player(True, name))
        # add the other players (controlled by the computer)
        for i in range(number_of_players - number_of_human_users):
            player_list.append(Player(False))
        # shuffle order
        random.shuffle(player_list)
        # assign ids
        for i in range(1, len(player_list)):
            player_list[i].set_id(i)

        # set and start the game
        GameManager(lines, columns, marks_to_win_the_game, player_list).start()


if __name__ == '__main__':
    main()
