alphabet = input().rstrip()

words = []
while True:
  i = input().rstrip()
  if i == "#":
    break
  words.append(i)

new_words = {}

for word in words:
  w = ""
  for l in word:
    w+=str(alphabet.index(l))
  new_words[word] = w
  
new_words = sorted(new_words.items(), key=lambda x:x[1])

finalline = ""
for word, weight in new_words:
  finalline += word + " "

print(finalline[0:-1])
