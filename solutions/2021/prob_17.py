def solution(num: int):
    periodic = ""
    count = 0
    for char in str(num):
        if len(periodic) == 0:
            periodic += char
        else:
            if count != 0 and count == len(periodic):
                count = 0
            if char == periodic[count]:
                count += 1
            else:
                periodic += char
    if count != 0 and count == len(periodic):
        print(f"The number {num} is periodic and its period is {periodic}")
    else:
        print(f"The number {num} is NOT periodic")


solution(int(input()))
