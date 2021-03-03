text = str(input())

upper = 0
low = 0
other = 0

for x in text:
    if (x.isupper()):
        upper += 1
    elif(x.islower()):
        low += 1
    elif(x != ''):
        other += 1
print('Mayusculas: ', upper)
print('Minusculas: ', low)
print('otros: ', other)
