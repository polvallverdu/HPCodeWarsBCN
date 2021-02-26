frase = input()
frase_modificada = frase.replace('r ', 'rr ')

frase_modificada = frase_modificada.replace('R ', 'RR ')

if frase_modificada[-1] == 'r' or frase_modificada[-1] == 'R':
    frase_modificada = frase_modificada + frase_modificada[-1]

print(frase_modificada)
