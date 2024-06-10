"""
Your job is to complete the definitions of each function mentioned in the comments so that it achieves its indicated behavior.

Do not run this file directly.
Rather, call whichever functions defined in this file that you want to run from within the file named main.py and run that file directly.
"""

import random

##--------------------- Function #1 ---------------------##
# Define a function named 'get_random_int'.  
# This function accepts two arguments: a minimum value and a maximum value.
# The function must return a random integer between these two values, inclusive.
# Use the function random.randint() to generate the pseudo-random number.

def get_random_int(minimum, maximum):
    return(random.randint(minimum,maximum))


##--------------------- Function #2 ---------------------##
# Define a function named 'get_guess'.
# This function accepts a single argument - an integer that serves as a max value.
# This function asks the user once to guess a random integer between 1 and the max value, inclusive.
# The function calls the function named get_random_int in order to generate the random integer in this range.
# If the user has entered an invalid response (i.e. anything that is not an integer in this range), the function returns an integer, -1.
# If the user has guessed the random integer correctly, this function returns a boolean True.
# If the user has guessed incorrectly, this function returns a boolean False.

def get_guess(max_value):
    user_guess = input("Guess a number between 1 and the max value")
    random_number = get_random_int(1, max_value)
    if not user_guess.isnumeric():
        return(-1)
    elif int(user_guess) < 1 or int(user_guess) > max_value:
        return(-1)
    elif int(user_guess) == random_number:
        return(True)
    elif int(user_guess) != random_number:
        return(False)
##--------------------- Function #3 ---------------------##
# Define a function named 'play_game'.
# This function does not accept any arguments.
# This function uses the get_guess function to ask the user four times to guess a random integer between 1 and 5, inclusive.
# Each time the user guesses, they are immediately informed whether they guessed correctly or not, with the printed output, "Correct!" or "Wrong!"
# If at any time, the user enters an invalid response, the program immediately prints out the text, "Invalid response!" and does not print out anything further.
# At the end, the function, assuming the user has entered all valid guesses, the program prints out the percent of guesses that user guessed correctly, following the format: "You guessed 75% of the random numbers correctly."

def play_game():
    correct_count = 0
    times_played = 0
    while (times_played < 4):
        guess = get_guess(5)
        if guess is True:
            print("Correct!")
            correct_count = correct_count + 1
            times_played = times_played + 1
        elif guess is False:
            print("Wrong!")
            times_played = times_played + 1
        else:
            print("Invalid response!")
            break
            
    if times_played == 4:
        print("You guessed " + str(int(correct_count * 100 /4)) + '% of the random numbers correctly.')

