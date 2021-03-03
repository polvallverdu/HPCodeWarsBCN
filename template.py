import sys


def solution(inputs: list):
    print(inputs)


def get_inputs() -> list:
    inputs = list()

    for line in sys.stdin:
        line = line.replace('\n', '').replace('\r', '')
        if line == '#' or line == '' or line == "0":
            break

        inputs.append(str(line))

    return inputs


if __name__ == "__main__":
    solution(get_inputs())
