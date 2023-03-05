abcd = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

i = input()
num = 0
for l in i:
  num+=abcd.index(l)

print(num)