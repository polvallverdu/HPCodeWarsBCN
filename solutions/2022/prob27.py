num_people = int(input().rstrip())
logs = {}

for _ in range(num_people):
  name, join, leave = input().rstrip().split(" ")
  jhour, jminute = join.rstrip().split(":")
  lhour, lminute = leave.rstrip().split(":")
  join = int(jhour)*60+int(jminute)
  leave = int(lhour)*60+int(lminute)
  
  if str(join) not in logs.keys():
    logs[str(join)] = []
  if str(leave) not in logs.keys():
    logs[str(leave)] = []
  
  logs[str(join)].append({
    "name": name,
    "type": "join",
  })
  logs[str(leave)].append({
    "name": name,
    "type": "leave"
  })

ss = sorted(logs.items(), key=lambda x:int(x[0]))

people = 0
people_names = []
passes = []
for x, t in enumerate(ss):
  time, actions = t
  for action in actions:
    if action["type"] == "join":
      people += 1
      people_names.append(action["name"])
    elif action["type"] == "leave":
      people -= 1
      people_names.remove(action["name"])
  if x+1 != len(ss):
    to_append = [people, people_names.copy(), int(ss[x+1][0])-int(time)]
    passes.append(to_append)

sss = sorted(passes, key=lambda x:x[0], reverse=True)
m = sss[0][0]
ssss = [x for x in sss if x[0] == m]
# ssss.reverse()

for line in ssss:
  print("Max capacity of {} people during {} minutes with following people: {}".format(line[0], line[2], ", ".join(line[1])))
