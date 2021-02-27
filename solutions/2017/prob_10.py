coste = round(float(input()), 2)
billete = round(float(input()), 2)

cambio_dar = billete-coste
cambio = round(float(input()), 2)
cambio_dado = cambio

while cambio != 0:
    cambio = round(float(input()), 2)
    cambio_dado += cambio

if(cambio_dado == cambio_dar):
    print('Right')
else:
    print('Wrong')
