import sys


def format_list(inputs: list) -> list:
    to_return = list()
    for hour in inputs:
        time = list()
        raw_hour = hour.split(':')

        if int(raw_hour[0]) >= 12:
            time.append(float(raw_hour[0])-12)
        else:
            time.append(float(raw_hour[0]))
        time.append(float(raw_hour[1]))

        to_return.append(time)

    return to_return


def get_minutes(minute: int) -> tuple:
    to_multiply = 0
    to_restar = 0
    if minute >= 0 and minute < 5:
        to_multiply = 0
    if minute >= 5 and minute < 10:
        to_multiply = 1
        to_restar = 5
    if minute >= 10 and minute < 15:
        to_multiply = 2
        to_restar = 10
    if minute >= 15 and minute < 20:
        to_multiply = 3
        to_restar = 15
    if minute >= 20 and minute < 25:
        to_multiply = 4
        to_restar = 20
    if minute >= 25 and minute < 30:
        to_multiply = 5
        to_restar = 25
    if minute >= 30 and minute < 35:
        to_multiply = 6
        to_restar = 30
    if minute >= 35 and minute < 40:
        to_multiply = 7
        to_restar = 35
    if minute >= 40 and minute < 45:
        to_multiply = 8
        to_restar = 40
    if minute >= 45 and minute < 50:
        to_multiply = 9
        to_restar = 45
    if minute >= 50 and minute < 55:
        to_multiply = 10
        to_restar = 50
    if minute >= 55 and minute < 60:
        to_multiply = 11
        to_restar = 55

    return 30*to_multiply, minute-to_restar


def solution(rawinputs: list):
    inputs = format_list(rawinputs)

    for rawhour in inputs:
        hour_angle = rawhour[0]*30+(rawhour[1]*0.5)

        minutes, units = get_minutes(rawhour[1])
        minutes_angle = minutes+units*6

        r = 0
        if hour_angle > minutes_angle:
            r = hour_angle-minutes_angle
        else:
            r = minutes_angle-hour_angle
        
        if 360-r < r:
            print(360-r)
        else:
            print(r)


def get_inputs() -> list:
    inputs = list()

    for line in sys.stdin:
        line = line.replace('\n', '').replace('\r', '').lstrip().rstrip()
        if line == '#':
            break

        inputs.append(str(line))

    return inputs


solution(get_inputs())
