'''
Author: William Torres Ortiz
Date: 09-18-2026
Program: Determines whether a given Hebrew calendar year is a leap year by checking its position in the 19-year cycle.
'''
# Get year from user to be called by functioned
while True:
    try:
        current_year = int(input("Input the current year as an integer: "))
        break
    except ValueError:
        print("Please input a valid integer.")

# Function defined as instructed in Assignment details
def is_hebrew_leap_year(year):
    '''Takes year argument, divides it by 19 and determines if Hebrew calendar leap year.'''
    leap_years = [0,3,6,8,11,14,17] # list of remainders that would constitute a hebrew leap year.
    remainder = year % 19 # calculate remainder of current year divided by 19
    return remainder in leap_years

# call function and take returned value as variable result
result = is_hebrew_leap_year(current_year)

# print result
print(result)
