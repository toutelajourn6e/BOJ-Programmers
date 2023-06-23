def solution(n, lost, reserve):
    lost = set(lost)
    common = lost.intersection(set(reserve))
    lost -= common
    reserve = set(reserve) - common
    
    for i in list(reserve): 
        if i-1 in lost: 
            lost.discard(i-1)
            continue
        if i+1 in lost:
            lost.discard(i+1)
            continue
        
        
        
    return n - len(lost)
            