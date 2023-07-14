def solution(info, edges):
    visited = [False] * len(info)
    ans = []
    
    def dfs(sheep, wolf):
        if sheep > wolf:
            ans.append(sheep)
        else: return
        
        for a, b in edges:
            if visited[a] and not visited[b]:
                visited[b] = True
                if not info[b]:
                    dfs(sheep+1, wolf)
                else:
                    dfs(sheep, wolf+1)
                visited[b] = False
                    
    visited[0] = True
    dfs(1, 0)
    return max(ans)