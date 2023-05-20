n, m = map(int, input().split())
rs = []

def dfs(start, depth):
    if depth == m:
        print(' '.join(map(str, rs)))
        return
    
    for i in range(start, n+1):
        rs.append(i)
        dfs(i ,depth+1)
        rs.pop()
            
dfs(1, 0)