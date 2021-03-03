<<<<<<< HEAD
gpu = int(input())
mingpu = int(input())
listvideogamos = 0
while (mingpu != 0):
    if(gpu >= mingpu):
        listvideogamos += 1
    mingpu = int(input())

print(listvideogamos)
=======
gpu_freq = int(input())
games = 0

while True:
     requested_freq = int(input())
     
     if requested_freq == 0:
          break
     
     if gpu_freq > requested_freq:
          games = games + 1
     
print(games)
>>>>>>> bb138f27f174278e24adb2939c523606a2d8749f
