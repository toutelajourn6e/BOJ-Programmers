from collections import deque

def solution(board):
    n = len(board)
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    
    def bfs(cost, d):
        maps = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1: maps[i][j] = -1
                
        q = deque()
        q.append((0, 0, cost, d))
        
        while q:
            x, y, cost, d = q.popleft()
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < n and maps[nx][ny] != -1:
                    if d == i: newcost = cost + 100
                    else: newcost = cost + 600
                    
                    if not maps[nx][ny] or (maps[nx][ny] != 0 and maps[nx][ny] > newcost):
                        q.append((nx, ny, newcost, i))
                        maps[nx][ny] = newcost
        return maps[n-1][n-1]
    
    return min(bfs(0, 1), bfs(0, 3))
                