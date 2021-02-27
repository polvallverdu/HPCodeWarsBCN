import sys

def is_prime(num: int) -> bool:
    if num <= 1:
        return False
    
    for i in range(2, num):
        if (num % i) == 0:  
            return False
    return True

inputs = list()

for line in sys.stdin: 
    if line.replace("\n", "") == "0": 
        break
    inputs.append(int(line))

for num in inputs:
    if is_prime(num):
        print(f"{num} is prime")
    else:
        print(f"{num} is not prime")
