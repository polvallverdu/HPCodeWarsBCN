import sys

inputs = list()

for line in sys.stdin: 
    if line.replace("\n", "") == "0": 
        break
    inputs.append(int(line))

a = str(inputs)

for num in inputs:
     b = a ([0] + [-1])
     c = a ([1] + [-2])
     if b == c:
          print(num, "is a balanced number")
     else:
          print(num, "is not a balanced number")


