texto = input()
numeros = '0123456789'
numeros_guardados = ''
for x in texto:
    for y in numeros:
        if (x == y):
            numeros_guardados = numeros_guardados + x

texto = texto.replace('0', '')
texto = texto.replace('1', '')
texto = texto.replace('2', '')
texto = texto.replace('3', '')
texto = texto.replace('4', '')
texto = texto.replace('5', '')
texto = texto.replace('6', '')
texto = texto.replace('7', '')
texto = texto.replace('8', '')
texto = texto.replace('9', '')

print(texto)
print(numeros_guardados)
