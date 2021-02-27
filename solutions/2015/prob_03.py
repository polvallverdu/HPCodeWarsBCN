age = int(input())
real_age = 0
name = input()

if age > 2:
    real_age = 2*10 + (age-2) * 4
else:
    real_age = age*10

# Better solution 
# print("{name} is {real_age} human years old")
print(name + " is " + str(real_age) + " human years old")
