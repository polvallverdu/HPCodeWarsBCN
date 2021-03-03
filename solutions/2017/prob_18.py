import sys
import operator

inputs = dict()
nombre = str()
posicion = 0

for entrada in sys.stdin:
    entrada = entrada.replace('\n', '').replace('\r', '')
    num = float()

    is_name = True

    if entrada == '#':
        break
    try:
        num = float(entrada)
        is_name = False
    except:
        posicion = 0
    if is_name:
        nombre = entrada
        inputs[nombre] = float()
    else:
        inputs[nombre] += int(float(num))


for x in inputs:
    total_millas = inputs[x]
    points = 0
    if total_millas > 10000:
        if total_millas > 25000:
            if total_millas > 50000:
                points = 10000 + (15000*2) + (25000*3) + (total_millas-50000)*5
            else:
                points = 10000 + (15000*2) + (total_millas-25000)*3
        else:
            points = 10000 + (total_millas-10000)*2
    else:
        points = total_millas
    inputs[x] = points

inputs_ordenada = sorted(
    inputs.items(), key=operator.itemgetter(1), reverse=True)

for x in inputs_ordenada:
    print(
        f'{inputs_ordenada[posicion][0]} {int(inputs_ordenada[posicion][1])}')
    posicion += 1
