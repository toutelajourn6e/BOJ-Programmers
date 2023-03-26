from math import factorial as f

def solution(n):
    maximum = 0
    m = 0
    
    while maximum < n:
        m += 1
        if f(m) > n:
            m -= 1
            break
        maximum = f(m)
        
        
    return m