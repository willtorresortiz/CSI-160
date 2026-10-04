# Loop 5. Comma Code
listToPrint = []
while True:
    newWord = input("Enter a word to add to the list (press return to stop adding words): ")
    if newWord == "":
        break
    else:
        listToPrint.append(newWord)
for index,item in enumerate(listToPrint):
    if index == len(listToPrint) - 1:
        print(f'and {item}')
    else:
        print(f'{item}', end=", ")
