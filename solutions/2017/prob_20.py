entrada = input()
coste_avion, coste_coche, coste_habitacion, coste_comida, min_amigos, maximo_amigos = entrada.split()

amigos = []
costes_personas = []

valor_pequeño = 0
numero_amigos = 0


for x in range(int(min_amigos), int(maximo_amigos)+1):

    numero_coches = 0
    if x % 5 == 0:
        numero_coches = x//5
    else:
        numero_coches = x//5 + 1

    numero_habitaciones = 0
    if x % 3 == 0:
        numero_habitaciones = x//3
    else:
        numero_habitaciones = x//3 + 1

    coste_persona_coche = int(coste_coche)*numero_coches//x
    coste_persona_habitacion = int(coste_habitacion)*numero_habitaciones//x
    coste_persona_total = coste_persona_coche + \
        coste_persona_habitacion+int(coste_comida)

    costes_personas.append(coste_persona_total)
    amigos.append(x)

    print(f'{x} friends. Cost per person by plane: {int(coste_avion)}. Cost per person by car: {coste_persona_total}')


valor_pequeño = costes_personas[0]
numero_amigos = amigos[0]
medio_transporte = ''
for x in range(len(costes_personas)):
    if costes_personas[x] < valor_pequeño:
        valor_pequeño = costes_personas[x]
        numero_amigos = amigos[x]
        medio_transporte = 'car'

if valor_pequeño > int(coste_avion):
    numero_amigos = amigos[len(amigos)-1]
    valor_pequeño = int(coste_avion)
    medio_transporte = 'plane'


print(
    f'The optimal number of friends are: {numero_amigos}, and the total cost going by {medio_transporte} is {valor_pequeño*numero_amigos}')
