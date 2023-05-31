import sys
input = sys.stdin.readline

def bf(start):
    distance[start] = 0
    
    for i in range(v):
        for j in range(e):
            cur = edges[j][0]
            next_node = edges[j][1]
            cost = edges[j][2]
            if distance[cur] != INF and distance[cur] + cost < distance[next_node]:
                distance[next_node] = distance[cur] + cost
                if i == v-1:
                    return True
    return False



INF = int(1e9)
v, e = map(int, input().split())
edges = []
distance = [INF] * (v+1)

for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((a, b, cost))
    
n_cycle = bf(1)

if n_cycle:
    print(-1)
else:
    for i in range(2, v+1):
        if distance[i] == INF:
            print(-1)
        else:
            print(distance[i])