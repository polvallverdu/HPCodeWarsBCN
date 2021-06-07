import sys


def solution(columns: int, rows: int, sequences_size: int, inputs: list):
    for line_num in range(0, rows):
        row = ""
        for x in range(0, sequences_size):
            index = (line_num+x*rows)
            if index < 0:
                index = 0
            row += inputs[index]
        print(row)


def get_inputs() -> tuple:
    columns = 0
    rows = 0
    got_colums_rows = False

    sequences_size = 0
    got_sequences_size = False

    inputs = list()
    count = 0

    for line in sys.stdin:
        line = line.replace('\n', '').replace('\r', '')
        if not got_colums_rows:
            raw_sizes = line.split(' ')
            columns = int(raw_sizes[0])
            rows = int(raw_sizes[1])
            got_colums_rows = True
        elif not got_sequences_size:
            sequences_size = int(line)
            got_sequences_size = True
        else:
            inputs.append(str(line))
            if count == (rows*sequences_size)-1:
                break
            count += 1

    return columns, rows, sequences_size, inputs

columns, rows, sequences_size, inputs = get_inputs()
solution(columns, rows, sequences_size, inputs)
