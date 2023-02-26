a = int(input())

count = 0
for x in range(a, -1, -1):
  for letter in str(x):
    if letter == "5":
      count += 1

print(count)