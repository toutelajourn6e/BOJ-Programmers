import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a <= b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().rstrip().split())
parent = [0] * (n)
count = 0

for i in range(n):
    parent[i] = i
    

cycle = False

for _ in range(m):
    a, b = map(int, input().rstrip().split())
    if not cycle:
        count += 1 
    if find(a) == find(b):
        cycle = True
    else:
        union(a, b)
        
if cycle:
    print(count)
else:
    print(0)