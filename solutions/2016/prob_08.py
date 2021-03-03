entrada = input()


def fibonacci(n1, n2):
    fib = list()
    for i in range(n1):
        i = 0
        fib.append(1)
    for x in range(n1, n2):
        fib.append(0)
        for i in range(n1+1):
            fib[x] += fib[x-i]
    return fib


numeros = entrada.split(' ')
numeros = list(map(int, numeros))

for x in fibonacci(numeros[0], numeros[1]):
    print(x, end=' ')
