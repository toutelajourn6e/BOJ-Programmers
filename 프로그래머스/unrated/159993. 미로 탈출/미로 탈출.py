from collections import deque

def solution(maps):
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    n, m = len(maps), len(maps[0])
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                start = (i, j)
            elif maps[i][j] == 'L':
                lever = (i, j)
            elif maps[i][j] == 'E':
                end = (i, j)
                
    def bfs(start, target):
        distance = [[0] * m for _ in range(n)]
        visited = [[False] * m for _ in range(n)]
        visited[start[0]][start[1]] = True
        q = deque()
        q.append(start)
        
        while q:
            x, y = q.popleft()
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny] != 'X':
                    visited[nx][ny] = True
                    distance[nx][ny] = distance[x][y] + 1
                    q.append((nx, ny))
        
        return distance[target[0]][target[1]]
         
    to_l = bfs(start, lever)
    to_e = bfs(lever, end)
    
    return -1 if not to_l or not to_e else to_l + to_e