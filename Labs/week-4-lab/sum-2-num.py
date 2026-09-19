'''
Author: William Torres Ortiz
Date: 09-15-2026
Program: Take two numbers from user, make sum and compare to number 100, if less - print num, if more - print statement
'''

def get_valid_number(iteration):
    '''Prompts for a number and validates it as a float, reprompting on invalid input. Returns the validated float.'''
    while True:
        try:
            # Get float value from user and assigns to local number variable
            number = float(input(f"Input the {iteration} number: "))
            break
        except ValueError:
            # validates float value, if not float restarts loop
            print("Please enter a valid number: ")
    # return local function number to be called later
    return number

# Pull number value from function to 2 numbers
number1 = get_valid_number("first")
number2 = get_valid_number("second")

# Takes the numbers and checks sums, prints depending on sum.
if number1 + number2 > 100:
    # Print only IF sum of numbers higher than 100
    print("They add up to a big number")
else:
    # runs if sum is less than 100 adds numbers and saves to Total variable, prints value.
    total = number1 + number2
    print(f"They add up to {total}")
