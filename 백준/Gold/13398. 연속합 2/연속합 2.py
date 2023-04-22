n = int(input())
a = list(map(int, input().split()))
d = [0] * n
dr = [0] * n

for i in range(n):
    d[i] = a[i]
    if i == 0:
        continue
    if a[i] < a[i] + d[i-1]:
        d[i] = a[i] + d[i-1]

for i in range(n-1,-1,-1):
    dr[i] = a[i]
    if i == n-1:
        continue
    if a[i] < a[i] + dr[i+1]:
        dr[i] = a[i] + dr[i+1]
        
ans = max(d)
for i in range(1, n-1):
    if ans < d[i-1] + dr[i+1]:
        ans = d[i-1] + dr[i+1]
print(ans)