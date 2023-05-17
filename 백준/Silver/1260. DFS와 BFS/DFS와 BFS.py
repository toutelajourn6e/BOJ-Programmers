from collections import deque
import sys

def dfs(v):
    visited[v] = True
    result_dfs.append(v)
    
    for i in sorted(gragh[v]):
        if visited[i] == False:
            dfs(i)
    
def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = True
    
    while q:
        v = q.popleft()
        result_bfs.append(v)
        
        for i in sorted(gragh[v]):
            if visited[i] == False:
                q.append(i)
                visited[i] = True

n, m, v = map(int, input().split())

gragh = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    gragh[a].append(b)
    gragh[b].append(a)

result_dfs = []
result_bfs = []

visited = [False for _ in range(n+1)]
         
dfs(v)
visited = [False for _ in range(n+1)]
bfs(v)

print(*result_dfs)
print(*result_bfs)
