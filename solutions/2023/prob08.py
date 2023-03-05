a = int(input())
count = 0
while True:
  print(f"{a} -> ", end="")
  if a%2==0: #par
    a = a//2
  else:
    a = (a*3)+1
  count+=1
  
  if a <= 1:
    print(f"{a} [{count}]")
    exit()