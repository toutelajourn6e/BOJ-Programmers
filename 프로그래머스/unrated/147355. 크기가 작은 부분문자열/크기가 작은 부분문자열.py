def solution(t, p):
    result = 0
    n = len(t)
    k = len(p)
    p = int(p)
    window = 0
    
    for i in range(k, n+1):
        window = int(t[i-k:i])
        if window <= p:
            result += 1
        
    return result