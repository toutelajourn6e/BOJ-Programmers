from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, y, v):
    q = deque()
    q.append((x, y))
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and grid[nx][ny] == v:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    
def bfs2(x, y, v):
    q = deque()
    q.append((x, y))
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and grid[nx][ny] == v:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                
                
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(input())
grid = [list(input()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
count1 = 0
              
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            visited[i][j] = True
            v = grid[i][j]
            bfs(i, j, v)
            count1 += 1
            
print(count1)

visited = [[False] * n for _ in range(n)]
count2 = 0

for i in range(n):
    for j in range(n):
        if grid[i][j] == 'G':
            grid[i][j] = 'R'

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            visited[i][j] = True
            v = grid[i][j]
            bfs(i, j, v)
            count2 += 1
            
print(count2)