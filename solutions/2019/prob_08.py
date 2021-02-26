text = str(input())
sustituir = str(input())
alumnos = int(input())

for x in range(alumnos):
    nombre = str(input())
    print(text.replace(sustituir, nombre))
