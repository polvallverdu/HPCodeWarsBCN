from math import remainder


base62String = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

a = int(input())
shortened_url = ""

while a >= 62:
  r = a % 62
  a //= 62
  shortened_url = base62String[r] + shortened_url

shortened_url = base62String[a] + shortened_url
print(shortened_url)
