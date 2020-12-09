from colorama import init
init()
from colorama import Back, Style

import random


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
    if player_word == word_to_guess:
        return True


def get_random_word():
    random_words = ["CITRON", "ORANGE", "ETOILE", "JARDIN", "TOMATE", "COULIS", "BRIQUE", "STUDIO", "OIGNON", "RAISON", "ACCENT", "CHLORE", "SIMPLE"]
    return random.choice(random_words)


#Programme principal

word_to_guess = get_random_word()

for turn in range(8):
    player_word = input("Entrez un mot : ").upper()
    check_word(player_word, word_to_guess)
    print(Style.RESET_ALL)
    if check_win(player_word, word_to_guess):
        print("Gagné !")
        break
else:
    print("Perdu")