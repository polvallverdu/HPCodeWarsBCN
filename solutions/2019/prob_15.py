entrada = input()


def fibonacci(n):
    fib = [0, 1, 1]

    if n > 0 and n <= 2:
        return fib[1]

    elif n == 0:
        return fib[0]

    else:
        for x in range(3, n+1):
            fib.append(0)
            fib[x] = fib[x-1] + fib[x-2]
        return fib[n]


numeros = entrada.split(' ')
numeros = list(map(int, numeros))

print(str(fibonacci(numeros[0])) + " " + str(fibonacci(numeros[1])) + " "
      + str(fibonacci(numeros[2])) + " " + str(fibonacci(numeros[3])))
