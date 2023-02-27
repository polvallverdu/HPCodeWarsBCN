word = input()
anagrams = input().split(" ")

def get_list_alphabetic_order(l: list) -> list:
  list_words = []
  for i in l:
    if i != word:
      list_words.append(sorted(i))
  return list_words
    

word_sorted= ''.join(sorted(word)).lower()

anagrams_sorted = get_list_alphabetic_order(anagrams)
res = []

for i, ass in enumerate(anagrams_sorted):
  if word_sorted == ass:
    res.append(anagrams[i])

print(" ".join(res))
