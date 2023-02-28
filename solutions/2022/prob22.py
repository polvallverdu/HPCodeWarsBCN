import math
org_s = input()
s = org_s.replace(' ', '')
l = len(s)

lsqrt = math.sqrt(l)
rows = round(float(lsqrt))
columns = int(lsqrt) +1

matrix = []

for _ in range(rows):
  matrix.append([])


for z in range(rows):
  for _ in range(columns):
    if s != '':
      
      matrix[z] += s[0]
      s = s[1::]
    else:
      break
    

def transpose_matrix(matrix: list[list[int]]) -> list[list[int]]:
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    transposed = []
    for j in range(num_cols):
        transposed_row = []
        for i in range(num_rows):
            if j < len(matrix[i]):
                transposed_row.append(matrix[i][j])
            else:
                transposed_row.append(None)
        transposed.append(transposed_row)
    return transposed

m = transpose_matrix(matrix)

msg = ''

for row in m:
  for column in row:
    msg += column if column is not None else ""
  msg += ' '
    
print(msg.rstrip())