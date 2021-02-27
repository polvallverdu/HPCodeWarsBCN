import sys

columns = 0
last_column = 0
row = 0
triangle = False

for x in sys.stdin:
    last_column = columns
    x = x.lstrip()
    x = x.rstrip()
    if x != '':
        columns = len(x)
        if last_column != columns and row != 0:
            triangle = True
        row += 1
    else:
        break

if triangle:
    print('I see a triangle')
elif columns == row:
    print('I see a square')
else:
    print('I see a rectangle')
