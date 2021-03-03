import sys


def solution(inputs: list):
    for line in inputs:
        text = line[::-1]
        final_text = ""

        for letter in text:
            if letter == 'G':
                final_text += 'C'
            elif letter == 'C':
                final_text += 'G'
            elif letter == 'T':
                final_text += 'A'
            elif letter == 'A':
                final_text += 'T'
        print(final_text)


def get_inputs() -> list:
    inputs = list()

    for line in sys.stdin:
        line = line.replace('\n', '').replace('\r', '')
        if line == '.':
            break

        inputs.append(str(line))

    return inputs


if __name__ == "__main__":
    solution(get_inputs())
