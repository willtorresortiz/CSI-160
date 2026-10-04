num = [1, 2, 1, 7, 3, 1, 4, 5, 6, 7, 7, 8, 11, 34, 56, 78, 3, 7, 9]
def print_even(numbers):
    """Prints the even numbers in a list, one per line
    :param numbers: (list) list of integers
    :return: None
    """
    for i in numbers:
        if(i % 2 == 0):
            print(i)
# usage
print_even(num)
