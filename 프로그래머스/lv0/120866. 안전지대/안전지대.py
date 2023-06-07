from collections import deque

def solution(board):
    n = len(board)
    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, -1, 1, -1, 1, -1, 1]
    q = deque()
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                q.append((i, j))
                
    while q:
        x, y = q.popleft()
        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]
                    
            if 0 <= nx < n and 0 <= ny < n:
                board[nx][ny] = 1                    
    count = 0
    
    for a in range(n):
        for b in range(n):
            if board[a][b] == 0:
                count += 1
                
    return count