n, m = map(int, input().split())
a = sorted(list(map(int, input().split())))
visited = [False] * n
rs = []

def dfs(depth):
    if depth == m:
        print(' '.join(map(str, rs)))
        return
    
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            rs.append(a[i])
            dfs(depth+1)
            visited[i] = False
            rs.pop()

dfs(0)