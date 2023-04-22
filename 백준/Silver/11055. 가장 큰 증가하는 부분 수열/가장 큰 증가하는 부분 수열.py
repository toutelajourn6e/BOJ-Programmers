n = int(input())
a = list(map(int, input().split()))
d = [0] * n
d[0] = a[0]

for i in range(1, n):
    d[i] = a[i]
    for j in range(i):
        if a[j] < a[i] and d[i] < d[j] + a[i]:
            d[i] = d[j] + a[i]
    
print(max(d))