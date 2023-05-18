from collections import deque
import sys

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                if grid[nx][ny] == 0:
                    grid[nx][ny] = grid[x][y] + 1
                    q.append((nx, ny))
                    


m, n = map(int, sys.stdin.readline().rstrip().split())
grid = []
q = deque()
result = 0

for _ in range(n):
    grid.append(list(map(int, sys.stdin.readline().rstrip().split())))
    
for i in range(n):
    for j in range(m):
        if grid[i][j] == 1:
            q.append((i, j))
        
bfs()

for i in grid:
    for j in i:
        if j == 0:
            print(-1)
            sys.exit(0)
    result = max(result, max(i))  

print(result - 1)