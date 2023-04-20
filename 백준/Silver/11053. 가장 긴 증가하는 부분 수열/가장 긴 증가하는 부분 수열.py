import sys

t = int(sys.stdin.readline().rstrip())

a = [0] + list(map(int, sys.stdin.readline().rstrip().split()))
d = [1] * (t+1)
    
for i in range(1, t+1):
    for j in range(1, i):
        if a[j] < a[i]:
            if d[j] == d[i]:
                d[i] += 1
            
print(max(d))