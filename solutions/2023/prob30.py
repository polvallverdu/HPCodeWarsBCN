import math
import sys

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
    def input_string_spaces(separator=" ") -> list:
        return CodeWarsHelper.input_string().split(separator)

    @staticmethod
    def input_string_spaces_tuple(separator=" ") -> tuple:
        return tuple(CodeWarsHelper.input_string().split(separator))

    @staticmethod
    def input_string_spaces_list(end="", separator=" ") -> list:
        r = []
        for l in CodeWarsHelper.input_string_list(end):
            r.extend(l.split(separator))
        return r

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
    def input_int_spaces(separator=" ") -> list:
        return [int(n) for n in CodeWarsHelper.input_string().split(separator)]

    @staticmethod
    def input_int_spaces_tuple(separator=" ") -> tuple:
        return tuple(int(n) for n in CodeWarsHelper.input_string().split(separator))

    @staticmethod
    def input_int_spaces_list(end="", separator=" ") -> list:
        r = []
        for l in CodeWarsHelper.input_string_list(end):
            r.extend([int(i) for i in l.split(separator)])
        return r

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
    def input_float_spaces(separator=" ") -> list:
        return [float(n) for n in CodeWarsHelper.input_string().split(separator)]
    
    @staticmethod
    def input_float_spaces_tuple(separator=" ") -> tuple:
        return tuple(float(n) for n in CodeWarsHelper.input_string().split(separator))

    @staticmethod
    def input_float_spaces_list(end="", separator=" ") -> list:
        r = []
        for l in CodeWarsHelper.input_string_list(end):
            r.extend([float(i) for i in l.split(separator)])
        return r

    @staticmethod
    def truncate(number: float, digits: int) -> float:
        stepper = 10.0 ** digits
        return math.trunc(stepper * number) / stepper

    # pol be like:
    # ⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠛⠛⠋⠉⠈⠉⠉⠉⠉⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿
    # ⣿⣿⣿⣿⣿⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⢿⣿⣿⣿⣿
    # ⣿⣿⣿⣿⡏⣀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿
    # ⣿⣿⣿⢏⣴⣿⣷⠀⠀⠀⠀⠀⢾⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿
    # ⣿⣿⣟⣾⣿⡟⠁⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣷⢢⠀⠀⠀⠀⠀⠀⠀⢸⣿
    # ⣿⣿⣿⣿⣟⠀⡴⠄⠀⠀⠀⠀⠀⠀⠙⠻⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⣿
    # ⣿⣿⣿⠟⠻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠶⢴⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⣿
    # ⣿⣁⡀⠀⠀⢰⢠⣦⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⡄⠀⣴⣶⣿⡄⣿
    # ⣿⡋⠀⠀⠀⠎⢸⣿⡆⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⠗⢘⣿⣟⠛⠿⣼
    # ⣿⣿⠋⢀⡌⢰⣿⡿⢿⡀⠀⠀⠀⠀⠀⠙⠿⣿⣿⣿⣿⣿⡇⠀⢸⣿⣿⣧⢀⣼
    # ⣿⣿⣷⢻⠄⠘⠛⠋⠛⠃⠀⠀⠀⠀⠀⢿⣧⠈⠉⠙⠛⠋⠀⠀⠀⣿⣿⣿⣿⣿
    # ⣿⣿⣧⠀⠈⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠟⠀⠀⠀⠀⢀⢃⠀⠀⢸⣿⣿⣿⣿
    # ⣿⣿⡿⠀⠴⢗⣠⣤⣴⡶⠶⠖⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡸⠀⣿⣿⣿⣿
    # ⣿⣿⣿⡀⢠⣾⣿⠏⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠉⠀⣿⣿⣿⣿
    # ⣿⣿⣿⣧⠈⢹⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿
    # ⣿⣿⣿⣿⡄⠈⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣾⣿⣿⣿⣿⣿
    # ⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿
    # ⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    # ⣿⣿⣿⣿⣿⣦⣄⣀⣀⣀⣀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    # ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    # ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠙⣿⣿⡟⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿
    # ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠁⠀⠀⠹⣿⠃⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿
    # ⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⢐⣿⣿⣿⣿⣿⣿⣿⣿⣿
    # ⣿⣿⣿⣿⠿⠛⠉⠉⠁⠀⢻⣿⡇⠀⠀⠀⠀⠀⠀⢀⠈⣿⣿⡿⠉⠛⠛⠛⠉⠉
    # ⣿⡿⠋⠁⠀⠀⢀⣀⣠⡴⣸⣿⣇⡄⠀⠀⠀⠀⢀⡿⠄⠙⠛⠀⣀⣠⣤⣤⠄

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

        while (index != len(ludics)):
            first_ludic = ludics[index]
            remove_index = index + first_ludic

            while (remove_index < len(ludics)):
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
        if reverse:
            l.reverse()
        return l

    @staticmethod
    def chunk_list(l: list, element_num: int) -> list:
        return [l[i:i+element_num] for i in range(0, len(l), element_num)]

    @staticmethod
    def mcd(*numbers):
        if len(numbers) == 0:
            return None
        elif len(numbers) == 1:
            return numbers[0]
        else:
            # apply Euclidean algorithm iteratively
            a = numbers[0]
            for b in numbers[1:]:
                while b:
                    a, b = b, a % b
            return a

    @staticmethod
    def mcm(*numbers):
        if len(numbers) == 0:
            return None
        elif len(numbers) == 1:
            return numbers[0]
        else:
            # apply LCM formula iteratively
            result = numbers[0]
            for num in numbers[1:]:
                result = (result * num) // CodeWarsHelper.gcd(result, num)
            return result

    @staticmethod
    def decimal_to_binary(decimal_num: int) -> str:
        binary_num = ""
        if decimal_num == 0:
            return "0"
        while decimal_num > 0:
            binary_num = str(decimal_num % 2) + binary_num
            decimal_num //= 2
        return binary_num
    
    @staticmethod
    def binary_to_decimal(binary_num: str) -> int:
        decimal_num = 0
        for i in range(len(binary_num)):
            digit = int(binary_num[i])
            decimal_num += digit * 2**(len(binary_num) - i - 1)
        return decimal_num

    #def transpose_matrix(rows: list[list[any]]) -> list[list[any]]:
    # @staticmethod
    # def transpose_matrix(rows: list) -> list:
    #     num_rows = len(rows)
    #     num_cols = len(rows[0])
    #     columns = [[] for _ in range(num_cols)]
    #     for i in range(num_rows):
    #         for j in range(num_cols):
    #             columns[j].append(rows[i][j])
    #     return columns
    
    # def transpose_matrix(matrix: list[list[any]]) -> list[list[any]]:
    @staticmethod
    def transpose_matrix(matrix: list) -> list:
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        transposed = []
        for j in range(num_cols):
            transposed_row = []
            for i in range(num_rows):
                if j < len(matrix[i]):
                    transposed_row.append(matrix[i][j])
                else:
                    transposed_row.append(None)
            transposed.append(transposed_row)
        return transposed

