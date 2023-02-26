amount = int(input())

a = []

for _ in range(amount):
  xx = input().split(" ")
  a.append([int(xx[0]), int(xx[1])])

pos = [0, 0]

for coord in a:
  yres = coord[1]-pos[1]
  ycoord = "north" if yres > 0 else "south"
  if yres != 0:
    print(f"Walk {abs(yres)} steps {ycoord}")
  
  xres = coord[0]-pos[0]
  xcoord = "east" if xres > 0 else "west"
  if xres != 0:
    print(f"Walk {abs(xres)} steps {xcoord}")
  
  pos = coord
