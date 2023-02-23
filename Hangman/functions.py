
import sys
import os

##
# Functions
##

# Creates a placeholder for the given word
def create_placeholder(expected_word):
    length = len(expected_word)
    return '_' * length

# updates the placeholder with the found char and returns it
def update_placeholder_with(found_char, placeholder, expected_word):
    result = ""
    index = 0
    for i in expected_word:
        result += found_char if i == found_char else placeholder[index]
        index += 1
    return result


# checks if the given char is in the expected word
def check_if_in_expected_word(char, expected_word):
    result = True if char in expected_word else False
    return result


# tries to get the first position of the given value string
def convert_to_char(value):
    try:
        # return only the first char if possible
        return str(value)[:1]
    except:
        e = sys.exc_info()[0]
        print(e.with_traceback)

# clears the console depending on used OS
def clear():
    os.system("clear" if os.name == "posix" else "cls" )