num = [1, 2, 1, 7, 3, 1, 4, 5, 6, 7, 7, 8, 11, 34, 56, 78, 3, 7, 9]

def sequentialSearch():
    #This part of the function searches and captures data from the list
    foundItem = [] # Holds the index position of each instance of the items
    find = int(input("What value are you looking for in list? "))
    count = 0 # Acts as a counter
    removedItems =[] # Takes removed data
    for x, y in enumerate(num):
        # print(f"The Index position: {x} and the item value is {y}")
        if(y == find):
            count += 1 # same as count = count + 1
            foundItem.append(x) # Drops in the index position here
        else:
            continue
    print(f'The Element {find} exists {count} times in the list.')
    print(f'There are {len(foundItem)} items in the foundItem list.')
    print(f'The index positions held in this list are {foundItem}.')
    # Now its time to remove the data after capture
    for i in range(count): # Cycles back to the beginning of the list as many times as the value of count.
        num.remove(find)
        removedItems.append(find)
    print(f'The revised num list is now {num}')
    print(f'the {len(removedItems)} removed items were {find}s')


    ans = input("Do you wish to return the item to its original position")
    ans = ans.lower()
    if(ans == 'yes' or ans == 'y'):
        putBack(find, foundItem)
    else:
        quit()
def putBack(find, foundItem):
    for i in foundItem:
        num.insert(i, find) #'i' is the index position, find is the value
    print(f'the list "num" has been restored: {num}')


sequentialSearch()
