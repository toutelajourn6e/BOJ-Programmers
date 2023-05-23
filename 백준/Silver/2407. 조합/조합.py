from math import factorial as f

n, m = map(int, input().split())

result = f(n) // (f(n-m) * f(m))
print(result)