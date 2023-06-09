def find(x, parent):
    if parent[x] != x:
        parent[x] = find(parent[x], parent)
    return parent[x]

def union(a, b, parent):
    a = find(a, parent)
    b = find(b, parent)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def solution(n, costs):
    parent = [i for i in range(n)]
    edges = []
    result = 0
    
    for a, b, cost in costs:
        edges.append((cost, a, b))
    
    edges.sort()
    
    for cost, a, b in edges:
        if find(a, parent) != find(b, parent):
            union(a, b, parent)
            result += cost
            
    return result
    
    
    
    
    
    