lineas = ['', '', '', '', '']
columna = ['', '', '', '', '']

lineas[0] = input()
lineas[1] = input()
lineas[2] = input()
lineas[3] = input()
lineas[4] = input()

for i in range(5):
    columna[i] = lineas[0][i] + lineas[1][i] + \
        lineas[2][i]+lineas[3][i]+lineas[4][i]

if (lineas[0] == lineas[4][::-1] and lineas[1] == lineas[3][::-1] and lineas[2] ==
    lineas[2][::1] and
    columna[0] == columna[4][::-1] and columna[1] == columna[3][::-1] and
    columna[2] == columna[2][::-1] and
    lineas[0] == columna[0] and lineas[1] == columna[1] and lineas[2] ==
        columna[2] and lineas[3] == columna[3] and lineas[4] == columna[4]):
    print("Magic Square like Sator Arepo")
else:
    print("Not a Magic Square")
