def solution(picks, minerals):
    ans = []
    partition = []
    
    for i in range(0, len(minerals), 5):
        partition.append(minerals[i:i+5])
    
        
    def dfs(fatigue, cnt):
        if cnt == len(partition) or not sum(picks):
            ans.append(fatigue)
            return
        
        for i in range(len(picks)):
            if not picks[i]: continue
            total = 0
            diamond = partition[cnt].count('diamond')
            iron = partition[cnt].count('iron')
            stone = partition[cnt].count('stone')
            if i == 0: total += (diamond + iron + stone)
            elif i == 1: total += ((diamond * 5) + iron + stone)
            else: total += ((diamond * 25) + (iron * 5) + stone)
            picks[i] -= 1
            dfs(fatigue + total, cnt + 1)
            picks[i] += 1
            
    dfs(0, 0)
    return min(ans)