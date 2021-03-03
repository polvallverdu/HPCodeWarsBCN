n = int(input())

matrix = [[None for i in range(n)] for x in range(n)]

for line in range(n):
    line_int = [int(i) for i in input().split()]
    matrix[n-line-1] = line_int

num_shots = int(input())
num_hits = 0

for x in range(num_shots):
    [x, y] = [int(i) for i in input().split()]
    if matrix[y][x] == 1:
        num_hits += 1
        matrix[y][x] = 0

print(num_hits)
