def solution(cards):
    chosen = set()
    ans = 0
    
    def dfs(cur, select, cnt, flag):
        cur = cards[cur] - 1
        if select & (1 << cur):
            if flag:
                chosen.add((select, cnt))
            return cnt
        
        return dfs(cur, select | 1 << cur, cnt+1, flag)
        
        
    for i in range(len(cards)):
        dfs(i, 1 << i, 1, True)
        
    for visited, a in chosen:
        temp = 0
        for i in range(len(cards)):
            if not visited & 1 << i:
                temp = max(temp, dfs(i, visited | 1 << i, 1, False))
        ans = max(ans, temp * a)
        
    return ans