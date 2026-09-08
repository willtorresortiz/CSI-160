"""DESCRIPTION OF THE MODULE GOES HERE
Author: William Torres Ortiz
Class: CSI-160-01
Assignment: Week 2: Lab - Conversation with a Computer
Due Date: 9/7/2026

Certification of Authenticity:
I certify that this is entirely my own work, except where I have given
fully-documented references to the work of others. I understand the definition
and consequences of plagiarism and acknowledge that the assessor of this
assignment may, for the purpose of assessing this assignment:
- Reproduce this assignment and provide a copy to another member of academic
- staff; and/or Communicate a copy of this assignment to a plagiarism checking
- service (which may then retain a copy of this assignment on its database for
- the purpose of future plagiarism checking)
"""
#Import Modules
import sys
import time

#Dialogue functions

def conversation_greetings(): #Get user name + occupation
    user_name = str(input('Shopkeeper: “Ho there, traveler. Don\'t believe I\'ve seen your face around these parts. What do they call you?” \nTraveler: ')) #Get User name
    if (user_name == ''):
        print('Shopkeeper: "Alright. I\'ve heard enough, go upon your way now."')
        sys.exit("Error: you're boring and this program doesnt want to run anymore")
    user_occupation = str(input(f'Shopkeeper: "{user_name}, eh? I\'ll remember it. And what trade has a man like you wandering these roads?" \nInput your occupation Traveler: ')) #Get user occupation
    if (user_occupation == ''):
        print('Shopkeeper: "Not one to mince words are we?"')
        time.sleep(1)
        user_age = int(input('Shopkeeper: "Still, you look awfully young to be a traveler. How many winters have you seen?"\nTraveler: '))
    elif (user_occupation.lower() == 'adventurer') or (user_occupation.lower() == 'an adventurer') or (user_occupation.lower() == 'just an adventurer') or (user_occupation.lower() == 'im an adventurer'):
        print('Shopkeeper: "An Adventurer huh, dime a dozen trade isn\'t it. Every gung-ho adolescent these days calls themselves one."')
        time.sleep(1)
        user_age = int(input(f'Shopkeeper: "Still, you look awfully young to be a(n) {user_occupation.lower()}. How many winters have you seen?"\nTraveler: '))
    elif (user_occupation.lower() == 'knight') or (user_occupation.lower() == 'a knight') or (user_occupation.lower() == 'just a knight') or (user_occupation.lower() == 'im a knight'):
        print('Shopkeeper: "A sword-arm, then. Good. Roads have grown mean lately."')
        time.sleep(1)
        user_age = int(input(f'Shopkeeper: "Still, you look awfully young to be a(n) {user_occupation.lower()}. How many winters have you seen?"\nTraveler: '))
    elif (user_occupation.lower() == 'bard') or (user_occupation.lower() == 'a bard') or (user_occupation.lower() == 'just a bard') or (user_occupation.lower() == 'im a bard'):
        print('Shopkeeper: "A bard! If you\'re planning to sing, buy something first."')
        time.sleep(1)
        user_age = int(input(f'Shopkeeper: "Still, you look awfully young to be a(n) {user_occupation.lower()}. How many winters have you seen?"\nTraveler: '))
    elif (user_occupation.lower() == 'traveler') or (user_occupation.lower() == 'a traveler') or (user_occupation.lower() == 'just a traveler') or (user_occupation.lower() == 'im a traveler'):
        print('Shopkeeper: "No trade worth naming, huh."')
        time.sleep(1)
        user_age = int(input(f'Shopkeeper: "Still, you look awfully young to be a(n) {user_occupation.lower()}. How many winters have you seen?"\nTraveler: '))
    else:
        print(f'Shopkeeper: "A {user_occupation.lower()} huh? I can\'t say I recall that trade. Are you pulling my leg?"')
        time.sleep(1)
        user_age = int(input(f'Shopkeeper: "Still, you look awfully young to be a(n) {user_occupation.lower()}. How many winters have you seen?"\nTraveler: '))
    return user_age, user_occupation

#Variables
user_name = conversation_greetings()
user_occupation = ''
user_age = ''

#Print tests
# print(user_name)
conversation_greetings()
