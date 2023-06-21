def solution(n, m, section):
    wall = [1 for _ in range(section[-1]+1)]
    ans = 0
    
    for s in section:
        wall[s] = 0
        
    for i in range(1, len(wall)):
        if wall[i] == 0:
            for j in range(0, m):
                if i+j < len(wall):
                    wall[i+j] = 1
            ans += 1
                
    return ans