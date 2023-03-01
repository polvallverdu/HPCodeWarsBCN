words = []

while True:
  i = input().rstrip()
  if i == "#":
    break
  words.append(i)

piramids = []
for word in words:
  counter = len(word)-1
  spaces = 0
  piramid = []
  for i, letter in enumerate(word):
    piramid.append(" "*spaces + (letter*counter)+word[i:] + " "*spaces)
    counter -= 1
    spaces += 1
  piramid.reverse()
  piramids.append(piramid)

biggest_word = max([len(x) for x in piramids])
for piramid in piramids:
  for _ in range(biggest_word-len(piramid)):
    piramid.insert(0, len(piramid[0])*" ")

for x in range(biggest_word):
  for i, piramid in enumerate(piramids):
    print(piramid[x], end=" " if len(piramids)-1 != i else "\n")