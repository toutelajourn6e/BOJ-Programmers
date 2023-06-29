from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, maps, n, m, visited):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    sum_v = int(maps[x][y])
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if maps[nx][ny] != 'X':
                    sum_v += int(maps[nx][ny])
                    visited[nx][ny] = True
                    q.append((nx, ny))
    return sum_v

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    visited = [[False for _ in range(m)] for _ in range(n)]
    result = []
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] != 'X' and not visited[i][j]:
                result.append(bfs(i, j, maps, n, m, visited))
                
    if result: return sorted(result)
    else: return [-1]