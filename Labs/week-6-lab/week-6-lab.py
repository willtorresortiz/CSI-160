import enum
from random import randint
import sys
# Loop 1. Area Codes
# phone = ['555-1234', '555-8945', '555-9632', '555-2587', '802-555-7532', '555-9512', '802-555-9173', '555-4562']
#
# def add_area_code(phone_numbers, area_code):
#     """Returns a list of phone numbers with the area code added.
#     Given a list of phone numbers that are missing the area code,
#     append the area code to the phone numbers in the list and return the result list.
#
#     :param phone_numbers: (list) A list of phone numbers (strings) that do not have the area code
#                                 Example: ['555-1212']
#     :param area_code: (str) The area code to add Example: '802'
#     :return: (list) A list of phone numbers with the area code Example: ['802-555-1212']
#     """
#     full_phone_numbers = []
#     for n in phone_numbers:
#         full_phone_numbers.append(area_code + '-' + n)
#     return full_phone_numbers
#
# # example usage
# phone_numbers = ['555-1212', '999-0738']
# with_area_code = add_area_code(phone_numbers, '802')
# print(with_area_code)

# Loop 2. Print even numbers
# num = [1, 2, 1, 7, 3, 1, 4, 5, 6, 7, 7, 8, 11, 34, 56, 78, 3, 7, 9]
# def print_even(numbers):
#     """Prints the even numbers in a list, one per line
#     :param numbers: (list) list of integers
#     :return: None
#     """
#     for i in numbers:
#         if(i % 2 == 0):
#             print(i)
# # usage
# print_even(num)

# # Loop 3. Guessing Game
# randomNum = randint(1,100)
# def guessing_game(randomNum):
#     # While loop to get and validate int input from user
#     while True:
#         try:
#             # Prompt user for integer input, if valid continues down
#             guess_num = int(input("What is your guess? "))
#         except ValueError:
#             # If invalid number prints and restarts loop
#             print("Please enter a valid integer.")
#             continue
#         if guess_num == randomNum:
#             print(f'CORRECT! The number was {randomNum}')
#             break
#         elif guess_num >= randomNum:
#             print('Your guess was higher! Try again!')
#             continue
#         else:
#             print('Your guess was lower! Try again!')
#             continue
#
# # Usage
# print(randomNum)
# guessing_game(randomNum)

# Loop 4. Backpack of Stuff
# itemsInBackpack = ["book", "computer", "keys", "travel mug"]
#
# while True:
#     print("Would you like to:")
#     print("1. Add an item to the backpack?")
#     print("2. Check if an item is in the backpack?")
#     print("3. Quit")
#     userChoice = input()
#
#     if(userChoice == "1"):
#         print("What item do you want to add to the backpack?")
#         itemToAdd = input()
#         itemsInBackpack.append(itemToAdd)
#         print(f'{itemToAdd} added to backpack!')
#         continue
#     if(userChoice == "2"):
#         print("What item do you want to check to see if it is in the backpack?")
#         itemToCheck = input()
#         if itemToCheck in itemsInBackpack:
#             print(f'{itemToCheck} is in the backpack')
#         else:
#             print(f'{itemToCheck} not found in backpack')
#         continue
#     if(userChoice == "3"):
#         sys.exit()

# Loop 5. Comma Code
# listToPrint = []
# while True:
#     newWord = input("Enter a word to add to the list (press return to stop adding words): ")
#     if newWord == "":
#         break
#     else:
#         listToPrint.append(newWord)
# for index,item in enumerate(listToPrint):
#     if index == len(listToPrint) - 1:
#         print(f'and {item}')
#     else:
#         print(f'{item}', end=", ")
