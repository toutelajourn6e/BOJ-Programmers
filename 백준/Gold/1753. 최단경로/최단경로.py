import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)
n, m = map(int, input().rstrip().split())
start = int(input().rstrip())
gragh = [[] for _ in range(n+1)]
distance = [INF for _ in range(n+1)]


for _ in range(m):
    u, v, w = map(int, input().rstrip().split())
    gragh[u].append((v, w))
    
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

for i in range(1, n+1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])