def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def solution(n, costs):
    result = 0
    parent = [i for i in range(n)]
    edges = []
    
    for a, b, cost in costs:
        edges.append((cost, a, b))
    
    edges.sort()
    
    for cost, a, b in edges:
        if find(parent, a) != find(parent, b):
            union(parent, a, b)
            result += cost
            
            
    return result