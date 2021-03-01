import sys

inputs = list()

for line in sys.stdin: 
    if line.replace("\n", "") == "0": 
        break
    inputs.append(int(line))

