import sys

n = int(input().rstrip())
cost = [[0, 0, 0]]
INF = 100001
input = sys.stdin.readline

for _ in range(n):
    cost.append(list(map(int, input().rstrip().split())))
    
result = INF

for j in [0, 1, 2]:
    d = [[0, 0, 0] for _ in range(n+1)]
    d[1] = [INF, INF, INF]
    d[1][j] = cost[1][j]
    
    for i in range(2, n+1):
        d[i][0] = min(d[i-1][1], d[i-1][2]) + cost[i][0]
        d[i][1] = min(d[i-1][0], d[i-1][2]) + cost[i][1]
        d[i][2] = min(d[i-1][0], d[i-1][1]) + cost[i][2]
    
    d[n][j] = INF
    result = min(result, min(d[n]))
    
print(result)