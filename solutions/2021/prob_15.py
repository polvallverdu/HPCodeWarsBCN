rawdate = int(input())
name = input()

sentences = {
    1: "You tend to be critical of yourself",
    2: "You have a great deal of unused capacity which you have not turned to your advantage.",
    3: "While you have some personality weaknesses, you are generally able to compensate for them.",
    4: "At times you are extroverted, affable, sociable, while at other times you are introverted, wary, reserved.",
    5: "Disciplined and self-controlled outside, you tend to be worrisome and insecure inside.",
    6: "At times you have serious doubts as to whether you have made the right decision or done the right thing.",
    7: "You prefer a certain amount of change and variety and become dissatisfied when hemmed in by restrictions and limitations.",
    8: "You pride yourself as an independent thinker and do not accept others' statements without satisfactory proof.",
    9: "You have found it unwise to be too frank in revealing yourself to others."
}

total = 0

for num in str(rawdate):
    total += int(num)

for letter in name:
    total += ord(letter)

safe_total = total
while True:
    total = 0
    for num in str(safe_total):
        total += int(num)
    if len(str(total)) == 1:
        break
    safe_total = total

print(sentences[total])
