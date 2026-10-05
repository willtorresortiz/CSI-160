num = [1, 2, 1, 7, 3, 7, 1, 4, 5, 6, 7, 7, 8, 11, 34, 56, 78, 3, 7, 9]
# Convert the list 'num' into a tuple
num_tuple = tuple(num)
print(num_tuple)

# take index of target and pop it to variable x
# target_index = num.index(56)
# x = num.pop(target_index)
# print(x)
# print(num)

'''
All of this fails, tuples are immutable (cant change them)
target_index2 = num_tuple.index(56)
x2 = num_tuple.pop(target_index2)
print(target_index2, x2)

'''

'''
This process will not work.
numSorted = num.sort()
print(numSorted)

Each process must be done individually as shown below
'''

# num2 = num # Passes the list 'num' to a new list, 'num2'. LINKED LISTS

numSorted = sorted(num) # Passes the list 'num' to a new list, 'numSorted'
# Now we can begin to execute binary search
def binarySearch():
    print(numSorted)
    x = int(input('Enter your search criteria: '))
    low = 0
    high = len(numSorted) - 1

    while low <= high:
        mid = low + (high - low)//2

        if(numSorted[mid] < x):
            print(numSorted[mid])
            break
        else:
            print()
            break

binarySearch()
