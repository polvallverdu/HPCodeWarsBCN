import math

ciudadanos = int(input())
dias = 0
zombies = 1

while ciudadanos > 0:
    dias += 1
    nuevos_zombies = min(ciudadanos, zombies*2)
    muertos = math.ceil(zombies*0.25)
    zombies += nuevos_zombies - muertos
    ciudadanos -= zombies

print(dias, 'days')
