import sys
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

while True:
    v, e = map(int, input().split())
    
    if v == 0 and e == 0:
        break
        
    parent = [i for i in range(v+1)]
    edges = []
    result = 0
    
    for _ in range(e):
        a, b, cost = map(int, input().split())
        edges.append((cost, a, b))
    
    edges.sort()

    for cost, a, b in edges:
        if find(a) != find(b):
            union(a, b)
        else:
            result += cost
        
    print(result)
