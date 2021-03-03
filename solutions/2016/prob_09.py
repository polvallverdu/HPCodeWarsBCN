import sys
import operator

tiempo = dict()


def solution(inputs: list):
    for x in inputs:
        nombre, num1, num2 = x.split()

        tiempo[nombre] = int(num1)/int(num2)

    tiempo_ord = sorted(
        tiempo.items(), key=operator.itemgetter(1), reverse=False)

    posicion = 0
    for x in tiempo_ord:
        print(f'{tiempo_ord[posicion][0]} {int(tiempo_ord[posicion][1])}')
        posicion += 1


def get_inputs() -> list:
    inputs = list()

    for line in sys.stdin:
        line = line.replace('\n', '').replace('\r', '')
        if line == '.':
            break

        inputs.append(str(line))

    return inputs


solution(get_inputs())
