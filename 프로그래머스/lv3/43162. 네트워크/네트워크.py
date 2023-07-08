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

def solution(n, computers):
    result = set()
    parent = [i for i in range(n)]
    
    for i, computer in enumerate(computers):
        for j, connect in enumerate(computer):
            if connect:
                if find(parent, i) != find(parent, j):
                    union(parent, i, j)
                    
    for i in parent:
        result.add(find(parent, i))
        
    return len(result) 