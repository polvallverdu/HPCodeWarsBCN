import re
times = []
for num_times in range(3):
    # No error detection in the input format!
    a = [int(i) for i in re.findall('[0-9]+', input())]
    times.append(a)

# Lets add the times
total = [0, 0, 0]
# loop hh mm ss
for x in range(3):
    for y in range(len(times)):
        total[x] = total[x]+times[y][x]
# And reduce the minutes and seconds to 60
total[1] = total[1]+int(total[2]/60)
total[2] = total[2] % 60
total[0] = total[0]+int(total[1]/60)
total[1] = total[1] % 60

print("%02dh%02dm%02ds" % (total[0], total[1], total[2]))
