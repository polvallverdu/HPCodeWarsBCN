abcd = list(input())
num = int(input())
words = []

for _ in range(num):
  words.append(input())
  
for word in words:
  cabd = abcd.copy()
  done = False
  for l in word.lower():
    if l not in cabd:
      print("No")
      done = True
      break
  if not done:
    print("Yes")