people = int(input())
if ((people % 5) == 0):
    people = people//5
else:
    people = people//5 + 1

print('- {0} natural yogurt'.format(people*1))
print('- {0} natural yogurt'.format(people*3))
print('- {0} natural yogurt'.format(people*250))
print('- {0} natural yogurt'.format(people*125))
print('- {0} natural yogurt'.format(people*250))
print('- {0} natural yogurt'.format(people*125))
print('- {0} natural yogurt'.format(people*1))
