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
  
  @staticmethod
  def list_insert(l: list, l_with_elements: list) -> list:
    for e in l_with_elements:
      l.append(e)
    return l


class Square:
  
  def __init__(self, x, y, value) -> None:
      self.x = x
      self.y = y
      self.value = value
      self.v = value
      self.checked = False

rawxy = CodeWarsHelper.input_string().split(" ")
xS = int(rawxy[0])
yS = int(rawxy[1])

squares = []

i = CodeWarsHelper.input_string_list()
for y in range(yS):
  for x in range(xS):
    squares.append(Square(x, y, i[y][x]))

def getSquare(x, y):
  try:
    return squares[y * xS + x]
  except:
    return None

def getWindow(x: int, y: int) -> list: # Stolen code from another problem 2021/29
  return [s for s in [getSquare(x, y), getSquare(x, y + 1), getSquare(x, y - 1), getSquare(x + 1, y), getSquare(x - 1, y)] if s is not None]


def recursive_check(x, y):
  to_check = [s for s in getWindow(x, y) if not s.checked and s.v == '#']
  if len(to_check) == 0:
    return
  
  for s in to_check:
    s.checked = True
    recursive_check(s.x, s.y)

b = 0
for s in list([s for s in squares if s.value == "#"]):
  if s.checked:
    continue
  
  b += 1
  s.checked = True
  recursive_check(s.x, s.y)

print(b)
