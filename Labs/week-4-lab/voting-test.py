'''
Author: William Torres Ortiz
Date: 09-15-2026
Purpose: input age and determine if user is voting age or not
'''

def voting_age():
    '''Gets and validates user age as int and compares against voting age'''
    while True:
    # Take user age and convert to int, if not valid interger - loop until valid integer
        try:
            # Take integer from user
            age = int(input("Please enter your age: "))
            break
        except ValueError:
            # If not whole integer, print error handler and restart loop.
            print("Please enter a valid whole number.")
    #Validate if user is over 18 to vote
    if age >= 18:
        # Age over 18 - tell user they can vote
        print("You are of voting age.")
    else:
        # Let user know they cant vote yet, age less than 18
        print("You must be 18 to vote.")
