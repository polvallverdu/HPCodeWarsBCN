entrada = input()

numero_a_comprobar = int(float(entrada))
total_caracteres = len(str(numero_a_comprobar))
pasado = set()


while total_caracteres != 1:
    for i in str(numero_a_comprobar):
        numero = 0
        numero += int(i)**2
    numero_a_comprobar = numero
    total_caracteres = len(str(numero_a_comprobar))
    if numero_a_comprobar in pasado:
        break
    pasado.add(numero_a_comprobar)


if (numero_a_comprobar == 1):
    print('{0} is a happy number!'.format(int(float(entrada))))
else:
    print('{0} is an unhappy number!'.format(int(float(entrada))))
