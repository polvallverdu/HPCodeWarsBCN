a = int(input())

for _ in range(a):
  b = input().split(" ")
  name = b[0]
  b.remove(b[0])
  numbers = " ".join(b)
  x, y = numbers.split(" # ")
  x = x.split(" ")
  y = y.split(" ")
  y.reverse()
  if x == y:
    print(f"{name} has same number of steps for both faces")
  else:
    print(f"{name} has NOT same number of steps for both faces")