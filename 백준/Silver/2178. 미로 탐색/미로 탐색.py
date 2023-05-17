from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        
            if 0 <= nx < n and 0 <= ny < m:
                if grid[nx][ny] == 1:
                    grid[nx][ny] = grid[x][y] + 1
                    q.append((nx, ny))
                    
    
    return grid[n-1][m-1]
                    
                    
                    
n, m = map(int, input().split())

grid = []

for _ in range(n):
    grid.append(list(map(int, input())))
                
ans = bfs(0, 0)

print(ans)