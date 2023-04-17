import sys

t = int(sys.stdin.readline().rstrip())
memo = {0: [1,0], 1:[0,1]}

def fibonacci(n):
    if n == 0:
        return memo[0]
    elif n == 1:
        return memo[1]
    elif n in memo:
        return memo[n]
    else:
        memo[n] = [0,0]
        memo[n][0] = fibonacci(n-1)[0] + fibonacci(n-2)[0]
        memo[n][1] = fibonacci(n-1)[1] + fibonacci(n-2)[1]
        return memo[n]

for i in range(t):
    n = int(sys.stdin.readline().rstrip())
    print(*fibonacci(n))
