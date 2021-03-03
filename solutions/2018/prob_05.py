
text = 'Name is a age year-old gender. Pronoun is living with possesive pronoun parents in an apartment in the centre of city, where pronoun hangs out with possesive pronoun friends. Moreover, in possesive pronoun free time pronoun plays favourite sportin a team called favourite team. name would like to pursue a career in ideal job when pronoun is older, that is why pronoun is studying hard.'

name = str(input())
age = str(input())
gender = str(input())
city = str(input())
favorite_sport = str(input())
favorite_team = str(input())
ideal_job = str(input())

pronom_possesive = ''
pronom_upper = ''
pronom = ''

if(gender == 'girl'):
    pronom = 'she'
    pronom_possesive = 'her'
    pronom_upper = 'She'
else:
    pronom = 'he'
    pronom_possesive = 'his'
    pronom_upper = 'He'

print(text.replace('Name', name).replace('age', age).replace('gender', gender).replace('pronoun', pronom).replace('name', name).replace('Pronoun',
                                                                                                                                        pronom_upper).replace('possesive pronoun', pronom_possesive).replace('favourite sport', favorite_sport).replace('ideal job', ideal_job).replace('city', city).replace('favourite team', favorite_team))
