def solution(n,a,b):
    round = 1
    
    while True:
        if a % 2: a = (a + 1) // 2
        else: a //= 2
            
        if b % 2: b = (b + 1) // 2
        else: b //= 2
        
        if a == b:
            break
        
        round += 1
        
    return round