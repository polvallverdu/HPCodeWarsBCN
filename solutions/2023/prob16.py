a = input().strip().split(" ")
res = []
cache_upper = ""
noupper = ""
point = False

if a[-1].endswith("."):
  a[-1] = a[-1][:-1]
  point = True

for x, word in enumerate(a):
  if word[0].isupper():
    if cache_upper != "":
      cache_upper += word[0]
      if len(a)-1 == x:
        res.append(cache_upper)
    elif noupper == "":
      noupper = word
      if len(a)-1 == x:
        res.append(noupper)
    else:
      cache_upper += noupper[0]
      cache_upper += word[0]
      noupper = ""
      if len(a)-1 == x:
        res.append(cache_upper)
    continue
  if noupper != "":
    res.append(noupper)
    noupper = ""
  elif cache_upper != "":
    res.append(cache_upper)
    cache_upper = ""
  res.append(word)
  
print(" ".join(res) + ("." if point else ""))