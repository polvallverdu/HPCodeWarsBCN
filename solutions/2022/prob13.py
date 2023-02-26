conversions = {
    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "A": "Alpha",
    "B": "Bravo",
    "C": "Charlie",
    "D": "Delta",
    "E": "Echo",
    "F": "Foxtrot",
    "G": "Golf",
    "H": "Hotel",
    "I": "India",
    "J": "Juliett",
    "K": "Kilo",
    "L": "Lima",
    "M": "Mike",
    "N": "November",
    "O": "Oscar",
    "P": "Papa",
    "Q": "Quebec",
    "R": "Romeo",
    "S": "Sierra",
    "T": "Tango",
    "U": "Uniform",
    "V": "Victor",
    "W": "Whiskey",
    "X": "X-ray",
    "Y": "Yankee",
    "Z": "Zulu",
    ".": "Decimal"
}



lines = []
while True:
  l = input().rstrip()
  if l == "#":
    break
  lines.append(l)

final_output = ""

for line in lines:
  for word in line.split(" "):
    if word in conversions.values():
      final_output += word + " "
      continue

    if word[0].isupper() or word[0].isnumeric():
      for letter in word:
        final_output += conversions[letter] + " "
      continue
    
    final_output += word + " "
  
  final_output = final_output[:-1] + "\n"
  
print(final_output)
