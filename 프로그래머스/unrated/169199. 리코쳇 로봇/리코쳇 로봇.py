from collections import deque

def solution(board):
    n, m = len(board), len(board[0])
    visited = [[False] * m for _ in range(n)]
    distance = [[0] * m for _ in range(n)]
    q = deque()
    Gx, Gy = 0, 0
    
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                q.append((i, j))
            if board[i][j] == 'G':
                Gx, Gy = i, j
    
    while q:
        x, y = q.popleft()
        visited[x][y] = True
        
        for i in [-1, 1]:
            nx, ny = x, y
            while 0 <= nx + i < n and board[nx+i][y] != 'D':
                nx += i
            else: 
                if nx != x and not visited[nx][y]:
                    q.append((nx, y))
                    if distance[nx][y] != 0:
                        distance[nx][y] = min(distance[nx][y], distance[x][y] + 1)
                    else: distance[nx][y] = distance[x][y] + 1
            while 0 <= ny + i < m and board[x][ny+i] != 'D':
                ny += i
            else:
                if ny != y and not visited[x][ny]:
                    q.append((x, ny))
                    if distance[x][ny] != 0:
                        distance[x][ny] = min(distance[x][ny], distance[x][y] + 1)
                    else: distance[x][ny] = distance[x][y] + 1
    
    return distance[Gx][Gy] if distance[Gx][Gy] else -1