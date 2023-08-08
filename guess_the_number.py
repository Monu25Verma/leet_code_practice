# name = "Monu"
# company_name = 'infosys'
# mid = f"I am a girl {name:}, i work in {company_name:} company as a system engineer"
# print(mid)
import random


def guess(x):
    random_val = random.randint(1, x)
    guess_val = 0
    while guess_val != random_val:
        guess_val = int(input(f"enter the number between 1 to {x}: "))
        if guess_val < random_val:
            print("the number is to low")
        elif guess_val > random_val:
            print("the number is too high")
    print("congrats guess number is correct:", random_val)


def guess_computer(x):
    low = 1
    high = x
    feedback = ''
    guess_val = 0
    while feedback != 'c':
        if low != high:
            guess_val = random.randint(low, high)
        else:
            guess_val = low
        feedback = input(f'whet is your choice {guess_val}  (H),it is too high, (L) too low, (C) correct" : ')
        if feedback == 'h':
            guess_val = high - 1
        elif feedback == 'l':
            guess_val = low + 1
    print(f'yat! congratulation computer has guess  the correct number {guess_val}')


guess_computer(20)

guess(10)
