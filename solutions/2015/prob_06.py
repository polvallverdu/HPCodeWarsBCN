import math

def truncate(number, digits) -> float:
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper

text = input().replace("#", "").replace(" ", "").lower()

vowels_list = "aeiou"
consonants_list = "bcdfghjklmnpqrstvwxyz"

vowels = 0
consonants = 0

for letter in text:
    if letter in vowels_list:
        vowels += 1
    elif letter in consonants_list:
        consonants += 1
    
print(f"Consonants: {consonants}")
print(f"Vowels: {vowels}")

ratio = truncate(vowels/consonants, 3)

if ratio == 0:
    ratio = "Infinite"

print(f"Ratio: {ratio}")
