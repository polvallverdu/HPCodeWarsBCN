import sys

lista = dict()


def solution(inputs: list):
    for x in inputs:
        x = x.split(' ')
        ter1 = dar_var(x[2])
        ter2 = dar_var(x[4])
        op = x[3]
        lista[x[0]] = solucion_op(ter1, ter2, op)
        print(lista[x[0]])


def solucion_op(n1, n2, op):
    if op == '+':
        return n1+n2
    if op == '-':
        return n1-n2
    if op == '/':
        return n1//n2
    if op == '*':
        return n1*n2


def dar_var(n):
    if '$' in n:
        n = n.replace('$', '')
        return int(lista[n])
    return int(n)


def get_inputs() -> list:
    inputs = list()

    for line in sys.stdin:
        line = line.replace('\n', '').replace('\r', '')
        if line == '#' or line == '' or line == "0" or line == 'end':
            break

        inputs.append(str(line))

    return inputs


if __name__ == "__main__":
    solution(get_inputs())
