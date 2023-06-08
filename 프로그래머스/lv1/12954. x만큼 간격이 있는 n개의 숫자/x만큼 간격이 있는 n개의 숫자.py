def solution(x, n):
    ans = []
    d = x
    while True:
        if len(ans) == n:
            break
            
        ans.append(d)
        d += x
        
    return ans