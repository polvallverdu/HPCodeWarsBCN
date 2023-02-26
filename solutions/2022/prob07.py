a = int(input())
b = int(input())

num = a

for _ in range(b):
  for l in str(num):
    num += int(l)
  
print(num)
