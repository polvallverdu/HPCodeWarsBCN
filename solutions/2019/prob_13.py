texto = str(input())

texto.lower()
lista_letras = 'abcdefghijklmnopqrstuvwxyz'
lista_letras = lista_letras[::-1]

for x in lista_letras:
    count = 0
    for y in texto:
        if x == y:
            count += 1
    print(x, '=', count)
