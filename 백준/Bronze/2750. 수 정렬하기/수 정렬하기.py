import sys

n = int(sys.stdin.readline().rstrip())
a = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

for i in range(n-1):
    min_idx = i
    for j in range(i+1, n):
        if a[j] < a[min_idx]:
            min_idx = j
    a[i], a[min_idx] = a[min_idx], a[i]
    
for k in a:
    print(k)