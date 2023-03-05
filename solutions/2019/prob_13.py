import string

sentence = input().rstrip().lower()
alphabet = "abcdefghijklmnopqrstuvwxyz"[::-1]
letters = {}
for l in alphabet:
    letters[l] = 0

for l in sentence:
    try:
        letters[l] += 1
    except Exception as e:
        "ignore"

for l, num in letters.items():
    print(f"{l} = {num}")