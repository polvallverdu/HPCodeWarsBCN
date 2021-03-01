resultados = str(input())
apuesta = str(input())

aciertos = 0
mirar = 0

hola = apuesta[3]

for x in resultados:

    if x == apuesta[mirar]:
        aciertos += 1
    mirar += 1

print(aciertos)
