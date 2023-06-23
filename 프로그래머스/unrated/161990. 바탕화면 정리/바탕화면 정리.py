def solution(wallpaper):
    n = len(wallpaper)
    m = len(wallpaper[0])
    x = []
    y = []
    
    for i in range(n):
        for j in range(m):
            if wallpaper[i][j] == '#':
                x.append(i)
                y.append(j)
            
    return [min(x), min(y), max(x)+1, max(y)+1]