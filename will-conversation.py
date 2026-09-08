"""
This module creates an interactive fantasy-themed conversation between a shopkeeper and a traveler.
It collects information from the user, reuses their responses throughout the dialogue, and performs calculations using numerical input gathered during the conversation.
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
        sys.exit("Error: you're boring and this program doesn't want to run anymore")
    user_occupation = str(input(f'Shopkeeper: "{user_name}, eh? I\'ll remember it. And what trade has a man like you wandering these roads?" \nInput your occupation Traveler: ')) #Get user occupation
    if (user_occupation == ''):
        print('Shopkeeper: "Not one to mince words are we?"')
        time.sleep(1)
    elif (user_occupation.lower() == 'adventurer') or (user_occupation.lower() == 'an adventurer') or (user_occupation.lower() == 'just an adventurer') or (user_occupation.lower() == 'im an adventurer'):
        print('Shopkeeper: "An Adventurer huh, dime a dozen trade isn\'t it. Every gung-ho adolescent these days calls themselves one."')
        time.sleep(1)
    elif (user_occupation.lower() == 'knight') or (user_occupation.lower() == 'a knight') or (user_occupation.lower() == 'just a knight') or (user_occupation.lower() == 'im a knight'):
        print('Shopkeeper: "A sword-arm, then. Good. Roads have grown mean lately."')
        time.sleep(1)
    elif (user_occupation.lower() == 'bard') or (user_occupation.lower() == 'a bard') or (user_occupation.lower() == 'just a bard') or (user_occupation.lower() == 'im a bard'):
        print('Shopkeeper: "A bard! If you\'re planning to sing, buy something first."')
        time.sleep(1)
    elif (user_occupation.lower() == 'traveler') or (user_occupation.lower() == 'a traveler') or (user_occupation.lower() == 'just a traveler') or (user_occupation.lower() == 'im a traveler'):
        print('Shopkeeper: "No trade worth naming, huh."')
        time.sleep(1)
    else:
        print(f'Shopkeeper: "A {user_occupation.lower()}, huh? I can\'t say I recall that trade. Are you pulling my leg?"')
        time.sleep(1)
    return user_name, user_occupation

def get_user_age(user_occupation): #Function to get age depending on occupational answer
    if (user_occupation == ""):
        user_age = int(input('Shopkeeper: "Keeping your secrets, eh? Fine by me. How many winters have you seen?"\nTraveler: '))
    else:
        user_age = int(input('Shopkeeper: "Still, you look awfully young to be wandering these roads. How many winters have you seen?"\nTraveler: '))
    if (user_age > 25):
        print(f'Shopkeeper: “{user_age} winters? Hmph. You\'ve seen your share of roads, then."')
    else:
        print(f'Shopkeeper: “{user_age} winters? Hmph. Younger than I expected.”')
    return user_age

def get_journey_data(): #Function to get journey data and average those out. first algorithmic thingy
    time.sleep(1)
    days_traveled = int(input('Shopkeeper: “So tell me, how many days have you been wandering these roads?”\nTraveler: '))
    time.sleep(1)
    miles_covered = float(input('Shopkeeper: “And how many miles have you covered in that time?”\nTraveler: '))
    average_covered = miles_covered / days_traveled
    print(f"Shopkeeper: “{miles_covered} miles in {days_traveled} days? That’s about {average_covered} miles each day. No wonder you look worn through.”")

def shop_scene():
    user_gold = float(input('Shopkeeper: "Well, enough about the road. How much gold are you carrying?"\nTraveler: '))
    time.sleep(1)
    user_buy_amount = int(input('Shopkeeper: “Healing draughts are 5 gold each. How many do you need?”\nTraveler: '))
    healing_draught_price = 5
    total_ordering_price = user_buy_amount * healing_draught_price
    user_remaining_gold = user_gold - total_ordering_price
    print(f'Shopkeeper: "{user_buy_amount} draughts, eh? That’ll be {total_ordering_price} gold."')
    time.sleep(1)
    print(f'Shopkeeper: "That leaves you with {user_remaining_gold} gold. Try not to spend it all in one place."')

#Print tests
# print(user_name)
# conversation_greetings()
# get_user_age(user_occupation)
# get_journey_data()

#final calls
user_name, user_occupation = conversation_greetings()
get_user_age(user_occupation)
get_journey_data()
shop_scene()
