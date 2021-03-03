control = 0
lista_numeros = []

while control == 0:
    line = ''
    try:
        line = input()
    except:
        control = 1
    if line == '':
        control = 1
    else:
        lista_numeros.append(line)

for numero in lista_numeros:
    numero += numero[0]
    sum = 0
    for index in range(len(numero)-1):
        digit = int(numero[index])
        next_digit = int(numero[index+1])
        if digit == next_digit:
            if digit % 2 == 0:
                sum += (index+1)*digit
            else:
                sum += digit
    print(sum)
