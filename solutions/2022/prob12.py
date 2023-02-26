word = input()
final_word = ""
vowels = ["a", "e", "i", "o", "u"]
skip = False
cache_vowel = ""

for x, letter in enumerate(word):
  if cache_vowel != "" and not skip:
    if letter in vowels:
      if len(word) == x+1 or word[x+1] not in vowels:
        final_word += letter
        final_word += cache_vowel
      else:
        final_word += cache_vowel
        final_word += letter
      cache_vowel = ""
      skip = True
    else:
      final_word += cache_vowel
      final_word += letter
      cache_vowel = ""
  else:
    if cache_vowel != "":
      final_word += cache_vowel
    if letter in vowels:
      cache_vowel = letter
    else:
      cache_vowel = ""
      skip = False
      final_word += letter

if cache_vowel != "":
  final_word += cache_vowel

print(final_word)