gpu = int(input())
mingpu = int(input())
listvideogamos = 0
while (mingpu != 0):
    if(gpu >= mingpu):
        listvideogamos += 1
    mingpu = int(input())

print(listvideogamos)
