months = ["Thern", "Thanern", "Nimmer", "Anner", "Irrem", "Moth", # 6
          "Tuwa", "Osme", "Ockre", "Kus", "Hakanna", "Gor", "Susymy", "Grende"]

days = ["Getheny", "Sordny", "Eps", "Arhad", "Netherhad", "Streth",
        "Berny", "Orny", "Harhahad", "Guyrny", "Yrny", "Posthe", "Tormenbod", # 13
        "Odgetheny", "Odsordny", "Odeps", "Odarhad", "Onnetherhad", "Odstreth",
        "Obberny", "Odorny", "Odharhahad", "Odguyrny", "Odyrny", "Opposthe",
        "Ottormenbod"]

first_time, second_time = input().rstrip().split(" - ")
first_time = first_time.split(" ")
second_time = second_time.split(" ")

first_day, first_month, second_day, second_month = days.index(first_time[0])+ 1, months.index(first_time[1])+ 1, days.index(second_time[0])+ 1, months.index(second_time[1])+ 1

month_difference = second_month - first_month
day_difference = second_day - first_day
dif = 0

if month_difference < 0:
  dif += 26*14

month_days = abs(month_difference)*26

print(f"{abs((month_days-first_day+second_day)-dif)}")

