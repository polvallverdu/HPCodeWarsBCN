import sys

text = str()

for line in sys.stdin:
    line = line.replace('\n', '').replace('\r', '')
    if line == '':
        break
    if text == '':
        text = line
    else:
        text = text + ' ' + line


posicion = 0
for x in text:
    if x == ' ':
        continue
    elif x == 'i' and text[posicion-1] == ' ' and text[posicion+1] == ' ':
        text[posicion] = x.upper
    elif x == '.':
        text[posicion + 2] == x.upper

print(text)
