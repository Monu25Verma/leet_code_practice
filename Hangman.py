# list of word, # select the char to field the words
# user will get the choice # chances(0< words>)


import random
from words import words
import string


def user_input(words_val):
    word = random.choice(words_val)
    while '_' in word or ' ' in word:
        word = random.choice(words_val)
    return word


def hangman():
    word = user_input(words)
    word_letter = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    while len(word_letter) > 0:
        print('you have use the letter: ', ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('current word: ', ' '.join(word_list))

        used_letter = input("guess a letter: ").upper()
        if used_letter in alphabet - used_letters:
            used_letters.add(used_letter)
            if used_letter in word_letter:
                word_letter.remove(used_letter)

        elif used_letter in used_letters:
            print('you have already used that character. please try again ')
        else:
            print("invalid character. please try again ")


user_input = input("type something: ")
print(hangman)




