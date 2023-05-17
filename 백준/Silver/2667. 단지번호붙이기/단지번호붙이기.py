from collections import deque

def bfs(x, y):
    global ans
    count = 0
    q = deque()
    q.append((x, y))
    grid[x][y] = 0 
    
    while q:
        x, y = q.popleft()
        count += 1
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n:
                if grid[nx][ny] == 1:
                    q.append((nx, ny))
                    grid[nx][ny] = 0
    return ans.append(count)
n = int(input())
grid = [list(map(int, input())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = 0
ans = []

for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            bfs(i, j)
            result += 1
            
print(result)

ans.sort()

for i in ans:
    print(i)
        
    