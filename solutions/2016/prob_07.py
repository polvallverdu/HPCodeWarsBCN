
time = input()
lista_bin = list()
lista_vertical = ['', '', '', '', ]
hora_bin = list()
time = time.replace(':', '')

for x in time:
    x = bin(int(x))
    lista_bin.append(x[2:])

for x in range(len(lista_bin)):
    lista_bin[x] = '0'*(4-len(str(lista_bin[x]))) + str(lista_bin[x])

posicion = 0
for x in range(4):
    lista_vertical[x] = lista_bin[0][posicion]+lista_bin[1][posicion] + \
        lista_bin[2][posicion]+lista_bin[3][posicion] + \
        lista_bin[4][posicion]+lista_bin[5][posicion]
    posicion += 1
posicion_1 = 0
for x in lista_vertical:
    hora = ''
    for y in x:
        if y == '0':
            x = '-'
        else:
            x = 'o'
        hora += x
    hora_bin.append(hora)


for x in hora_bin:
    print(' '.join(x))
