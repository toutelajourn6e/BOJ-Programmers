from collections import deque
import sys
input = sys.stdin.readline

m, n, h = map(int, input().rstrip().split())
grid = [[list(map(int, input().rstrip().split())) for _ in range(n)] for _ in range(h)]


dx = [0, 0, 1, -1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
q = deque()

def bfs():
    while q:
        z, x, y = q.popleft()
        
        for i in range(6):
            nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
            
            if 0 <= nx < n and 0 <= ny < m and  0 <= nz < h:
                if grid[nz][nx][ny] == 0:
                    grid[nz][nx][ny] = grid[z][x][y] + 1
                    q.append((nz, nx, ny))
                    



for i in range(h):
    for j in range(n):
        for k in range(m):
            if grid[i][j][k] == 1:
                q.append((i, j, k))
        
bfs()

result = 0

for i in range(h):
    for j in range(n):
        for k in range(m):
            if grid[i][j][k] == 0:
                print(-1)
                sys.exit(0)
            result = max(result, grid[i][j][k])

print(result - 1)

