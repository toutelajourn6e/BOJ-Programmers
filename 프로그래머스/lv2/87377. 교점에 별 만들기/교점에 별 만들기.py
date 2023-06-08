def solution(line):
    n = len(line)
    cross = []
    
    x_max = y_max = -int(1e10)
    x_min = y_min = int(1e10)
    
    for i in range(n):
        a, b, e = line[i]
        for j in range(i+1, n):
            c, d, f = line[j]
            if (a * d) - (b * c) == 0:
                continue
                
            x = ((b * f) - (e * d)) / ((a * d) - (b * c))
            y = ((e * c) - (a * f)) / ((a * d) - (b * c))
            
            if x == int(x) and y == int(y):
                x = int(x)
                y = int(y)
                
                cross.append((x, y))
                
                x_max, y_max = max(x_max, x), max(y_max, y)
                x_min, y_min = min(x_min, x), min(y_min, y)
                
    width = abs(x_max - x_min) + 1
    height = abs(y_max - y_min) + 1
    ans = [['.'] * width for _ in range(height)]
    cross = sorted(cross, key = lambda x: -x[1])
    
    for x, y in cross:
        ny = y_max - y
        nx = x - x_min
        ans[ny][nx] = '*'
        
    return list(map(''.join, ans))
    