n, m = map(int, input().split())

rs = []

def dfs(start):
    if len(rs) == m:
        print(' '.join(map(str, rs)))
        return
    
    for i in range(start, n+1):
        if not i in rs:
            rs.append(i)
            dfs(i+1)
            rs.pop()
            
dfs(1)