facil = {}
players = {}
teams = {}
brands = {}

for player in CodeWarsHelper.input_string_list(end="#"):
  name, team, brand = player.split(" ")
  default = {
    "wins": 0,
    "points": 0
  }
  players[name] = default.copy()
  teams[team] = default.copy()
  brands[brand] = default.copy()
  facil[name] = {"team": team,
    "brand": brand,}

matches = []
for match in CodeWarsHelper.input_string_list(end="#"):
  winners, fastest = match.split("|")
  missing = list(players.keys()).copy()
  for p in winners.split("_"):
    missing.remove(p)
  
  matches.append([winners.split("_"), missing, fastest])

points = [10, 8, 6, 4, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for match in matches:
  for i, winner in enumerate(match[0]):
    # p = 0 if i > len(points) else points[i]
    p = points[i]
    players[winner]["points"] += p
    nameindex = list(players.keys()).index(winner)
    teams[facil[winner]["team"]]["points"] += p
    brands[facil[winner]["brand"]]["points"] += p
    if p == 10:
      players[winner]["wins"] += 1
      teams[facil[winner]["team"]]["wins"] += 1
      brands[facil[winner]["brand"]]["wins"] += 1
  
  if match[2] not in match[1]:
    players[match[2]]["points"] += 1
    teams[facil[match[2]]["team"]]["points"] += 1
    brands[facil[match[2]]["brand"]]["points"] += 1

print("Riders Classification:")
ss = sorted(players, key=lambda x: players[x]["points"], reverse=True)
max_points = max([x["points"] for x in players.values()])
max_players = [x for x in players.items() if x[1]["points"] == max_points]
sss = sorted(max_players, key=lambda x: x[1]["wins"], reverse=True)
for i in range(3):
  if len(sss) > i:
    print("{} - {} - {} pts - {} wins".format(i+1, sss[i][0], players[sss[i][0]]["points"], players[sss[i][0]]["wins"]))
  else:
    print("{} - {} - {} pts - {} wins".format(i+1, ss[i], players[ss[i]]["points"], players[ss[i]]["wins"]))

print("Teams Classification:")
ss = sorted(teams, key=lambda x: teams[x]["points"], reverse=True)
max_points = max([x["points"] for x in teams.values()])
max_players = [x for x in teams.items() if x[1]["points"] == max_points]
sss = sorted(max_players, key=lambda x: x[1]["wins"], reverse=True)
for i in range(3):
  if len(sss) > i:
    print("{} - {} - {} pts - {} wins".format(i+1, sss[i][0], teams[sss[i][0]]["points"], teams[sss[i][0]]["wins"]))
  else:
    print("{} - {} - {} pts - {} wins".format(i+1, ss[i], teams[ss[i]]["points"], teams[ss[i]]["wins"]))
    
print("Brands Classification:")
ss = sorted(brands, key=lambda x: brands[x]["points"], reverse=True)
max_points = max([x["points"] for x in brands.values()])
max_players = [x for x in brands.items() if x[1]["points"] == max_points]
sss = sorted(max_players, key=lambda x: x[1]["wins"], reverse=True)
for i in range(3):
  if len(sss) > i:
    print("{} - {} - {} pts - {} wins".format(i+1, sss[i][0], brands[sss[i][0]]["points"], brands[sss[i][0]]["wins"]))
  else:
    print("{} - {} - {} pts - {} wins".format(i+1, ss[i], brands[ss[i]]["points"], brands[ss[i]]["wins"]))
    