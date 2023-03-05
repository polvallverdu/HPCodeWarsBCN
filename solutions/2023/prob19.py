import math

dis = float(input())
angle = float(input())*(2*math.pi/360)

mind = dis-3+(0.0427/2)
maxd = dis+3-(0.0427/2)

mintime = math.sqrt((2*mind*math.sin(angle))/(9.8*math.cos(angle)))
maxtime = math.sqrt((2*maxd*math.sin(angle))/(9.8*math.cos(angle)))

minspeed = mind/(math.cos(angle)*mintime)
maxspeed = maxd/(math.cos(angle)*maxtime)

print(f"The maximum speed is: {maxspeed:.02f} m/s.")
print(f"The minimum speed is: {minspeed:.02f} m/s.")
