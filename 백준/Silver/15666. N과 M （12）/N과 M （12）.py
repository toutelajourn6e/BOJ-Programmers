n, m = map(int, input().split())
a = sorted(list(map(int, input().split())))
rs = []
temp = set()

def dfs(start, depth):
    if depth == m:
        if not str(rs) in temp:
            print(' '.join(map(str, rs)))
            temp.add(str(rs))
        return
    
    for i in range(start, n):
        rs.append(a[i])
        dfs(i, depth+1)
        rs.pop()

dfs(0, 0)