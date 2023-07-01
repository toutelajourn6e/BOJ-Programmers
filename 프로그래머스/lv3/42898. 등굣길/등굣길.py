def solution(m, n, puddles):
    maps = [[0] * (m+1) for _ in range(n+1)]
    
    for i in puddles:
        x, y = i
        maps[y][x] = 'X'
        
    maps[1][1] = 1
        
    for i in range(1, n+1):
        for j in range(1, m+1):
            if maps[i][j] == 'X':
                continue
            if maps[i][j-1] != 'X':
                maps[i][j] += maps[i][j-1] % 1000000007
            if maps[i-1][j] != 'X':
                maps[i][j] += maps[i-1][j] % 1000000007
    
    return maps[n][m] % 1000000007