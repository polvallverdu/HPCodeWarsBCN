word = input().rstrip().lower()
checked = []
for char in word:
    if char in checked:
        print("Not an isogram")
        exit()
    checked.append(char)
print("Isogram detected")