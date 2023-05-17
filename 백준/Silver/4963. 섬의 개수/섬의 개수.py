import sys
sys.setrecursionlimit(10 ** 5)

while True:
    w, h = map(int, sys.stdin.readline().rsplit())
    if w == 0 and h == 0:
        break
        
    gragh = []
    for _ in range(h):
        gragh.append(list(map(int, sys.stdin.readline().rsplit())))
        
    def dfs(x, y):
        if x < 0 or x >= h or y < 0 or y >= w:
            return False
        
        if gragh[x][y] == 1:
            gragh[x][y] = 0
            
            dfs(x, y-1)
            dfs(x, y+1)
            dfs(x+1, y)
            dfs(x-1, y)
            dfs(x+1, y+1)
            dfs(x+1, y-1)
            dfs(x-1, y+1)
            dfs(x-1, y-1)
            
            return True
        
        return False
    
    
    answer = 0

    for i in range(h):
        for j in range(w):
            if dfs(i, j) == True:
                answer += 1
            
    print(answer)
        