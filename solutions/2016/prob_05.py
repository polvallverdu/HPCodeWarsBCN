records = str(input())
city_points_W = 0
city_points_Z = 0

while records != "#":
    (city), (speed), (speedmax) = records.split()
    city = city.lower()

    if city == "w":
        if int(speed) > int(speedmax):
            city_points_W =+ 1

    else:
        if int(speed) > int(speedmax):
            city_points_Z =+ 1

    city = " "
    speed = 0
    speedmax = 0

    records = str(input())

else:
    print(city_points_W, "fines to Whynot")
    print(city_points_Z, "fines to Zzyzx")

    if city_points_W > city_points_Z:
        print("Zzyzx habitants are safer at driving than Whynot ones")

    if city_points_W == city_points_Z:
        print("Whynot and Zzyzx habitants are equally safe at driving")

    else:
        print("Whynot habitants are safer at driving than Zzyzx ones")
