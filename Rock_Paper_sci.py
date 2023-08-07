#rock paper scesior
# r > s, s> p, p > r
#both same return tie, else true false

import random

def game():
    user_choice = input('What is your choice: "r" for Rock , "s" for secior, "p" for paper: ')
    computer_chance = random.choice(['r','s','p'])

    if user_choice == computer_chance:
        print("It's a tie")

    if how_win(user_choice, computer_chance):
        return 'You wom!'

    return 'You lost!'
def how_win(apponent, player):
    if player == 'r' and apponent == 's':
        return True
    elif player == 's' and apponent == 'p':
        return True
    elif player == 'p' and apponent == 'r' :
        return True
    else:
        return False

print(game())
