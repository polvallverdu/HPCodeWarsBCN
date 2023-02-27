matrix_l = int(input())
matrix = []
for _ in range(matrix_l):
  i = input().rstrip().split(" ")
  a = []
  for char in i:
    a.append(int(char))
  matrix.append(a)
    
pequeño = []

for row in matrix:
  pequeño.append(min(row))

for i, p in enumerate(pequeño):
  columna = []
  x = matrix[i].index(p)
  for row in matrix:
    columna.append(row[x])

  if max(columna) == p:
    print(f"The saddle point is {p}")
    exit()

print("No saddle point in the matrix")