import math


'''
IMPORTANT: importar la llibreria math amb -> import math

truncate(float, int) -> Talla el nombre de decimals
is_prime(int) -> Torna un bool de si un nombre es primer
fibonacci(int, int) -> Torna una llista de nombres fibonacci (mirar problema 8 del 2016)
ludic(int) -> Torna una llista de nombres ludic (mirar problema 16 del 2017)
reverse_num(int) -> Invertir un numero
polindrome(str o int) -> Detectar si un int o str es igual que la seva versió invertida
ternary(int) -> Ni idea (mirar problema 20 del 2019)
roman_to_int(str) -> Torna un int dels numeros romans
int_to_roman(int) -> Torna un string del numero en nombres romans

template.py -> Arxiu que podeu copiar i utilitzar per agafar diferents linees d'input.
'''


def truncate(number: float, digits: int) -> float:
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper


def is_prime(num: int) -> bool:
    if num <= 1:
        return False

    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True


def fibonacci(n1: int, n2: int) -> list:
    '''
    n1 = Vegades que sumarà els nombres
    n2 = Les vegades que farà el bucle
    '''
    fib = list()

    for i in range(n1):
        i = 0
        fib.append(1)

    for x in range(n1, n2):
        fib.append(0)
        for i in range(n1+1):
            fib[x] += fib[x-i]

    return fib


def ludic(n: int) -> list:
    ludics = []

    for i in range(1, n + 1):
        ludics.append(i)

    index = 1

    while(index != len(ludics)):
        first_ludic = ludics[index]
        remove_index = index + first_ludic

        while(remove_index < len(ludics)):
            ludics.remove(ludics[remove_index])
            remove_index = remove_index + first_ludic - 1

        index += 1
    return ludics


def reverse_num(num: int) -> int:
    reverse = 0
    while num > 0:
        reminder = num % 10
        reverse = (reverse*10) + reminder
        num = num//10
    return reverse


def polindrome(line) -> bool:
    return str(line) == str(line)[::-1]


def ternary(n: int) -> str:
    if n == 0:
        return '0'

    nums = []

    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))

    return ''.join(reversed(nums))


def roman_to_int(roman_num: str) -> int:
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,
             'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
    i = 0
    num = 0
    while i < len(roman_num):
        if i+1 < len(roman_num) and roman_num[i:i+2] in roman:
            num += roman[roman_num[i:i+2]]
            i += 2
        else:
            num += roman[roman_num[i]]
            i += 1
    return num


def int_to_roman(num: int) -> str:
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syb[i]
            num -= val[i]
        i += 1
    return roman_num


if __name__ == "__main__":
    print('''
IMPORTANT: importar la llibreria math amb -> import math

truncate(float, int) -> Talla el nombre de decimals
is_prime(int) -> Torna un bool de si un nombre es primer
fibonacci(int, int) -> Torna una llista de nombres fibonacci (mirar problema x del 201x)
ludic(int) -> Torna una llista de nombres ludic (mirar problema x del 201x)
reverse_num(int) -> Invertir un numero
polindrome(str o int) -> Detectar si un int o str es igual que la seva versió invertida
ternary(int) -> Ni idea (mirar problema x del 201x)
roman_to_int(str) -> Torna un int dels numeros romans
int_to_roman(int) -> Torna un string del numero en nombres romans

template.py -> Arxiu que podeu copiar i utilitzar per agafar diferents linees d'input.
''')
