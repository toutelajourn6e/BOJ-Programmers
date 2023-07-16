def solution(k, dungeons):
    ans = [0]
    
    def explore(k, clear):
        if clear:
            ans.append(len(clear))
        
        for i in range(len(dungeons)):
            if i not in clear and k >= dungeons[i][0]:
                clear.append(i)
                explore(k-dungeons[i][1], clear)
                clear.pop()
                
    explore(k, [])
    return max(ans)