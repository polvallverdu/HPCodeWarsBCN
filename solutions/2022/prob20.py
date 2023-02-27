def rows_to_columns(rows: list[list[any]]) -> list[list[any]]:
    num_rows = len(rows)
    num_cols = len(rows[0])
    columns = [[] for _ in range(num_cols)]
    for i in range(num_rows):
        for j in range(num_cols):
            columns[j].append(rows[i][j])
    return columns

board = [
  list(input().rstrip()),
  list(input().rstrip()), 
  list(input().rstrip()),
]

def invalid():
  print("NOT VALID")
  exit()

count = [0, 0]

playing = False
for row in board:
  if len(row) != 3:
    invalid()
  for char in row:
    if char == "X":
      count[0] += 1
    elif char == "O":
      count[1] += 1
    elif char == "_":
      playing=True
    else:
      invalid()

if abs(count[0]-count[1]) > 1:
  invalid()

if playing:
  print("PLAYING")
  exit()

winners = []

for row in board:
  if "".join(row) == "XXX":
    winners.append("X")
  elif "".join(row) == "000":
    winners.append("0")

for colunn in rows_to_columns(board):
  if "".join(row) == "XXX":
    winners.append("X")
  elif "".join(row) == "000":
    winners.append("0")

check1 = board[0][0] + board[1][1] + board[2][2]
check2 = board[0][2] + board[1][1] + board[2][0]

if check1 == "XXX":
  winners.append("X")
elif check1 == "000":
  winners.append("0")

if check2 == "XXX":
  winners.append("X")
elif check2 == "000":
  winners.append("0")

if len(winners) == 0:
  print("IT'S A TIE")
else:
  print("{} WON".format(winners[0]))