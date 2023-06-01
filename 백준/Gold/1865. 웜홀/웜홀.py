import sys
input = sys.stdin.readline

def bf():
    distance[1] = 0
    
    for i in range(v):
        for cur, next_node, cost in edges:
            if distance[cur] + cost < distance[next_node]:
                distance[next_node] = distance[cur] + cost
                if i == v-1:
                    return 'YES'
    return 'NO'

t = int(input())
INF = int(1e9)

for _ in range(t):
    v, e, w = map(int, input().split())
    distance = [INF] * (v+1)
    edges = []
    
    for _ in range(e):
        a, b, t = map(int, input().split())
        edges.append((a, b, t))
        edges.append((b, a, t))
        
    for _ in range(w):
        s, e, t = map(int, input().split())
        edges.append((s, e, -t))
        
    print(bf())