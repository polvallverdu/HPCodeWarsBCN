

def isPrime(x):
    prime = True
    i = 2
    while i < x:
        if x/i == 0:
            prime = False
            break
        i += 1
    return prime


def reverse(x):
    reverse = 0
    while x > 0:
        reminder = x % 10
        reverse = (reverse*10) + reminder
        x = x//10
    return reverse


def polindrome(x):
    return(str(x) == str(x)[::-1])


number = int(input())
result = isPrime(number) and isPrime(reverse(number))
result = result and not polindrome(number)
if result:
    print(str(number) + " is an emirp number")
else:
    print(str(number) + " is not an emirp number")
