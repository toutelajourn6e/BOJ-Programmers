n, m = map(int, input().split())

rs = []

def dfs():
    if len(rs) == m:
        print(' '.join(map(str, rs)))
        return
    
    for i in range(1, n+1):
        rs.append(i)
        dfs()
        rs.pop()
        
dfs()
        