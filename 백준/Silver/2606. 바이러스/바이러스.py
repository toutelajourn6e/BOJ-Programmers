from collections import deque
import sys

def bfs(v):
    global result
    q = deque()
    q.append(v)
    visited[v] = True
    
    while q:
        v = q.popleft()
        
        for i in gragh[v]:
            if visited[i] == False:
                q.append(i)
                visited[i] = True
                result += 1
    

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())

visited = [False for _ in range(n+1)]
gragh = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    gragh[a].append(b)
    gragh[b].append(a)
    
result = 0

bfs(1)

print(result)