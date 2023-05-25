import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)
n = int(input().rstrip())
m = int(input().rstrip())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

via = [-1] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    graph[a].append((b, c))

start, end = map(int, input().rstrip().split())    
    
def dijkstra(start):
    pq = []
    heapq.heappush(pq, (0, start))
    distance[start] = 0
    
    while pq:
        dist, node = heapq.heappop(pq)
        if distance[node] < dist:
            continue
            
        for adj_node, adj_weight in graph[node]:
            cost = dist + adj_weight
            if cost < distance[adj_node]:
                distance[adj_node] = cost
                heapq.heappush(pq, (cost, adj_node))
                via[adj_node] = node
                
dijkstra(start)
print(distance[end])

path = [end]

while end != start:
    end = via[end]
    path.append(end)
    
path.reverse()
    
print(len(path))
print(*path)