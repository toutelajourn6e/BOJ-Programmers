def solution(board, skill):
    n = len(board)
    m = len(board[0])
    demage = [[0] * (m+1) for _ in range(n+1)]
    ans = 0
    
    for type, r1, c1, r2, c2, degree in skill:
        if type == 1: degree *= -1
        demage[r1][c1] += degree
        demage[r1][c2+1] += -degree
        demage[r2+1][c1] += -degree
        demage[r2+1][c2+1] += degree
        
    for i in range(n):
        for j in range(m):
            demage[i][j+1] += demage[i][j]
            
    for j in range(m):
        for i in range(n):
            demage[i+1][j] += demage[i][j]
            
    for i in range(n):
        for j in range(m):
            board[i][j] += demage[i][j]
            if board[i][j] > 0: ans += 1
            
    return ans