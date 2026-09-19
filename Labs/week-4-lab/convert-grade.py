'''
Author: William Torres Ortiz
Date: 09-15-2026
Program: Take grade percentage as integer input and convert to letter grade according to Champlain College grading scale.
'''

# Take and Validate grade percentage as Int, loops until valid Int
while True:
    try:
        # Asks user for grade percentage as whole number, if valid breaks loop
        grade_percentage = int(input("Input grade percent as whole number: "))
        if grade_percentage < 0:
            print("Please enter a non-negative grade.")
            continue
        break
    except ValueError:
        # If not valid whole number, restart loop
        print("Please enter a valid whole number.")

# Take grade percentage and evaluate against Champlain college grading scale to pull grade letter
if grade_percentage >= 93:
    print("Your grade letter is an A")
elif grade_percentage >= 90:
    print("Your grade letter is an A-")
elif grade_percentage >= 87:
    print("Your grade letter is a B+")
elif grade_percentage >= 83:
    print("Your grade letter is a B")
elif grade_percentage >= 80:
    print("Your grade letter is a B-")
elif grade_percentage >= 77:
    print("Your grade letter is a C+")
elif grade_percentage >= 73:
    print("Your grade letter is a C")
elif grade_percentage >= 70:
    print("Your grade letter is a C-")
elif grade_percentage >= 67:
    print("Your grade letter is a D+")
elif grade_percentage >= 63:
    print("Your grade letter is a D")
elif grade_percentage >= 60:
    print("Your grade letter is a D-")
else:
    print("Your grade letter is an F")
