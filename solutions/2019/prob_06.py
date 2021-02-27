people = int(input())
if ((people % 5) == 0):
    people = people//5
else:
    people = people//5 + 1

print('- {0} natural yogurt.'.format(people*1))
print('- {0} eggs.'.format(people*3))
print('- {0}gr flour.'.format(people*250))
print('- {0}gr cocoa powder.'.format(people*125))
print('- {0}gr sugar.'.format(people*250))
print('- {0}gr olive oil.'.format(people*125))
print('- {0} packet of yeast.'.format(people*1))
