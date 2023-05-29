import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    ra = find(a)
    rb = find(b)
    if ra < rb:
        parent[rb] = ra
    else:
        parent[ra] = rb
        

v, e = map(int, input().split())
parent = [0] * (v+1)
edges = []
select = []
result = 0

for i in range(1, v+1):
    parent[i] = i
    
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))
    
edges.sort()

for edge in edges:
    cost, a, b = edge
    if find(a) != find(b):
        union(a, b)
        result += cost
        select.append(cost)
        
result -= select.pop()

print(result)
        
