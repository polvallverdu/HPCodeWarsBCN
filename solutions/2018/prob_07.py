gpu_freq = int(input())
games = 0

while True:
     requested_freq = int(input())
     
     if requested_freq == 0:
          break
     
     if gpu_freq > requested_freq:
          games = games + 1
     
print(games)
