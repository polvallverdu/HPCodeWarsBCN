from __future__ import annotations
import math
import sys


class Square:

    def __init__(self, x, y, value=None) -> None:
        self.x = x
        self.y = y
        self.value = value


class Matrix:
    
    def __init__(self, rows: int = 0, columns: int = -1):
        self.__rows = rows
        self.__columns = columns if columns != -1 else rows
        self.__matrix = []
        self.__generate()

    def __generate(self) -> None:
      for y in range(self.__rows):
        self.__matrix.append([Square(x, y) for x in range(self.__columns)])

    def __str__(self) -> str:
        return "\n".join([" ".join([str(square.value) for square in row]) for row in self.__matrix])
    
    @property
    def rows(self) -> int:
        return self.__rows

    @property
    def columns(self) -> int:
        return self.__columns

    def setRows(self, rows: int) -> None:
        self.__updateMatrix(rows, self.__columns)
    
    def setColumns(self, columns: int) -> None:
        self.__updateMatrix(self.__rows, columns)
    
    def setSquare(self, x: int, y: int, value) -> None:
        self.__updateMatrix(max(y, self.__rows), max(x, self.__columns))
        
        self.__matrix[y][x].value = value

    def __updateMatrix(self, rows: int, columns: int) -> None:
        if self.__columns != columns:
            if columns > self.__columns:
                for y, row in enumerate(self.__matrix):
                    row.extend([Square(x, y) for x in range(self.__columns, columns)])
            else:
                for row in self.__matrix:
                    for x in range(columns, self.__columns):
                        del row[x]
            self.__columns = columns
        
        if self.__rows != rows:
            if rows > self.__rows:
                for x in range(self.__rows, rows):
                    self.__matrix.append([Square(x, y) for y in range(self.__columns)])
            else:
                for x in range(rows, self.__rows):
                    del self.__matrix[x]

    def getSquare(self, x: int, y: int, newSquareIfMissing: bool=False) -> Square or None:
        try:
            return self.__matrix[x][y]
        except:
            return None if not newSquareIfMissing else Square(x, y)

    def getWindow(self, x: int, y: int, radius: int, onlyHorizontalAndVertical: bool = False) -> list[Square]:
        result = []

        for x in range(x - radius, x + radius + 1):
            for y in range(y - radius, y + radius + 1):
                if x >= 0 and y >= 0 and x < self.__rows and y < self.__columns:
                    if onlyHorizontalAndVertical and (x != x or y != y):
                        continue
                    result.append(self.__matrix[x][y])

        return result

    @property
    def squares(self) -> list[Square]:
        for row in self.__matrix:
            for c in row:
                yield c
    
    def getSquaresInZone(self, x1: int, y1: int, x2: int, y2: int) -> list[Square]:
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                yield self.getSquare(x, y)
    
    def getMatrixOfZone(self, x1: int, y1: int, x2: int, y2: int) -> Matrix:
        m = Matrix(x2 - x1 + 1, y2 - y1 + 1)
        for y in range(y1, y2 + 1):
            for x in range(x1, x2 + 1):
                m.setSquare(x - x1, y - y1, self.getSquare(x, y))


class CodeWarsHelper:

    def __init__(self) -> None:
        # Hi Judges :wave:, welcome to my lib :D
        # Esto no es codigo robado :wink:
        self.__author__ = "Pol Vallverdu"

    @staticmethod
    def input_string() -> str:
        return input().replace('\n', '').replace('\r', '').lstrip().rstrip()

    @staticmethod
    def input_string_list(end="") -> list:
        inputs = list()

        for line in sys.stdin:
            line = line.replace('\n', '').replace('\r', '').lstrip().rstrip()
            if line == end:
                break

            inputs.append(str(line))

        return inputs

    @staticmethod
    def input_int() -> int:
        return int(input())

    @staticmethod
    def input_int_list(end="") -> list:
        inputs = []

        for l in CodeWarsHelper.input_string_list(end):
            inputs.append(int(l))

        return inputs

    @staticmethod
    def input_float() -> float:
        return float(input())

    @staticmethod
    def input_float_list(end="") -> list:
        inputs = []

        for l in CodeWarsHelper.input_string_list(end):
            inputs.append(float(l))

        return inputs

    @staticmethod
    def truncate(number: float, digits: int) -> float:
        stepper = 10.0 ** digits
        return math.trunc(stepper * number) / stepper

    @staticmethod
    def is_prime(num: int) -> bool:
        if num <= 1:
            return False

        for i in range(2, num):
            if (num % i) == 0:
                return False
        return True

    @staticmethod
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

    @staticmethod
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

    @staticmethod
    def reverse_num(num: int) -> int:
        reverse = 0
        while num > 0:
            reminder = num % 10
            reverse = (reverse*10) + reminder
            num = num//10
        return reverse

    @staticmethod
    def polindrome(line) -> bool:
        return str(line) == str(line)[::-1]

    @staticmethod
    def ternary(n: int) -> str:
        if n == 0:
            return '0'

        nums = []

        while n:
            n, r = divmod(n, 3)
            nums.append(str(r))

        return ''.join(reversed(nums))

    @staticmethod
    def transform_roman_to_int(roman_num: str) -> int:
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

    @staticmethod
    def transform_int_to_roman(num: int) -> str:
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

    @staticmethod
    def get_list_duplicates(l: list) -> list:
        duplicates = []
        for i in l:
            if l.count(i) > 1 and i not in duplicates:
                duplicates.append(i)
        return duplicates

    @staticmethod
    def get_list_duplicates_with_amount(l: list) -> list:
        duplicates = []
        for i in l:
            if l.count(i) > 1 and i not in duplicates:
                duplicates.append({"count": l.count(i), "value": i})

        return duplicates

    @staticmethod
    def get_list_alphabetic_order(l: list, reverse: bool = False) -> list:
        l = sorted(l)
        return l if not reverse else l.reverse()

    @staticmethod
    def chunk_list(l: list, element_num: int) -> list:
        return [l[i:i+element_num] for i in range(0, len(l), element_num)]
