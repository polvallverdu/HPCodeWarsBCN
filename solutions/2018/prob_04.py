list= dict([("Mercury",88),    ("Venus",225),("Earth",365),     ("Mars",687),("Jupiter",4333),  ("Saturn",10759),("Uranus",30689),  ("Neptune",60182)])
age = int(input())
planet = input()
earthAge = (age * list[planet])//365
print(earthAge)