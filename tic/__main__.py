"""
Active Run File for the Tic Tac Toe Game

Author: Samuel Rodriguez
Date: 1/12/2021
"""
# Did tests already from tic import TicTester
from TicTacToeBuild import TicTacToeBuild
from Consts import *
def main_menu():
    """
    Hub controller of the game
    """
    print("\nMain Menu:\nPlease choose an option and select by pressing enter")
    menu_display = "\n[1] Play Game\t\t[2] Help Menu\t\t[3] Exit"
    user_input = valid_menu_option(menu_display, len(menu_items))
    if user_input != HELP:
        menu_items[user_input]()
    else:
        menu_items[user_input](False)

def help(is_game):
    """
    Provides information about how to play the game

    Parameter is_game: if help menu was triggered by the pause menu
    Precondition: is_game is a bool
    """
    assert type(is_game) == bool, "is_game is invalid type"
    print("RULES OF TIC TAC TOE!")
    print("\tTo move around your mark on the board, "
          "\n\tuse W (up) A (left) S (down) D (right)")
    print("\t-> The game is played on a grid that's n squares by n squares.")
    print("\t-> You can choose to be X or O, your friend "
          "(or the computer in this case) is the opposite")
    print("\t-> The first player to get n of her marks in a row "
          "\n\t(up, down, across, or diagonally) is the winner.")
    print("\t-> When all squares are full, the game is over.")
    if (is_game):
        print("\nPress any key and press enter to go back to pause menu")
        any_input = input("\t> ")
    else:
        print("\nPress any key and press enter to go back to the main menu")
        any_input = input("\t> ")
        main_menu()

def pause_menu():
    """
    Returns pause menu selection. Menu screen activated during in_game

    This menu screen allows players to resume game, start a new game, go to the help menu,
    or exit the game
    """
    print("GAME PAUSED")
    menu_display = "\n[1] New Game\t\t[2] Help Menu\t\t[3] Exit\t\t[4] Resume Game"
    user_input = valid_menu_option(menu_display, len(menu_items)+1)
    return user_input

def start():
    """
    Initial prompt for the game
    """
    print("Welcome to the Tic Tac Toe Game!\n\n")
    main_menu()

def in_game():
    """
    This method houses the core gameplay of the game
    """
    n = valid_n_input()
    player1, player2 = valid_player_input()

    print("Great! We can now begin the game.")

    # Setup done, start game
    game = TicTacToeBuild(n)
    game.printBoard()
    active = True
    count = 0
    currPlayer = player1
    user_prompt = ''
    pause_opt = ''
    game.startMark()
    while active:
        # Keep Track of who's turn it is
        print()
        if count % 2 == 0:
            currPlayer = player1
        else:
            currPlayer = player2
        if currPlayer == player1:
            user_prompt = "Player 1"
        else:
            user_prompt = "Player 2"
        print("%s Turn: " % user_prompt)

        print("\tIf you would like to pause/exit, type pause and press enter")
        user_i, user_j = next_move(game)
        print()
        if user_i == PAUSE_GAME:
            pause_opt = pause_menu()
            if pause_opt == PLAY_GAME:
                active = False
            if pause_opt == HELP:
                help(True)
            if pause_opt == EXIT:
                exit()
            # Skip iteration if input was RESUME_GAME
        else:
            game.move(user_i, user_j, currPlayer)
            game.printBoard()
            if game.gameOver():
                print("Game Over! %s wins!" % user_prompt)
                active = False
            elif game.tie():
                print("Game Over! Tie has occurred, DRAW")
                active = False
            count += 1
    if pause_opt == PLAY_GAME:
        in_game()
    else:
        main_menu()

def next_move(game):
    """
    Returns the move of the player using WASD keys
        or 'pause' if the player selected to pause the game

    Parameter game: the game being played
    Precondition: game is of class TicTacToeBuild
    """
    active = True
    # finds initial coordinates for the player to start on
    i, j = game.startMark()
    while (active):
        game.printBoard()
        user_input = valid_move()
        if user_input == "PAUSE":
            i = PAUSE_GAME
            j = PAUSE_GAME
            active = False
        elif user_input == '':
            active = False
            game.removeMark()
        else:
            game.removeMark()
            i, j = game.insertMark(user_input)
    return i, j

def valid_n_input():
    """
    Returns valid input for n from the user

    This method prompts the user to choose an n for the tic tac toe grid
    """
    n = 0
    print("\n\tTo start, please type the number of rows and columns to create an n x n grid:")
    incorrectInput = True
    while incorrectInput:
        try:
            n = int(input("\t\t> "))
            if n < 1:
                raise ValueError
            incorrectInput = False
            return n
        except ValueError:
            print("\t\tInvalid input, please type a number greater than 0")

def valid_player_input():
    """
    Returns valid 'X' and 'O' game pieces such that player 1
    and player 2 be assigned these pieces (they should not have the same
    game piece!)
    """
    player1 = ''
    player2 = ''
    print("Thanks! Now then, type X or O for Player 1's Game Piece: ")
    incorrectInput = True
    while incorrectInput:
        try:
            player1 = input("\t\t> ").upper()
            if player1 != 'O' and player1 != 'X':
                raise ValueError
            incorrectInput = False
        except ValueError:
            print("\t\tInvalid input, type X or O for Player 1's Game Piece: ")
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    print("OK. Player 1 is %s, so Player 2 is %s\n\n" % (player1, player2))
    return player1, player2

def valid_menu_option(menu_display, nOptions):
    """
    Returns the selected option from the menu
    While also ensuring a valid option was selected

    Parameter menu_display: the menu options to display
    Precondition: menu_display is a string

    Parameter nOptions: number of options available
    Precondition: nOptions is a positive int
    """
    assert type(nOptions) == int and nOptions > 0, "nOptions is invalid"
    assert type(menu_display) == str, "menu_display is invalid"
    user_input = 0
    incorrect_input = True
    while incorrect_input:
        try:
            print(menu_display)
            user_input = int(input("\t> "))
            if not 0 < user_input < nOptions+1:
                raise ValueError
            incorrect_input = False
            return user_input
        except ValueError:
            print("Invalid input, please try again")

def valid_move():
    """
    Returns one valid option to make when deciding to move their marker or pause
    """
    options = [UP, LEFT, DOWN, RIGHT, 'PAUSE', '']
    user_input = ''
    incorrect_input = True
    while (incorrect_input):
        try:
            print("If you would like this tile, simply press enter")
            user_input = input("\t> ").upper()
            if user_input not in options:
                raise ValueError
            incorrect_input = False
            return user_input
        except ValueError:
            print("Invalid input, please try again")





menu_items = {1: in_game, 2: help, 3: exit}


if __name__ == '__main__':
    start()
