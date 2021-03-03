control = 0
lista_media = []
suma_notas = 0

while control != 1:
    try:
        nota = float(input())
    except:
        control = 1
    lista_media.append(nota)
    suma_notas += nota


media = suma_notas/len(lista_media)

alumnos_malos = 0
for x in lista_media:
    if (x < media):
        alumnos_malos += 1

print(alumnos_malos)
