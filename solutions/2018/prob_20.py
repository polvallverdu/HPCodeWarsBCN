orden = input().split()
control = 0

while control == 0:
    line = ''
    try:
        line = input()
    except:
        control = 1
    if line == '':
        control = 1
    else:
        [racer_2, palabra, racer_1] = input().split()
        pos_racer_1 = orden.index(racer_1)
        temp_str = orden[pos_racer_1]
        orden[pos_racer_1] = orden[pos_racer_1 + 1]
        orden[pos_racer_1] = temp_str

for racer in orden:
    print(racer)
