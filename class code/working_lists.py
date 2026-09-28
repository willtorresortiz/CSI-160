num = [1, 2, 1, 7, 3, 1, 4, 5, 6, 7, 7, 8, 11, 34, 56, 78, 3, 7, 9]

#Loop through the list and locate the value in 'find'
#Output its index position
def findValue():
    find = int(input("What value are you searching for in the list?"))
    count = 0
    for i in num:
        if(i == find):
            idx = num.index(i)
            count = count + 1 #resetting variable value
        else:
            pass
    if (count > 0):
        print('Item found, index position equals', idx)
    else:
        print('Item not found in list.')

# findValue()
def findAllValues():
    find = int(input("What value are you searching for in the list?"))
    count = 0
    for k in num:
        if(k == find):
            count = count + 1 #resetting variable value
            continue
        else:
            continue
    if (count > 0):
        print(f'Item found {count} times')
    else:
        print('Value not found in list')

# findAllValues()

#Function that returns the count of a value AND each index position
def findIdxValues():
    find = int(input("What value are you searching for in the list?"))
    count = 0
    position = -1
    for i in num:
        position += 1
        if(i == find):
            print(f"item found, index position, {position}")
            count = count + 1 #resetting variable value
            continue
        else:
            continue
    if (count > 0):
        print(f'Item found {count} times')
    else:
        print('Value not found in list')

# findIdxValues()

# Function designed to identify a value and then remove it. Place
# each instance of the value in a list named foundItem[]
def removeItem():
    foundItem = []
    find = int(input("What value are you searching for in the list?"))
    count = 0
    for index,n in enumerate(num):
        if(n == find):
            count = count + 1 #resetting variable value
            continue
        else:
            continue
    for i in range(count): # Cycles back to the beginning of the list as many times as the value of count.
        num.remove(find)
        foundItem.append(find)
    print(num)
    print(foundItem)

removeItem()
