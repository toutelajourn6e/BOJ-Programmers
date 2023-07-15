from collections import Counter

def solution(topping):
    chulsu = {}
    brother = Counter(topping)
    ans = 0
    
    for i in topping:
        chulsu[i] = chulsu.get(i, 0) + 1
        if brother[i] == 1: del brother[i]
        else: brother[i] -= 1
        
        if len(chulsu) == len(brother):
            ans += 1
            
    return ans