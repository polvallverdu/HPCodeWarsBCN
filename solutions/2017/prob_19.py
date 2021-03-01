n = int(input())
count = n-2
print(' '*(n+(n-1))+'_'*n)

for x in range(n-1):
    print(' '*(n + count)+'_|')
    count -= 1
print('_'*(n-1)+'|')
