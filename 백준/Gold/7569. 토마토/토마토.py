from collections import deque


m, n, h = map(int, input().split())
grid = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]


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

flag = False
result = 0

for i in range(h):
    for j in range(n):
        for k in range(m):
            if grid[i][j][k] == 0:
                flag = True
            result = max(result, grid[i][j][k])

if flag:
    print(-1)
else:
    print(result - 1)

