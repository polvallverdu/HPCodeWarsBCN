type = input().rstrip()

ranks = "Admiral > Captain > Commander > Lieutenant > Officer".split(" > ")

def check_rank(rank):
  if rank not in ranks:
    print("Invalid input.")
    exit()

def is_higher_rank(rank1, rank2):
  return ranks.index(rank1) > ranks.index(rank2)

placeholders = [
  "From: ",
  "From rank: ",
  "To: ",
  "To rank: ",
  "Content: ",
  "Timestamp: ",
]
if type == "R":
  line = input().rstrip().split(",")
  
  if is_higher_rank(line[3], line[1]):
    print("<<< URGENT >>>")
  
  for x in range(len(placeholders)):
    if x == 1 or x == 3:
      check_rank(line[x])
    print(placeholders[x] + line[x])
elif type == "S":
  inputs = []
  for x in range(6):
    i = input().rstrip()
    if x == 1 or x == 3:
      check_rank(i)
    inputs.append(i)
  
  if is_higher_rank(inputs[3], inputs[1]):
    inputs.insert(0, "URGENT")
  
  print(",".join(inputs))
else:
  print("Invalid input.")