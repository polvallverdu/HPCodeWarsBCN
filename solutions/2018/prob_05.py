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
