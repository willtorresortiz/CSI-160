from datetime import datetime
#Working with fstrings

firstname = 'John'
lastname = 'Doe'

greeting1 = "Hello",firstname," ",lastname # treated as tuple
greeting2 = "Hello,firstname," ",lastname" # treated as variable
#print(greeting1)
sentence = 'Hello {} {}.'.format(firstname,lastname)
welcome = f'Hello {firstname} {lastname}'
print(sentence)
#print('Hello',firstname,lastname)
#print(welcome)

birthday = datetime(2001,10,27)
today = f'John\'s birthday is {birthday:%B %d, %Y}'
print(today)
#########################################################
#String Formats - upper() and lower()

name = "John Doe"

name = name.lower()
print(name)

state = "vt"
state = state.upper()
print(state)

#########################################################
#Data Validation - string functions
'''
All functions return either a True or False

isalpha() - Confirm that all of the data is comprised of letters
            AND is not blank

isalnum() - Confirm that the data is either letters and/or numbers
            AND is not blank

isdecimal() - Confirms the data is comprised of all integers AND
              is not blank

isspace() - Confirms the data is comprised of spaces, tabs and
            new lines AND is not blank

istitle() - Confirms the data is all string and the first letter
            is upper case followed by lower case letters AND no
            blanks
'''
