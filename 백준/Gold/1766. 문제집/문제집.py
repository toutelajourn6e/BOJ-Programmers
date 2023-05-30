import heapq
import sys
input = sys.stdin.readline

def topology_sort():
    pq = []
    result = []
    for i in range(1, v+1):
        if indegree[i] == 0:
            heapq.heappush(pq, i)
            
    while pq:
        cur = heapq.heappop(pq)
        result.append(cur)
        
        for i in graph[cur]:
            indegree[i] -= 1
            if indegree[i] == 0:
                heapq.heappush(pq, i)
                
    print(*result)
    
v, e = map(int, input().split())
graph = [[] for _ in range(v+1)]
indegree = [0] * (v+1)

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1
    
topology_sort()
