from collections import deque
import copy
import sys
input = sys.stdin.readline


def bfs():
    q = deque()
    test_grid = copy.deepcopy(grid)
    
    for i in range(n):
        for j in range(m):
            if test_grid[i][j] == 2:
                q.append((i, j))
                
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                if test_grid[nx][ny] == 0:
                    test_grid[nx][ny] = 2
                    q.append((nx, ny))
                    
    global result
    temp = 0
    for i in range(n):
        for j in range(m):
            if test_grid[i][j] == 0:
                temp += 1
                
    result = max(result, temp)
    

def wall(count):
    if count == 3:
        bfs()
        return
        
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0:
                grid[i][j] = 1
                wall(count+1)
                grid[i][j] = 0
                
                

n, m = map(int, input().rstrip().split())
grid = [list(map(int, input().rstrip().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = 0

wall(0)

print(result)
