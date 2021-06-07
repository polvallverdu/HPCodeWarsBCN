import sys


def solution(inputs: list, incoming_call: int):
    if incoming_call in inputs:
        print("1")
    else:
        print("0")


def get_inputs() -> list:
    inputs = list()
    incoming_call = 0
    get_incoming_call = False

    for line in sys.stdin:
        line = line.replace('\n', '').replace('\r', '').lstrip().rstrip()
        if line == "0":
            get_incoming_call = True
        elif get_incoming_call:
            incoming_call = int(line)
            break
        else:
            inputs.append(int(line))

    return inputs, incoming_call

inputs, incoming_call = get_inputs()
solution(inputs, incoming_call)
