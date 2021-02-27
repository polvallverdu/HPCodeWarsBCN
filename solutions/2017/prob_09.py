entarada1 = input()
entarda2 = input()

anchones, alturanes = entarada1.split()
ancho, altura = entarda2.split()

if int(ancho) < int(anchones) and int(altura) < int(alturanes):
    print('Yes')
else:
    print('No')
