from collections import deque

n, m, v = map(int, input().split())

gragh = [[] for _ in range(n+1)]
for _ in range(m):
    edge = list(map(int, input().split()))
    gragh[edge[0]].append(edge[1])
    gragh[edge[1]].append(edge[0])
    
for i in range(len(gragh)):
    gragh[i] = sorted(gragh[i])

result_dfs = []
result_bfs = []
visited_dfs = [False for _ in range(n+1)]
visited_bfs = [False for _ in range(n+1)]


def dfs(gragh, v):
    visited_dfs[v] = True
    result_dfs.append(v)
    
    for i in gragh[v]:
        if visited_dfs[i] == False:
            dfs(gragh, i)
    
def bfs(gragh, v):
    q = deque()
    q.append(v)
    visited_bfs[v] = True
    
    while q:
        v = q.popleft()
        result_bfs.append(v)
        
        for i in gragh[v]:
            if visited_bfs[i] == False:
                q.append(i)
                visited_bfs[i] = True
                
dfs(gragh, v)
bfs(gragh, v)

print(' '.join(map(str, result_dfs)))
print(' '.join(map(str, result_bfs)))
