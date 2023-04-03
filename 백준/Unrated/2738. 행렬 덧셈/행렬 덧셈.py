n, m = map(int, input().split())
a = list()
b = list()

for i in range(n):
    i = list(map(int, input().split()))
    a.append(i)

for j in range(n):
    j = list(map(int, input().split()))
    b.append(j)
    
for k in range(n):
    for l in range(m):
        print(a[k][l] + b[k][l], end=' ')
    print()