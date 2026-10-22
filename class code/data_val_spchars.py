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
'''
Passsword validation
- min 8 characters, max 12 characters
- mix of letters and numbers (At least one number, one letter)
- one and only one: ['!', '$', '&', '*']
'''
pswd = input('Enter a valid password: ')
length = len(pswd)
spchars = ['!', '$', '&', '*']

def valpswd1():
    count = 0
    for i in spchars:
        for k in pswd:
            if(k == i):
                count += 1
            else:
                pass
    if((length >= 8 or length <= 12) and count == 1):
        valpswd2()
    else:
        print("Process failed, invalid password.")

def valpswd2():
    count = 0
    for i in pswd:
        if i in spchars or i.isalnum():
            count += 1
    if(count == length):
        print("Valid password.")
    else:
        print("Validation failed.")

valpswd1()
