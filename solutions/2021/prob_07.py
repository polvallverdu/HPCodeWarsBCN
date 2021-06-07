chars = list()
kjdas = False

for char in input().lower().replace(".", "").replace(",", "").replace("#", "").replace("'", "").replace("\"", "").replace(":", "").replace(";", "").replace("-", ""):
    if char in chars:
        print("Not an isogram")
        kjdas = True
        break
    chars.append(char)


if not kjdas:
    print("Isogram detected")
