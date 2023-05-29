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
        

v = int(input())
e = int(input())
parent = [0] * (v+1)
edges = []
result = 0

for i in range(1, v+1):
    parent[i] = i
    
for _ in range(e):
    a, b, cost = map(int, input().rstrip().split())
    edges.append((cost, a, b))
    
edges.sort()

for edge in edges:
    cost, a, b = edge
    if find(a) != find(b):
        union(a, b)
        result += cost
        
print(result)