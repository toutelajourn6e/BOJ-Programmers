import heapq as hq

def solution(N, road, K):
    INF = int(1e9)
    graph = [[] for _ in range(N+1)]
    distance = [INF] * (N+1)
    
    for a, b, cost in road:
        graph[a].append((b, cost))
        graph[b].append((a, cost))
    
    def dijkstra(start):
        q = [(0, start)]
        distance[start] = 0
        
        while q:
            dist, cur = hq.heappop(q)
            if distance[cur] < dist:
                continue
            
            for next, weight in graph[cur]:
                if distance[next] > weight + distance[cur]:
                    cost = weight + distance[cur]
                    distance[next] = cost
                    hq.heappush(q, (cost, next))
    dijkstra(1)
    return len([distance[i] for i in range(1, len(distance)) if distance[i] <= K])