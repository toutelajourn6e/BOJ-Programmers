def solution(grid):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    n, m = len(grid), len(grid[0])
    ans = []
    path = set()
    
    def go(x, y, d):
        if grid[x][y] == 'S':
            x += directions[d][0]
            y += directions[d][1]
        elif grid[x][y] == 'L':
            d = (d - 1) % 4
            x += directions[d][0]
            y += directions[d][1]
        elif grid[x][y] == 'R':
            d = (d + 1) % 4
            x += directions[d][0]
            y += directions[d][1]
        
        x %= n
        y %= m
        return x, y, d
            
    for i in range(n):
        for j in range(m):
            for k in range(4):
                distance = 0
                while (i, j, k) not in path:
                    path.add((i, j, k))
                    i, j, k = go(i, j, k)
                    distance += 1
                if distance: ans.append(distance)
                  
    return sorted(ans)