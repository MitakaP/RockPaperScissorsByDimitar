import random
from colorama import Fore

rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'

player_wins = 0
player_draws = 0
computer_wins = 0

while True:

    player_move = input("Choose [R]ock, [P]aper or [S]cissors: ")

    if player_move == "R":
        player_move = rock
    elif player_move == "P":
        player_move = paper
    elif player_move == "S":
        player_move = scissors
    else:
        raise SystemExit(Fore.RED + "Invalid Input. Try again...")

    computer_random_number = random.randint(1, 3)

    computer_move = ""

    if computer_random_number == 1:
        computer_move = rock
    elif computer_random_number == 2:
        computer_move = paper
    else:
        computer_move = scissors

    print(Fore.BLUE + f"The computer chose {computer_move}.")

    if (player_move == rock and computer_move == scissors) or \
            (player_move == paper and computer_move == rock) or \
            (player_move == scissors and computer_move == paper):
        player_wins += 1
        print(Fore.GREEN + "You win!")
    elif player_move == computer_move:
        player_draws += 1
        print(Fore.YELLOW + "Draw!")
    else:
        computer_wins += 1
        print(Fore.RED + "You lose!")

    print(Fore.GREEN + "=====Scoreline=====")
    print(f"Wins: {player_wins}  Draws: {player_draws}  Losses: {computer_wins}")

    new_game = input(Fore.RESET + "Type [yes] to Play Again or [no] to quit: ")
    if new_game == "yes":
        continue
    elif new_game == "no":
        print(Fore.MAGENTA + "Thank you for playing! <3")
        break
