
entrada = input()

tabla = {'Ship': [0.3, 23.3], 'Train': [0.32, 23.1],
         'Road': [2.12, 160.1], 'Plane': [21.01, 1577.1]}

hacer_print = []

while entrada != '#':
    medio, energia = entrada.split()
    totalkm = int(energia)/tabla[medio][0]
    totalco2 = totalkm*tabla[medio][1]
    hacer_print.append('{0} {1} {2}'.format(
        medio, round(totalkm, 1), round(totalco2, 1)))
    entrada = input()

for x in hacer_print:
    print(x)
