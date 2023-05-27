import sys
input = sys.stdin.readline

INF = int(1e9)
n, m = map(int, input().rstrip().split())
graph = [[INF] * (n+1) for _ in range(n+1)]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0
            
for _ in range(m):
    a, b = map(int, input().rstrip().split())
    graph[a][b] = 1
    graph[b][a] = 1
    
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
            
result = []

for index, i in enumerate(graph):
    if index == 0:
        continue
    kv_idx = sum(i[1:])
    result.append((kv_idx, index))
    
        
result = sorted(result, key = lambda x: (x[0], x[1]))
print(result[0][1])