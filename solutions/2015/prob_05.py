import sys

inputs = list()

for line in sys.stdin:
    line = line.replace("\n", "")
    if line == "Palindrome!": 
        break
    inputs.append(line)

for sentence in inputs:
    if sentence == sentence[::-1]:
        print(f"\"{sentence}\" is a palindrome")
    else:
        print(f"\"{sentence}\" is not a palindrome")
