import datetime

# Format: IMG_YYYYMMDD_HHMMSS.jpg
# Reflex format: PDDMMYY_HHMMSS.jpg

city = input().rstrip()
mobile_photos = input().rstrip().split(" ")
reflex_photos = input().rstrip().split(" ")

photos = {}

for mp in mobile_photos:
  year = int(mp[4:8])
  month = int(mp[8:10])
  day = int(mp[10:12])
  hour = int(mp[13:15])
  minute = int(mp[15:17])
  second = int(mp[17:19])
  photos[mp] = datetime.datetime(year=year, month=month, day=day, hour=hour, minute=minute, second=second)

for rp in reflex_photos:
  year = int("20" + rp[5:7])
  month = int(rp[3:5])
  day = int(rp[1:3])
  hour = int(rp[8:10])
  minute = int(rp[10:12])
  second = int(rp[12:14])
  photos[rp] = datetime.datetime(year=year, month=month, day=day, hour=hour, minute=minute, second=second)

photos = sorted(photos.items(), key=lambda x:x[1])
x = 0
for filename, _ in photos:
  print(f"mv {filename} {city}_{x:03}.jpg")
  x+=1