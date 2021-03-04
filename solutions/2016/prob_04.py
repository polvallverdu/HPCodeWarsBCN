import sys
import math


def solution(inputs: list):

    for x in inputs:
        suma_par = 0
        suma_inpar = 0
        par = False
        inpar = True
        for y in x:
            if inpar == True:
                suma_inpar += int(y)
                inpar = False
                par = True
            else:
                suma_par += int(y)
                par = False
                inpar = True
        if suma_par == suma_inpar:
            print(f'{x} is a balanced number')
        else:
            print(f'{x} is not a balanced number')


def get_inputs() -> list:
    inputs = list()

    for line in sys.stdin:
        line = line.replace('\n', '').replace('\r', '')
        if line == "0":
            break

        inputs.append(str(line))

    return inputs


solution(get_inputs())
