def areAnagrams(a, b): 
    if a == b: 
        # a word is not an anagram of itself 
        return False 
 
    # Check if a and b sorted alphabetically are equal 
    return sorted(a) == sorted(b) 
 
subject = input() 
words   = input().split() 
 
first = True 
for word in words: 
    if areAnagrams(word, subject): 
        if not first: 
            print(' ', end='') 
        print(word, end='') 
        first = False 
 
if not first: 
    print('')