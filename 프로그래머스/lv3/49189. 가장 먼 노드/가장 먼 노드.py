import heapq as hq

def dijkstra(start, distance, graph):
    pq = []
    hq.heappush(pq, (0, start))
    distance[start] = 0
    
    while pq:
        dist, cur = hq.heappop(pq)
        if distance[cur] < dist:
            continue
        
        for next_node, weight in graph[cur]:
            cost = distance[cur] + weight
            if cost < distance[next_node]:
                distance[next_node] = cost
                hq.heappush(pq, (cost, next_node))


def solution(n, edge):
    INF = int(1e9)
    distance = [INF] * (n+1)
    graph = [[] for _ in range(n+1)]
    
    for a, b in edge:
        graph[a].append((b, 1))
        graph[b].append((a, 1))
        
    dijkstra(1, distance, graph)
        
    max_v = max(distance[1:])
    
    return distance[1:].count(max_v)
    