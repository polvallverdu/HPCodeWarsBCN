players_n = int(input())

players = []

for _ in range(players_n):
    a = input().rstrip().replace(" scored", "").replace(" goal(s) and earned", "").replace(" spade(s)", "")
    name, goals, spades = a.split(" ")
    players.append([name, int(goals), int(spades)])

res = {}
for p in players:
    res[p[0]] = p[1]*4+p[2]*2

s = sorted(res.items(), key=lambda x:x[1], reverse=True)

if len(s) == 1 or s[0][1] != s[1][1]:
    print("{} is the MVP with {} points!".format(s[0][0], s[0][1]))
else:
    print("DRAW")