import sys


def get_list(inputs) -> tuple:
    first = list()
    second = list()
    for a in inputs:
        b = a.split(' ')
        first.append(float(b[0]))
        second.append(float(b[1]))

    return first, second


def solution(random_num: str, inputs: list):
    dasnmljk = random_num.split('+')
    max_time = int(dasnmljk[0])
    delay = int(dasnmljk[1])
    rawfirst, rawsecond = get_list(inputs)

    first = 0
    second = 0
    for num in rawfirst:
        if num != 0.0:
            first += num+delay
    
    for num in rawsecond:
        if num != 0.0:
            second += num+delay
    
    print(str(max_time-first) + " " + str(max_time-second))


def get_inputs() -> tuple:
    random_num = ""
    isdsa = False
    inputs = list()

    for line in sys.stdin:
        line = line.replace('\n', '').replace('\r', '').lstrip().rstrip()
        if line == '#':
            break
        if not isdsa:
            random_num = line
            isdsa = True
        else:
            inputs.append(str(line))

    return random_num, inputs

random_num, inputs = get_inputs()
solution(random_num, inputs)
