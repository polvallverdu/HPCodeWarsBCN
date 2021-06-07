import sys


def get_num(num: float):
  if num % 1 == 0:
    return int(num)
  else:
    return num


def solution(inputs: list):
    w1 = 1.9116881315655996
    w2 = 1.22872621999026
    b = -7.119940111025795
    e = 2.718281828459045

    for flower in inputs:
        a = flower[0]*w1 + flower[1]*w2 + b
        c = 1/(1+e**(a*-1))
        if c < 0.5:
            # Blue
            print(f"The flower ({get_num(flower[0])} {get_num(flower[1])}) is blue")
        else:
            # Red
            print(f"The flower ({get_num(flower[0])} {get_num(flower[1])}) is red")



def get_inputs() -> list:
    inputs = list()
    count = 0
    inputcount = 0
    is_count = False

    for line in sys.stdin:
        line = line.replace('\n', '').replace('\r', '')

        if not is_count:
            inputcount = int(line)
            is_count = True
        else:
            rawflower = line.split(' ')
            flower = [float(rawflower[0]), float(rawflower[1])]
            inputs.append(flower)
            if count == inputcount-1:
                break
            count += 1

    return inputs

solution(get_inputs())
