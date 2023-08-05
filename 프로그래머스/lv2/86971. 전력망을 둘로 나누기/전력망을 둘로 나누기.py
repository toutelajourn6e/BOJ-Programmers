from collections import Counter

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent ,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def solution(n, wires):
    ans = 100000000
    
    for i in range(n-1):
        parent = [i for i in range(n)]
        for j in range(n-1):
            if i == j: continue
            a, b = wires[j][0]-1, wires[j][1]-1
            if find(parent, a) != find(parent, b):
                union(parent, a, b)
        
        u = []
        for i in parent:
            u.append(find(parent, parent[i]))
        
        p = Counter(u)
        result = list(p.values())
        ans = min(ans, abs(result[0] - result[1]))
        
    return ans