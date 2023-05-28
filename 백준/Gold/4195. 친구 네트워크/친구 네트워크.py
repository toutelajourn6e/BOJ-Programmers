import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    
    if a != b:
        parent[b] = a
        number[a] += number[b]


t = int(input().rstrip())

for _ in range(t):
    n = int(input().rstrip())
    parent = {}
    number = {}
    
    for _ in range(n):
        a, b = input().rstrip().split()
        if a not in parent:
            parent[a] = a
            number[a] = 1
        if b not in parent:
            parent[b] = b
            number[b] = 1
            
        union(a, b)
        
        print(number[find(a)])
    