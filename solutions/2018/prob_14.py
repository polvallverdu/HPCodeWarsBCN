num = int(input())
# Converts to a binary string
num_bin = bin(num)
# And check the max power. I.e 42=0b101010 -> Max power==5
leng = len(num_bin)

print(len(num_bin)-2-1)
