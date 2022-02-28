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
  def transform_roman_to_int(roman: str) -> int:
    num = [1, 4, 5, 9, 10, 40, 50, 90,
        100, 400, 500, 900, 1000]
    sym = ["I", "IV", "V", "IX", "X", "XL",
        "L", "XC", "C", "CD", "D", "CM", "M"]
    i = 12
    r = ""
      
    while roman:
        div = roman // num[i]
        roman %= num[i]
  
        while div:
            r += sym[i]
            div -= 1
        i -= 1
    return r
  
  @staticmethod
  def transform_int_to_roman(num: int) -> str:
    m = ["", "M", "MM", "MMM"]
    c = ["", "C", "CC", "CCC", "CD", "D",
         "DC", "DCC", "DCCC", "CM "]
    x = ["", "X", "XX", "XXX", "XL", "L",
         "LX", "LXX", "LXXX", "XC"]
    i = ["", "I", "II", "III", "IV", "V",
         "VI", "VII", "VIII", "IX"]
  
    thousands = m[num // 1000]
    hundreds = c[(num % 1000) // 100]
    tens = x[(num % 100) // 10]
    ones = i[num % 10]
  
    ans = (thousands + hundreds +
           tens + ones)
  
    return ans
  
  @staticmethod
  def generate_fibonacci(num: int) -> int:
    arr=[0,1]
    if num==1:
        return 0
    elif num==2:
        return 1
    else:
        while(len(arr)<num):
            arr.append(0)
        if(num==0 or num==1):
            return 1
        else:
            arr[0]=0
            arr[1]=1
            for i in range(2,num):   
                arr[i]=arr[i-1]+arr[i-2]
            return arr[num-1]
