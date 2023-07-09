from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    visited = [[False] * m for _ in range(n)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    q = deque()
    q.append((0, 0))
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny]:
                visited[nx][ny] = True
                maps[nx][ny] = maps[x][y] + 1
                q.append((nx, ny))
                
    return -1 if maps[n-1][m-1] == 1 else maps[n-1][m-1]
                
            
            
            
            
            
            