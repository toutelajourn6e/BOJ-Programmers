import sys

d = [0] * 1000001
d[0] = 1
d[1] = 1
d[2] = 2
mod = 1000000009

for n in range(3, 1000001):
    d[n] = d[n-1] + d[n-2] + d[n-3]
    d[n] %= mod

    
t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    print(d[n])
    
