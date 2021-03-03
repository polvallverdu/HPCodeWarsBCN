def decimalToBinary(num):
    """This function converts decimal number
    to binary and prints it"""
    if num > 1:
        decimalToBinary(num // 2)
    return num % 2

time_24h = str(input()).replace(':', '')
time = list()
times_binary = list()

for char in time_24h:
     time.append(int(char))

for num in time:
     binary = str(decimalToBinary(num))
     binaryNums = list()
     for char in binary:
          binaryNums.append(char)

for x in range(6):
     to_print = ''
     for num in times_binary:
          if num[x] == 0:
               to_print += '-'
          else:
               to_print += 'o'
     print(to_print)

