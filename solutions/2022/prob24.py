def transpose_matrix(rows: list) -> list:
    num_rows = len(rows)
    num_cols = len(rows[0])
    columns = [[] for _ in range(num_cols)]
    for i in range(num_rows):
        for j in range(num_cols):
            columns[j].append(rows[i][j])
    return columns

def replace(line: str, word: str) -> str:
  return line.replace(word, "0"*len(word)).replace(word[::-1], "0"*len(word))

def search_word(rows: list, word) -> tuple:
  counter = 0
  
  for i, row in enumerate(rows.copy()):
    newrow = replace("".join(row), word)
    if newrow != "".join(row):
      rows[i] = list(newrow)
      counter += 1
  
  columns = transpose_matrix(rows)
  for i, column in enumerate(columns.copy()):
    newcolumn = replace("".join(column), word)
    if newcolumn != "".join(column):
      counter += 1
      for x in range(len(newcolumn)):
        rows[x][i] = newcolumn[x]
  
  for x in range(rows_l):
    diagonal = ""
    for y in range(rows_l):
      diagonal += rows[x][x+y if x+y < len(rows) else x-y]

    newdiagonal = replace("".join(diagonal), word)
    if diagonal != newdiagonal:
      counter += 1
      for y in range(rows_l):
        rows[x][x+y if x+y < len(rows) else x-y] = newdiagonal[y]
  
  for x in range(rows_l):
    diagonal = ""
    for y in range(rows_l):
      diagonal += rows[-x][x+y if x+y < len(rows) else x-y]

    newdiagonal = replace("".join(diagonal), word)
    if diagonal != newdiagonal:
      counter += 1
      for y in range(rows_l):
        rows[x][x+y if x+y < len(rows) else x-y] = newdiagonal[y]

  return counter, rows

words = input().rstrip().split(" ")
rows_l = int(input())
rows = []

for _ in range(rows_l):
  rows.append(list(input().rstrip()))

counter = 0

for w in words:
  c, r = search_word(rows, w)
  counter += c
  rows = r

for row in rows:
  print("".join(row))

counter = 0.0
for row in rows:
  for x in row:
    if x == "0":
      counter += 1
      
total_len = float(rows_l*len(rows[0]))

percentage = (counter*100)/42
print(f"The words given occupy {percentage:.02f}% of the grid.")