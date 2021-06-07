import sys


def get_clean_num(line):
    splitted = line.split(' ')
    a = splitted[2]
    b = splitted[6]
    return str(splitted[0]), int(a), int(b)


def solution(inputs: list):
    data = dict()
    for player in inputs:
        name, a, b = get_clean_num(player)
        data[name] = a*4+b*2
    results = sorted(data.items(), key=lambda x: x[1])
    results.reverse()
    if results[0][1] == results[1][1]:
        print("DRAW")
    else:
        print(
            f"{results[0][0]} is the MVP with {results[0][1]} points!")


def get_inputs(players_size) -> list:
    inputs = list()

    count = 1
    for line in sys.stdin:
        line = line.replace('\n', '').replace('\r', '')
        inputs.append(str(line))
        if count == players_size:
            break
        count += 1

    return inputs


players_size = int(input())
solution(get_inputs(players_size))
