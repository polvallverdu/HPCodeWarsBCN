# amount = int(input())

# sumatoria = 0
# i = 1
# while True:
#   i += sumatoria
#   sumatoria += 1

#   if sumatoria == amount:
#     print("True")
#     exit()
#   elif not sumatoria < amount:
#     print("False")
#     exit()
# 


# A triangular number t meets the equation t = Sum(1..n) = n*(n+1)/2 that is, 
# 
#       t = (n^2i +i n) / 2 
# 
# and we get this quadratic equation: 
# 
#        n^2 + n - 2t = 0 
# 
# That can be solved as: 
# 
#            n = (-1 +/- sqrt(1+8t)) / 2 
# 
# The negative solution for n is discarded. And the positive solution for n is 
# 
#            n = (-1 + sqrt(1+8t)) / 2 
# 
# If t is a triangular number, n must be positive integer number, that follows 
# 
# a) 1+8t is a perfect square and   
#  
# b) -1 + sqrt(1+8t) is divisible by 2. This is true since 1+8t is odd and since  
#    it is a perfect square the square root is also odd. Finally substracting  
#    one unit the result is even 
#  
# Then to check if t is a triangular number: (1 + 8 * t) == (round(sqrt(1 + 8 * t))) 

import math 

t = int(input()) 

n = 1 + 8 * t 
m = round(math.sqrt(n)) 

#print(n, m**2) 

print(n == m**2)