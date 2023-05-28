n = int(input())
m = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
parent = list(range(n))
plan = list(map(int, input().split()))


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            union(i, j)

result = 'YES'

for i in range(1, m):
    if parent[plan[0]-1] != parent[plan[i]-1]:
        result = 'NO'
        break

print(result)