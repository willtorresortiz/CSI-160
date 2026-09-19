def calculate_tax(price, tax_rate=0.08):
    return price * tax_rate

def calculate_total(price, tax):
    return price + tax

# The values are handed back and saved into variables
subtotal = 100.00
item_tax = calculate_tax(subtotal)
final_total = calculate_total(subtotal, item_tax)

print("Tax paid is", item_tax)
print("Total spent: $"+str(final_total))  # Total spent: $108.0


def find_first_even(numbers):
    for num in numbers:
        if num % 2 == 0: #The % is the modulus symbol. It does the division and returns the remainder
            return num  # Function ends immediately here when found

    return None  # Only reached if the loop finishes with no evens found

def get_min_max(numbers):
    lowest = min(numbers)
    highest = max(numbers)
    return lowest, highest  # Returns both values as a tuple

# Unpacking the list into separate variables
smallest, largest = get_min_max([42, 7, 19, 88, 3])
print("Min:",smallest, "Max:",largest)  # Min: 3, Max: 88

print(find_first_even([1, 3, 7, 8, 11, 12]))  # Outputs: 8

print(14//3) #Rounds down with no decimal or remainder available

print("The remainder of 14/3 equals:",14%3) #Returns the remainder