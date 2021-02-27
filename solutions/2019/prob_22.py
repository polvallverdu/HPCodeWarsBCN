import string

opcion = input()
texto = input()
palabra_clave = input()

texto = texto.upper()
palabra_clave = palabra_clave.upper()

longitud_msg = len(texto)
longitud_clave = len(palabra_clave)

alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
            'Y', 'Z']
longitud_alfabeto = len(alfabeto)

vigenere_tabla = []
for i in range(longitud_alfabeto):
    vigenere = vigenere + [alfabeto]
    alfabeto = alfabeto[1:] + list(alfabeto[0])

if opcion == 'C':
    for i in range(longitud_msg):
        j = palabra_clave[i % longitud_clave]
        print(vigenere[string.ascii_uppercase.index(j)][string.ascii_uppercase.index(texto[i])],
              end="")
if (opcion == "D"):
    for i in range(longitud_msg):
        j = palabra_clave[i % longitud_clave]
        pos = vigenere[string.ascii_uppercase.index(j)].index(texto[i])
        print(alfabeto[pos], end="")
