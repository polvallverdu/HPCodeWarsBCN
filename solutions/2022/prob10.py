type = input().rstrip()

ranks = "Admiral > Captain > Commander > Lieutenant > Officer".split(" > ")

def check_rank(rank):
  if rank not in ranks:
    print("Invalid input.")
    exit()

placeholders = [
  "From: ",
  "From rank: ",
  "To: ",
  "To rank: ",
  "Content: ",
  "Timestamp: ",
]
if type == "R":
  line = input().split(",")
  print("<<< URGENT >>>")
  for x in range(len(placeholders)):
    if x == 1:
      check_rank(line[x])
    print(placeholders[x] + line[x])
elif type == "S":
  inputs = ["URGENT"]
  for x in range(6):
    i = input()
    if x == 1:
      check_rank(i)
    inputs.append(i)
  print(",".join(inputs))
else:
  print("Invalid input.")