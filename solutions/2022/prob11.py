times = []
for i in input().split(", "):
  hour_str, minute_str = i.split(":")
  times.append((int(hour_str)*60)+int(minute_str))

all_time = times[0]
times.remove(all_time)

for time in times:
  all_time -= time

passed = all_time<0
all_time = abs(all_time)

hour = all_time//60
minute = all_time%60

print(("{} hours of viewing remaining." if not passed else "LIMIT EXCEEDED BY {} hours. Benigno punished!").format(f"{hour:02}:{minute:02}"))
