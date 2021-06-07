rawnumbers = [input(), input(), input()]
numbers = list()

for line in rawnumbers:
    rawnums = line.split(' ')
    for num in rawnums:
        numbers.append(int(num))

missing = list()
for x in range(1, 10):
    if x not in numbers:
        missing.append(x)

if len(missing) == 0:
    print("This is a valid sudoku")
else:
    print("This is an invalid sudoku. Missing numbers are:")
    for num in missing:
        print(num)

