tocw = int(input())
bumw = int(input())
n = int(input())

possibilities = {}

global stop
stop = False
global i
i = 0

global m
m = 500

def putTree(tocs, bums):
  global i
  global stop
  global m
  
  t = tocw*tocs + bumw*bums
  
  try:
    possibilities[str(t)]["tocs"]
    return
  except:
    "Can do"
  
  possibilities[str(t)] = {
    "tocs": tocs,
    "bums": bums
  }
  i += 1
  if i == m:
    stop = True
  
  if not stop:
    putTree(tocs+1, bums)
    putTree(tocs, bums+1)

putTree(1, 0)
stop = False
i = 0
putTree(0, 1)

try:
  a = possibilities[str(n)]
  print(str("TOC "*a["tocs"] + "BUM "*a["bums"]).rstrip())
except:
  print(n)