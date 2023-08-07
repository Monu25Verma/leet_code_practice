# name = "Monu"
# company_name = 'infosys'
# mid = f"I am a girl {name:}, i work in {company_name:} company as a system engineer"
# print(mid)
import random
def guess(x):
    random_val = random.randint(1, x)
    guess = 0
    while guess != random_val:
        guess = int(input(f"enter the number between 1 to {x}: "))
        if guess < random_val:
            print("the number is to low")
        elif guess > random_val:
            print("the number is too high")
    print("congrats guess number is correct:", random_val)

def guess_computer(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'whet is your choice {guess}  (H),it is too high, (L) too low, (C) correct" : ')
        if feedback == 'h':
            guess = high - 1
        elif feedback == 'l':
            guess = low + 1
    print(f'yat! congratulation computer has guess  the correct number {guess}')

guess_computer(20)

guess(10)
