import datetime

entrada = input()

while entrada != '#':
    nombre, salida, final = entrada.split()
    salida = float(salida)
    final = float(final)
    salidaseg = datetime.datetime.fromtimestamp(salida).isoformat()
    finalseg = datetime.datetime.fromtimestamp(final).isoformat()
    tiempo = int(salidaseg)-(finalseg)
    print(nombre + tiempo)
