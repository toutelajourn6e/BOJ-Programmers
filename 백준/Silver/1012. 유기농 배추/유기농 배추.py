from collections import deque
import sys

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    grid[x][y] = 0
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                if grid[nx][ny] == 1:
                    q.append((nx, ny))
                    grid[nx][ny] = 0
    
    
t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().rstrip().split())
    grid = [[0] * m for _ in range(n)]
    result = 0
    
    for i in range(k):
        x, y = map(int, sys.stdin.readline().rstrip().split())
        x, y = y, x
        grid[x][y] = 1
        
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                bfs(i, j)
                result += 1
                
    print(result)