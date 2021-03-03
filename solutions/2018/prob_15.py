texto = str(input())
texto_nopermitido = str(input())

texto = texto.replace(texto_nopermitido, '', len(texto_nopermitido))

print(texto)
