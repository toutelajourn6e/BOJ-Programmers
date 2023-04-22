n = int(input())
a = list(map(int, input().split()))
d1 = [0] * n
d2 = [0] * n

for i in range(n):
    d1[i] = 1
    for j in range(i):
        if a[j] < a[i] and d1[i] < d1[j] + 1:
            d1[i] = d1[j] + 1
            
for k in range(n-1,-1,-1):
    d2[k] = 1
    for l in range(k+1, n):
        if a[l] < a[k] and d2[k] < d2[l] + 1:
            d2[k] = d2[l] + 1
            
ans = [d1[i] + d2[i] - 1 for i in range(n)]

print(max(ans))