entrada = input()


def triangulo_piramide():
    print(' ' + '/'+'\\')
    print('/'+'__'+'\\')


entrada = entrada.replace(' ', '')
for x in entrada:
    x = int(x)
    for i in range(x):
        print(f'{triangulo_piramide()}'*(x))


print(triangulo_piramide())
