ismale = input() == "Male"
redcells = float(input())
whitecells = int(input())
pla = int(input())
hemoglobin = float(input())
hematocrit = int(input())

n = "NORMAL"
d = "VISIT THE DOCTOR"

if ismale:
  print("Red blood cells: " + (n if redcells >4.3 and redcells < 5.9 else d))
else:
  print("Red blood cells: " + (n if redcells >3.5 and redcells < 5.5 else d))
  
print("White blood cells: " + (n if whitecells >4500 and whitecells < 11000 else d))

print("Platelets: " + (n if pla > 150000 and pla < 400000 else d))

if ismale:
  print("Hemoglobin: " + (n if hemoglobin > 13.5 and hemoglobin < 17.5 else d))
else:
  print("Hemoglobin: " + (n if hemoglobin > 12.0 and hemoglobin < 16.0 else d))
if ismale:
  print("Hematocrit: " + (n if hematocrit > 41 and hematocrit < 53 else d))
else:
  print("Hematocrit: " + (n if hematocrit > 36 and hematocrit < 46 else d))



