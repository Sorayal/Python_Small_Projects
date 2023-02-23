###
# own version
# Author: Sascha
###

import random
import graphics
import functions
from word_list import random_words as words

##
# Main algorythm
##

# Defining list to choose an expected word from it.
list_of_random_words = words

# Defining expected word and placeholder here
expected_word = random.choice(list_of_random_words)
placeholder = functions.create_placeholder(expected_word)

print(graphics.intro_logo)

lives = 6

while placeholder.find('_') != -1:
    value = input("Guess a letter: ")
    guessed = functions.convert_to_char(value)
    in_expected_word = functions.check_if_in_expected_word(guessed, expected_word)

    if in_expected_word:
        placeholder = functions.update_placeholder_with(guessed, placeholder, expected_word)
        print(placeholder)
    else:
        print(f"You guessed {guessed}, that's not in the word. You lose a life.")
        lives -= 1
        print("- - - - -" + graphics.life_process[lives])

    if(lives == 0):
        print("You lost!")
        break

print("Hangman finished")
input("Press any key to exit")
functions.clear()
