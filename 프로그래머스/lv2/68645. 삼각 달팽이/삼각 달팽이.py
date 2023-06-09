def solution(n: int) -> list:
     # 아래쪽 오른쪽 좌측위
    dx = [1, 0, -1]
    dy = [0, 1, -1]
    snail = [[0 for _ in range(i+1)] for i in range(n)]
    
    x = y = angle = 0
    last = n * (n+1) // 2
    cnt = 1
    
    while cnt <= last:
        snail[x][y] = cnt
        cnt += 1
        nx = x + dx[angle]
        ny = y + dy[angle]
        
        if 0 <= nx < n and 0 <= ny < n and snail[nx][ny] == 0:
            x = nx
            y = ny
        else:
            angle = (angle + 1) % 3
            x = x + dx[angle]
            y = y + dy[angle]
            
    ans = sum(snail, [])
    
    return ans
    
    
    