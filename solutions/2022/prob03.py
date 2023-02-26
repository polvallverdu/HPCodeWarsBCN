products = int(input())
boxes = int(input())
left = int(input())

q = products/boxes
l = products%boxes

if left == l:
  print(f"CORRECT, the capacity of each box is {int(q)}")
else:
  print("INCORRECT")
