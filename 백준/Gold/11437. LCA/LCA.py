import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def dfs(x, depth):
    d[x] = depth
    visited[x] = True
    
    for i in graph[x]:
        if visited[i]:
            continue
        parent[i] = x
        dfs(i, depth+1)
        
def lca(a, b):
    while d[a] != d[b]:
        if d[a] > d[b]:
            a = parent[a]
        else:
            b = parent[b]
            
    while a != b:
        a = parent[a]
        b = parent[b]
    
    return a


v = int(input())

parent = [0] * (v+1)
d = [0] * (v+1)
visited = [False] * (v+1)
graph = [[] for _ in range(v+1)]

for _ in range(v-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    

dfs(1, 0)

m = int(input())

for _ in range(m):
    a, b = map(int, input().split())
    print(lca(a, b))