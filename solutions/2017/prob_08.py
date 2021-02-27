nombre_mal = str(input())
nombre = ''
for x in nombre_mal:
    if x.islower():
        nombre = nombre + x.upper()
    elif x.isupper():
        nombre = nombre + x.lower()
    else:
        nombre = nombre + x

print(nombre)
