entrada = input()

# TODO: @DolphinGamerYT Acabar-lo


class solution:

    def __init__(self, n1):
        self.primero = True
        self.primero2 = True
        self.pos1 = n1*2-1
        self.pos2 = n1*2

    def triangulo_piramide(self, n1: int):
        for x in range(n1):
            print((self.espacios_arriba(n1) + '/'+'\\')*(x+1))
            print((self.espacios_abajo(n1)+'/'+'__'+'\\') * (x+1))

    def espacios_arriba(self, n1):
        if self.primero == True:
            self.primero = False
            return ' '*self.pos1
        else:
            return ' '*2

    def espacios_abajo(self, n1):
        if self.primero2 == True:
            self.primero2 = False
            return ' '*(self.pos1-1)
        else:
            return ''
        self.pos1 -= 2


entrada = entrada.replace(' ', '')
for x in entrada:
    x = int(x)
    solution(x).triangulo_piramide(x)
