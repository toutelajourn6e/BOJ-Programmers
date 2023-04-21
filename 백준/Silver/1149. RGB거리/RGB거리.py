n = int(input())
a = [[0,0,0]] + [list(map(int, input().split())) for _ in range(n)]
d = [[0,0,0] for _ in range(n+1)]

for n in range(n+1):
    d[n][0] = min(d[n-1][1], d[n-1][2]) + a[n][0]
    d[n][1] = min(d[n-1][0], d[n-1][2]) + a[n][1]
    d[n][2] = min(d[n-1][0], d[n-1][1]) + a[n][2]
    
print(min(d[n][0], d[n][1], d[n][2]))
    