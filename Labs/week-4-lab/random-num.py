'''
Author: William Torres Ortiz
Date: 09-17-2026
Program: starts with generating a random number, takes user guess and compares it with random number. Informs user when correct and incorrect
'''
# Import methods
from random import randint

# Get random number and assign to variable between 0-9
random_num = randint(0,9)

# While loop to get and validate int input from user
while True:
    try:
        # Prompt user for integer input, if valid breaks loop
        user_guess = int(input("Input your guess as an integer: "))
        break
    except ValueError:
        # If invalid number prints and restarts loop
        print("Please input a valid integer.")

def compare_guess():
    '''Compares the user's guess to the randomly generated number and informs the user whether the guess is correct.'''
    if user_guess == random_num:
        # Prints only when user guess is RIGHT
        print("Your guess was CORRECT")
        print(f'The random number was {random_num}!!')
    else:
        # prints when WRONG
        print("Incorrect guess.")
        print(f"Random number was {random_num}")

# Call function
compare_guess()
