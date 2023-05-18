import sys
sys.setrecursionlimit(10**6)

n, m = map(int, sys.stdin.readline().rstrip().split())

visited = [False for _ in range(n+1)]
gragh = [[] for _ in range(n+1)]
result = 0

for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    gragh[a].append(b)
    gragh[b].append(a)

def dfs(x):
    visited[x] = True
    
    for i in gragh[x]:
        if visited[i] == False:
            dfs(i)
            
for i in range(1, n+1):
    if visited[i] == False:
        dfs(i)
        result += 1
        
print(result)