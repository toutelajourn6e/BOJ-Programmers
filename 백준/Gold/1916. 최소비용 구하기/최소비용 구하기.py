import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)
n = int(input().rstrip())
m = int(input().rstrip())
gragh = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    u, v, w = map(int, input().rstrip().split())
    gragh[u].append((v, w))
    
start, end = map(int, input().rstrip().split())

def dijkstra(start):
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
                
dijkstra(start)
                
print(distance[end])
    