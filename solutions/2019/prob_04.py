processor = int(input())
grafics_card = int(input())
free_storage = int(input())

if processor >= 5 and grafics_card >= 2 and free_storage >= 50:
    print('You can run the game')
else:
    print('You can NOT run the game')
