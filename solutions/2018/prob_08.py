import sys
suma = 0
for line in sys.stdin:
    data = line.split()
for i in data:
    suma = suma + (int(i)*1.6)
if suma >= 622:
    print("Yes")
else:
    print("No")
