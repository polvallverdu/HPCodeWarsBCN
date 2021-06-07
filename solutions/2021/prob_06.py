import sys


def solution(inputs: list):
    points = 0
    for line in inputs:
        for char in line:
            if char == "o":
                points += 1
            elif char == "T":
                points += 2
            elif char == "+":
                points += 1.5
    print(points)


def get_inputs() -> list:
    inputs = list()

    for line in sys.stdin:
        line = line.replace('\n', '').replace('\r', '').lstrip().rstrip()
        if line == '#' or line == '' or line == "0":
            break

        inputs.append(str(line))

    return inputs


solution(get_inputs())
