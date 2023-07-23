def solution(n, s, A, B, fares):
    INF = int(1e9)
    graph = [[INF] * (n+1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j: graph[i][j] = 0
            
    for a, b, c in fares:
        graph[a][b] = c
        graph[b][a] = c
    
    for k in range(1, n+1):
        for a in range(1, n+1):
            for b in range(1, n+1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
    
    ans = int(1e9)
    for k in range(1, n+1):
        distance = graph[s][k]
        for i in range(1, n+1):
            distance += graph[k][A]
            distance += graph[k][B]
            ans = min(ans, distance)
            
    return ans    