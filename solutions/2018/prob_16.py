

def is_prime(x):
    prime = True
    i = 2
    while i < x:
        if x/i == 0:
            prime = False
            break
        i += 1
    return prime


def reverse_num(num: int) -> int:
    reverse = 0
    while num > 0:
        reminder = num % 10
        reverse = (reverse*10) + reminder
        num = num//10
    return reverse


def polindrome(num: int) -> bool:
    return str(num) == str(num)[::-1]


number = int(input())
result = is_prime(number) and is_prime(reverse_num(number))
result = result and not polindrome(number)
if result:
    print(str(number) + " is an emirp number")
else:
    print(str(number) + " is not an emirp number")
