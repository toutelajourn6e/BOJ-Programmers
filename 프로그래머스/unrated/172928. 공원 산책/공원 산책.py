def solution(park, routes):
    n = len(park)
    m = len(park[0])
    cur = (0, 0)
    d = [1, -1] # E W S N
    
    for i, j in enumerate(park):
        if 'S' in j:
            cur = (i, j.index('S'))
        
    for route in routes:
        direction, move = route.split()
        move = int(move)
        x, y = cur
        
        if direction == 'E' and (0 <= y + (move * d[0]) < m):
            for _ in range(move):
                y += d[0]
                if park[x][y] == 'X':
                    break
            else:
                cur = x, y
        
        elif direction == 'W' and (0 <= y + (move * d[1]) < m):
            for _ in range(move):
                y += d[1]
                if park[x][y] == 'X':
                    break
            else:
                cur = x, y
            
        elif direction == 'S' and (0 <= x + (move * d[0]) < n):
            for _ in range(move):
                x += d[0]
                if park[x][y] == 'X':
                    break
            else:
                cur = x, y
            
        if direction == 'N' and (0 <= x + (move * d[1]) < n):
            for _ in range(move):
                x += d[1]
                if park[x][y] == 'X':
                    break
            else:
                cur = x, y
            
    return list(cur)
            
            
            
            
            
        
        