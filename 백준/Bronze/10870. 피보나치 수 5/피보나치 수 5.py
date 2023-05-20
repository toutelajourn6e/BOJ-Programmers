import sys
sys.setrecursionlimit(10**6)

n = int(input())
memo = {}

def fibonacci(n):
    if n <= 1:
        return n
    
    if n in memo:
        return memo[n]
    else:
        memo[n] = fibonacci(n-1) + fibonacci(n-2)
        return memo[n]
    
print(fibonacci(n))