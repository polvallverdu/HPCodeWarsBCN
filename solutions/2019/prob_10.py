frase = input()
palabras_prohibidas = ['noob', 'no0b', 'n00b', 'n0ob']

frase = frase.replace('.', '')
frase = frase.replace(',', '')
frase = frase.replace('?', '')
frase = frase.replace('!', '')

palabras = frase.lower().split()

if any(palabra in palabras_prohibidas for palabra in palabras):
    print('User is banned.')
else:
    print('User is exhibiting a friendly behaviour.')
