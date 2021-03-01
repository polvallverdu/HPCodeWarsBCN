
entrada = input()
lista_todo = []

while entrada != '#':
    entrada = entrada.replace(';', '').replace(',', ' ')
    if entrada[:2] == 'CO':
        hola = 'hola'
    elif entrada[:2] == 'PD':
        entrada = entrada[2:]
        if entrada == '':
            lista_todo.append('PD;')
        else:
            lista = entrada.split()
            lista_todo.append('PD;')
            for x in range(len(lista)//2):
                coordx = lista[0]
                coordy = lista[1]
                lista.remove(coordx)
                lista.remove(coordy)
                printear = 'MA' + ' ' + coordx + ',' + coordy + ';'
                lista_todo.append(printear)
    elif entrada[:2] == 'PU':
        entrada = entrada[2:]
        if entrada == '':
            lista_todo.append('PU;')
        else:
            lista = entrada.split()
            lista_todo.append('PU;')
            for x in range(len(lista)//2):
                coordx = lista[0]
                coordy = lista[1]
                lista.remove(coordx)
                lista.remove(coordy)
                printear = 'MA' + ' ' + coordx + ',' + coordy + ';'
                lista_todo.append(printear)
    elif entrada[:2] == 'PA':
        entrada = entrada[2:]
        if entrada == '':
            hola = 'hola'
        else:
            lista = entrada.split()
            for x in range(len(lista)//2):
                coordx = lista[0]
                coordy = lista[1]
                lista.remove(coordx)
                lista.remove(coordy)
                printear = 'MA' + ' ' + coordx + ',' + coordy + ';'
                lista_todo.append(printear)
    entrada = input()

for x in lista_todo:
    print(x)
print('#')
