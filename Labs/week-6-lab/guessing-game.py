from random import randint
# Loop 3. Guessing Game
randomNum = randint(1,100)
def guessing_game(randomNum):
    # While loop to get and validate int input from user
    while True:
        try:
            # Prompt user for integer input, if valid continues down
            guess_num = int(input("What is your guess? "))
        except ValueError:
            # If invalid number prints and restarts loop
            print("Please enter a valid integer.")
            continue
        if guess_num == randomNum:
            print(f'CORRECT! The number was {randomNum}')
            break
        elif guess_num >= randomNum:
            print('Your guess was higher! Try again!')
            continue
        else:
            print('Your guess was lower! Try again!')
            continue

# Usage
print(randomNum)
guessing_game(randomNum)
