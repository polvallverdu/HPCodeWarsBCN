number_stars = int(input())
stars = ''
if number_stars > 0:
    for i in range(number_stars):
        stars += '*'
else:
    stars = '-'
print(stars)
