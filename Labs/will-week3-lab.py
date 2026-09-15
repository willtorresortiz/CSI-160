"""
This module demonstrates three mathematical functions using parameters and returned values.
Author: William Torres Ortiz
Class: CSI-160-01
Assignment: Week 3: Lab
Due Date: 9/14/2026

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

# Variables for bill total function
balance = float(input("Input bill amount: "))
tip = float(input("Input tip amount in $: "))

def calculate_bill_total(balance, tip):
    """
    Calculates the total bill by adding the tip amount to the original balance.

    Arguments:
        balance: The original bill amount.
        tip: The dollar amount of the tip.

    Returns:
        The total bill amount after the tip is added.

    Assumptions and Conditions:
        balance and tip are numeric values and are not negative.
    """
    total = balance + tip
    return total

bill_total = calculate_bill_total(balance, tip)
print(bill_total)


# Variables for calculating days to seconds
days = int(input("Input number of days to convert to seconds: "))

def days_to_seconds(days):
    """
    Converts a number of days into the equivalent number of seconds.

    Arguments:
        days: The number of days to convert into seconds.

    Returns:
        The total number of seconds contained in the given number of days.

    Assumptions and Conditions:
        days is a numeric value and is not negative.
    """
    seconds = days * 86400
    return seconds

seconds = days_to_seconds(days)
print("The seconds in that number of days is ", seconds)


# Variables for calculating pay based on hourly rate
hourly_rate = float(input("Input your hourly rate to calculate pay with following hours worked: "))
hours_worked = float(input("Input hours to calculate pay: "))

def calculate_pay(rate, worked):
    """
    Calculates gross pay using an hourly rate and the number of hours worked.

    Arguments:
        rate: The amount of money earned per hour.
        worked: The total number of hours worked.

    Returns:
        The gross pay calculated from the hourly rate and hours worked.

    Assumptions and Conditions:
        rate and worked are numeric values and are not negative.
    """
    pay = rate * worked
    return pay

gross_pay = calculate_pay(hourly_rate, hours_worked)
print("Your gross pay is: ", gross_pay)
