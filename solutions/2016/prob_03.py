s_f = str(input())
size = int(input())
s = s_f.lower()

if s == "m":
    if size < 44:
        print(size - 34.5)
    else:
        print(size - 35)
else:
    if size < 40:
        print(size - 31.5)
    else:
        print(size - 32)
