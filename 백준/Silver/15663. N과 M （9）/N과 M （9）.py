n, m = map(int, input().split())
a = sorted(list(map(int, input().split())))
visited = [False] * n
rs = []
temp = set()

def dfs(depth):
    if depth == m:
        if not str(rs) in temp:
            print(' '.join(map(str, rs)))
            temp.add(str(rs))
            return
    
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            rs.append(a[i])
            dfs(depth+1)
            visited[i] = False
            rs.pop()

dfs(0)