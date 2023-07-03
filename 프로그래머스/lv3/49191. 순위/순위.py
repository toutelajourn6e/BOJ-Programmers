def solution(n, results):
    INF = int(1e9)
    graph = [[INF] * (n+1) for _ in range(n+1)]
    ans = 0
    
    for i in range(n+1):
        for j in range(n+1):
            if i == j:
                graph[i][j] = 0
            
    for a, b in results:
        graph[a][b] = 1
        graph[b][a] = -1
            
    for k in range(n+1):
        for i in range(n+1):
            for j in range(n+1):
                if graph[i][k] == 1 and graph[k][j] == 1:
                    graph[i][j] = 1
                elif graph[i][k] == -1 and graph[k][j] == -1:
                    graph[i][j] = -1
    
    for i in range(1, n+1):
        if INF in graph[i][1:]:
            continue
        ans += 1
    
    return ans