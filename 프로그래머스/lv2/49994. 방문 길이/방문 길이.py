def solution(dirs):
    visited = [[False] * 21 for _ in range(21)]
    x, y = 0, 0
    ans = 0
    
    for dir in dirs:
        if dir == 'U' and (-10 <= y+2 <= 10):
            if not visited[y+1][x]:
                visited[y+1][x] = True
                ans += 1
            y += 2
        elif dir == 'D' and (-10 <= y-2 <= 10):
            if not visited[y-1][x]:
                visited[y-1][x] = True  
                ans += 1
            y -= 2
        elif dir == 'L' and (-10 <= x-2 <= 10):
            if not visited[y][x-1]:
                visited[y][x-1] = True
                ans += 1
            x -= 2
        elif dir == 'R' and (-10 <= x+2 <= 10):
            if not visited[y][x+1]:
                visited[y][x+1] = True
                ans += 1
            x += 2
    return ans