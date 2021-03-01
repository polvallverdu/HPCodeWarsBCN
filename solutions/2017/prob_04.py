n = int(input())
m = int(input())
sumacon = 0
sumapre = 0

for x in range(m):
    sumacon += n+(x+1)
    sumapre += n-(x+1)

print(sumacon, sumapre)
