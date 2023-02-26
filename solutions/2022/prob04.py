def get_inputs(line) -> tuple:
  b = line.split(" ")
  return b[0], int(b[1]), int(b[2])

games = int(input())
team_name, team_wins, team_lose = get_inputs(input())
other_team_name, other_team_wins, other_team_lose = get_inputs(input())

magic = games - team_wins - other_team_lose + 1
print(f"{team_name} must win {magic} matches")