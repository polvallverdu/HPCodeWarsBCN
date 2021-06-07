columns = int(input())
numbers_to_get = 0
numbers_gotten = list()

for x in range(1, columns+1):
    numbers_to_get += x

count = 1
counter = 0
while counter != numbers_to_get:
    if count % 2 != 0:
        numbers_gotten.append(count)
        count += 1
    counter += 1

total = 0
for num in numbers_gotten:
    total += num

print(total)
