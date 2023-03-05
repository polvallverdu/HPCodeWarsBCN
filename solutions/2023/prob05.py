a = input()
vowels = list("aeiouAEIOU")

for v in vowels:
  a = a.replace(v, "*")
  
print(a)