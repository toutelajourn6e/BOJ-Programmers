import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)
n, m = map(int, input().rstrip().split())
gragh = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    gragh[a].append((b, c))
    gragh[b].append((a, c))
    
u, v = map(int, input().rstrip().split())
    
def dijkstra(start):
    distance = [INF] * (n+1)
    pq = []
    heapq.heappush(pq, (0, start))
    distance[start] = 0
    
    while pq:
        dist, node = heapq.heappop(pq)
        if distance[node] < dist:
            continue
        
        for i in gragh[node]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(pq, (cost, i[0]))
                
    return distance


first = dijkstra(1)
second = dijkstra(u)
third = dijkstra(v)

path1 = first[u] + second[v] + third[n]
path2 = first[v] + third[u] + second[n]

result = min(path1, path2)

print(result if result < INF else -1)
    
    