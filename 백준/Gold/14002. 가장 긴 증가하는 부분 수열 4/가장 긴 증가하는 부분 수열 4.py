import sys

t = int(sys.stdin.readline().rstrip())

a = list(map(int, sys.stdin.readline().rstrip().split()))
d = [0] * (t)
v = [-1] * (t)
    
for i in range(t):
    d[i] = 1
    for j in range(i):
        if a[j] < a[i]:
            if d[j] == d[i]:
                d[i] += 1
                v[i] = j
                
ans = max(d)            
print(ans)

p = [i for i, x in enumerate(d) if x == ans][0]


def back(p):
    if p == -1:
        return
    back(v[p])
    print(a[p], end=' ')
    
back(p)
    