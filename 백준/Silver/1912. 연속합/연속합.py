import sys

n = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().rstrip().split()))
d = [0] * n
d[0] = a[0]

for i in range(1, n):
    if d[i] + d[i-1] > d[i]:
         d[i] = a[i] + d[i-1]
    else:
         d[i] = a[i]
         

print(max(d))
         
