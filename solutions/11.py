entarda = input()

numero, mes = entarda.split()

division = int(numero)/int(mes)

decimales = (division-int(division))

primer_decimal = int(decimales*10)

segundo_decimal = int(((decimales*10) - primer_decimal)*10)

if primer_decimal != 0 and segundo_decimal == 0:
    print('1')
else:
    print('0')
