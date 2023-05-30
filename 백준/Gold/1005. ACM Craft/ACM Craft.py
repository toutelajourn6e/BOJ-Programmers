from collections import deque
import sys
input = sys.stdin.readline

def topology_sort():
    q = deque()
    
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)
            d[i] += cost[i]
            
    while q:
        cur = q.popleft()

        for i in graph[cur]:
            indegree[i] -= 1
            d[i] = max(d[cur] + cost[i], d[i])
            if indegree[i] == 0:
                q.append(i)
        
        
t = int(input())

for _ in range(t):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    indegree = [0] * (v+1)
    cost = [0] + list(map(int, input().split()))
    d = [0] * (v+1)
    
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1
        
    w = int(input())
    
    topology_sort()
        
    print(d[w])
    
        
    