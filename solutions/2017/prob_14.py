numero_planetas = int(input())
gravedad_alta = 0
index = 0
for x in range(numero_planetas):
    # separo las variables
    caracteristcas = input()
    altura, tiempo = caracteristcas.split()
    # calcula la gravedad
    gravedad = (2.0*float(altura))/(float(tiempo)**2)
    # cojo la gravedad más alta
    if(gravedad > gravedad_alta):
        gravedad_alta = gravedad
        index = x

print('Planet number {0} has the most gravity.'.format(index+1))
