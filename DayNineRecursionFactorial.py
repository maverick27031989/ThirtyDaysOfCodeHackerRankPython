import math

N = int(input())
fact = 1

# option 1: using the math function
# math.factorial(N)


# option 2: using without math function
if 2 <= N <= 12:
    for i in range(1, N+1):
        fact = fact * i
    print(fact)


