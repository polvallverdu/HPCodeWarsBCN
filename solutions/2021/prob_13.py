import sys


def solution(inputs: list):
    print(inputs)


data = dict()

a = input().split(' ')
b = input().split(' ')
notes = list()


for x in range(0, len(a)):
    notes.append(float(a[x])*float(b[x]))

final_note = 0

for note in notes:
    final_note += note

print(
    f"The student final grade is {round(final_note, 1)}")
