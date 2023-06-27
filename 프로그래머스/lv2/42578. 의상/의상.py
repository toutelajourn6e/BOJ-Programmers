from collections import defaultdict

def solution(clothes):
    ans = 1
    clothes_type = defaultdict(int)
    
    for item, typ in clothes:
        clothes_type[typ] += 1
    
    for typ in clothes_type:
        ans *= clothes_type[typ] + 1
        
    return ans - 1