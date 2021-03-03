<<<<<<< HEAD
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
=======
name = str(input())
age = int(input())
gender = str(input())
city = str(input())
sport = str(input())
team = str(input())
job = str(input())

proun = " "
possesive_proun = " "
Proun = " "


if gender == "girl":
     pronoun = "she"
     Pronoun = "She"
     possesive_pronoun = "her"
else:
     pronoun = "he"
     Pronoun = "He"
     possesive_pronoun = "her"

output_string = name, " is a ", age, " year-old ", gender\
     , ". ", Pronoun, " is living with ", possesive_pronoun\
          , " parents in an apartment in the centre of ", city\
               , ", where ", pronoun, " hangs out with ", possesive_pronoun\
                    , " friends. Moreover, in ", possesive_pronoun, " free time "\
                         , pronoun+" plays ", sport, " in a team called ", team\
                              , ". ", name, " would like to pursue a career in ", job\
                                   , " when ", pronoun, " is older, that's why ", pronoun\
                                        , " is studying hard."

print(output_string)
>>>>>>> bb138f27f174278e24adb2939c523606a2d8749f
