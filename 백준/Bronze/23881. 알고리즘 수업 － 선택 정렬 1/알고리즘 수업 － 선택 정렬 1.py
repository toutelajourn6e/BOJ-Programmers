import sys

n, k = map(int, input().split())
a = list(map(int, input().split()))
c = 0
for i in range(n-1,0,-1):
    max_idx = i
    for j in range(i-1,-1,-1):
        if a[j] > a[max_idx]:
            max_idx = j
    if a[i] != a[max_idx]:
        c += 1
        a[i], a[max_idx] = a[max_idx], a[i]
        if c == k:
            print(a[max_idx], a[i])
            sys.exit(0)
            
print(-1)