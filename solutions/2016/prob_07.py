<<<<<<< HEAD
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
=======
def decimalToBinary(num):
    """This function converts decimal number
    to binary and prints it"""
    if num > 1:
        decimalToBinary(num // 2)
    return num % 2

time_24h = str(input()).replace(':', '')
time = list()
times_binary = list()

for char in time_24h:
     time.append(int(char))

for num in time:
     binary = str(decimalToBinary(num))
     binaryNums = list()
     for char in binary:
          binaryNums.append(char)

for x in range(6):
     to_print = ''
     for num in times_binary:
          if num[x] == 0:
               to_print += '-'
          else:
               to_print += 'o'
     print(to_print)
>>>>>>> bb138f27f174278e24adb2939c523606a2d8749f


for x in hora_bin:
    print(' '.join(x))
