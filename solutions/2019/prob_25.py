import sys
operators = ['+', '-', '*', '/', '%', '=']


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


def format_list(inputs: list) -> list:
    formatted_list = list()
    for e in inputs:
        if e not in operators:
            formatted_list.append(roman_to_int(e))
        else:
            formatted_list.append(e)
    return formatted_list


def solution(inputs: list):
    formatted_list = format_list(inputs)
    num = 0

    for x in range(0, len(formatted_list), 2):
        operator = ""
        if x != 0:
            operator = formatted_list[x-1]

        if operator == "-":
            num -= formatted_list[x]
        elif operator == "*":
            num *= formatted_list[x]
        elif operator == "/":
            num //= formatted_list[x]
        elif operator == "%":
            num %= formatted_list[x]
        else:
            num += formatted_list[x]
    print(int_to_roman(num))


def get_inputs() -> list:
    inputs = list()

    for line in sys.stdin:
        line = line.replace('\n', '').replace('\r', '').upper()
        if line == '=':
            break

        inputs.append(str(line))

    return inputs


solution(get_inputs())
