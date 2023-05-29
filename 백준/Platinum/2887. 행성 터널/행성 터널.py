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
        

v = int(input())
parent = [i for i in range(v)]
edges = []
result = 0

X = []
Y = []
Z = []

for i in range(v):
    x, y, z = map(int, input().split())
    X.append((x, i))
    Y.append((y, i))
    Z.append((z, i))
    
X.sort()
Y.sort()
Z.sort()

for i in range(v-1):
    edges.append((abs(X[i+1][0] - X[i][0]), X[i][1], X[i+1][1]))
    edges.append((abs(Y[i+1][0] - Y[i][0]), Y[i][1], Y[i+1][1]))
    edges.append((abs(Z[i+1][0] - Z[i][0]), Z[i][1], Z[i+1][1]))

edges.sort()

for cost, a, b in edges:
    if find(a) != find(b):
        union(a, b)
        result += cost
        
print(result)