from collections import deque

n, k = map(int, input().split())
visited = [0] * 100001

def bfs():
    q = deque()
    q.append(n)
    
    while q:
        v = q.popleft()
        
        if v == k:
            print(visited[v])
            break
        
        for i in (v+1, v-1, v*2):
            if 0 <= i <= 100000 and visited[i] == 0:
                q.append(i)
                visited[i] = visited[v] + 1
                
bfs()