from collections import defaultdict

def solution(k, tangerine):
    typ = defaultdict(int)
    remove = len(tangerine) - k
    ans = 0
    
    for i in tangerine:
        typ[i] += 1
        
    box = sorted(typ.items(), key=lambda x: x[1])
    
    for x in box:
        if remove < x[1]:
            break
        else:
            ans += 1
            remove -= x[1]
            
    return len(set(tangerine)) - ans