from colorama import init
init()
from colorama import Back, Style

import random

def get_letter_index(letter, word):
    for i in range(len(word)):
        if letter == word[i]:
            return i


def check_letter(letter, letter_index, player_word, word):
    if letter in word:
        if word[letter_index] == player_word[letter_index]:
            print(Back.RED + letter, end='')
            return
        print(Back.YELLOW + letter, end='')
        return
    print(Back.BLUE + letter, end='')


def check_word(player_word, word):
    for i in range(len(word)):
        check_letter(player_word[i], i, player_word, word)


def check_win(player_word, word_to_guess):
    guessed_letters_num = 0
    for i in range(len(word_to_guess)):
        if player_word[i] == word_to_guess[i]:
            guessed_letters_num += 1
    if guessed_letters_num == len(word_to_guess):
        return True


"""
def get_random_word():
    random_words = [""]
    return random.choice()
"""

print(check_win("abc", "abc"))