team_a, team_b = input().split(" - ")
first_set = input().split(" - ")
second_set = input().split(" - ")

first_winner = team_a if int(first_set[0]) > int(first_set[1]) else team_b
second_winner = team_a if int(second_set[0]) > int(second_set[1]) else team_b

if first_winner == second_winner:
  score = "2 - 0" if first_winner == team_a else "0 - 2"
else:
  tie_breaker = input().split(" - ")
  tie_winner = team_a if int(tie_breaker[0]) > int(tie_breaker[1]) else team_b
  score = "2 - 1" if tie_winner == team_a else "1 - 2"
  first_winner = tie_winner

print(f"{first_winner} won the match {score}.")

