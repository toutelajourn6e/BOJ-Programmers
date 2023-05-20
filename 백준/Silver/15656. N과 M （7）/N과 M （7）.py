n, m = map(int, input().split())
a = sorted(list(map(int, input().split())))
rs = []

def dfs(depth):
    if depth == m:
        print(' '.join(map(str, rs)))
        return
    
    for i in range(n):
        rs.append(a[i])
        dfs(depth+1)
        rs.pop()

dfs(0)