
import math
thows = int(input())
goals = int(input())
tgoals = int(input())
totals = thows+goals*2+tgoals*3
shots = int(input())

print(f"{totals} {int(math.floor(((thows+goals+tgoals)/shots)*100))}%")