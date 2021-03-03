años = int(input())
planet = str(input())

planetas = dict([('Mercury', 88), ('Venus', 225), ('Earth', 365), (
    'Mars', 687), ('Jupiter', 4333), ('Saturn', 10759), ('Uranus', 30689), ('Neptune', 60182)])


print(años*planetas[planet]//365)
