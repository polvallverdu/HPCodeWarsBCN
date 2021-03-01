entarda = input()
diferencia_total = 0
diferencia = 0
while entarda != '-1':
    robados, cogidos = entarda.split()
    robados = int(robados)
    cogidos = int(cogidos)
    diferencia = robados - cogidos
    if robados > cogidos:

        print('The Niffler is escaping. +{0}'.format(diferencia))
    elif robados < cogidos:

        print('Newt is getting closer to the Niffler. {0}'.format(diferencia))
    else:
        print('Newt is keeping the distance with the Niffler')
    entarda = input()

    diferencia_total += diferencia

if diferencia_total == 0:

    print('Newt catches the Niffler')
else:
    print('The Niffler has escaped')
